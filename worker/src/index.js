/**
 * Harmony-Flux — Moderation Worker
 * ----------------------------------
 * Endpoints :
 *   POST /submit    public  — Reçoit un avis visiteur (Turnstile + rate-limit)
 *   GET  /pending   admin   — Liste des avis en attente
 *   POST /approve   admin   — Approuve un avis et commit dans temoignages.json
 *   POST /reject    admin   — Supprime un avis en attente
 *   GET  /health    public  — Sanity check
 *
 * Bindings requis (wrangler.toml) :
 *   - KV namespace MOD_KV
 *
 * Secrets (wrangler secret put) :
 *   - GITHUB_TOKEN      Fine-grained PAT, scope contents:write sur harmony-flux
 *   - ADMIN_TOKEN       Token aléatoire 32 octets (saisi 1x dans admin.html)
 *   - TURNSTILE_SECRET  Cloudflare Turnstile (anti-bot, gratuit)
 *
 * Variables (wrangler.toml [vars]) :
 *   - GITHUB_REPO       "phm045/harmony-flux"
 *   - GITHUB_BRANCH     "main"
 *   - TEMOIGNAGES_PATH  "temoignages.json"
 *   - ALLOWED_ORIGIN    "https://phm045.github.io"  (ou domaine custom)
 */

const MAX_TEXT_LEN = 2000;
const MAX_FIELD_LEN = 100;
const RATE_LIMIT_PER_HOUR = 3;          // 3 avis/heure/IP
const PENDING_TTL_SECONDS = 60 * 60 * 24 * 30; // 30 jours

// ---------- Helpers ----------

function corsHeaders(env) {
  return {
    'Access-Control-Allow-Origin': env.ALLOWED_ORIGIN || '*',
    'Access-Control-Allow-Methods': 'GET, POST, OPTIONS',
    'Access-Control-Allow-Headers': 'Content-Type, Authorization',
    'Access-Control-Max-Age': '86400',
  };
}

function json(data, status, env) {
  return new Response(JSON.stringify(data), {
    status,
    headers: {
      'Content-Type': 'application/json; charset=utf-8',
      ...corsHeaders(env),
    },
  });
}

function sanitize(str, maxLen) {
  if (typeof str !== 'string') return '';
  return str.trim().slice(0, maxLen).replace(/[\u0000-\u001F\u007F]/g, '');
}

function isAdmin(request, env) {
  const auth = request.headers.get('Authorization') || '';
  const token = auth.replace(/^Bearer\s+/i, '');
  if (!token || !env.ADMIN_TOKEN) return false;
  // Comparaison constante
  if (token.length !== env.ADMIN_TOKEN.length) return false;
  let diff = 0;
  for (let i = 0; i < token.length; i++) {
    diff |= token.charCodeAt(i) ^ env.ADMIN_TOKEN.charCodeAt(i);
  }
  return diff === 0;
}

async function verifyTurnstile(token, ip, env) {
  if (!env.TURNSTILE_SECRET) return true; // désactivé si pas configuré
  if (!token) return false;
  const body = new FormData();
  body.append('secret', env.TURNSTILE_SECRET);
  body.append('response', token);
  if (ip) body.append('remoteip', ip);
  const resp = await fetch('https://challenges.cloudflare.com/turnstile/v0/siteverify', {
    method: 'POST',
    body,
  });
  const data = await resp.json();
  return !!data.success;
}

async function checkRateLimit(ip, env) {
  const key = `rl:${ip}:${new Date().toISOString().slice(0, 13)}`; // par heure
  const cur = parseInt(await env.MOD_KV.get(key) || '0', 10);
  if (cur >= RATE_LIMIT_PER_HOUR) return false;
  await env.MOD_KV.put(key, String(cur + 1), { expirationTtl: 3600 });
  return true;
}

function uuid() {
  return crypto.randomUUID();
}

function b64encode(str) {
  // UTF-8 safe base64
  const bytes = new TextEncoder().encode(str);
  let bin = '';
  for (const b of bytes) bin += String.fromCharCode(b);
  return btoa(bin);
}

function b64decode(str) {
  const bin = atob(str.replace(/\s/g, ''));
  const bytes = new Uint8Array(bin.length);
  for (let i = 0; i < bin.length; i++) bytes[i] = bin.charCodeAt(i);
  return new TextDecoder().decode(bytes);
}

// ---------- GitHub ----------

async function ghGetTemoignages(env) {
  const url = `https://api.github.com/repos/${env.GITHUB_REPO}/contents/${env.TEMOIGNAGES_PATH}?ref=${env.GITHUB_BRANCH}`;
  const resp = await fetch(url, {
    headers: {
      'Authorization': `Bearer ${env.GITHUB_TOKEN}`,
      'User-Agent': 'harmony-flux-worker',
      'Accept': 'application/vnd.github+json',
    },
  });
  if (!resp.ok) throw new Error(`GitHub GET failed: ${resp.status}`);
  const meta = await resp.json();
  const content = b64decode(meta.content);
  return { sha: meta.sha, list: JSON.parse(content) };
}

async function ghPutTemoignages(env, list, sha, message) {
  const url = `https://api.github.com/repos/${env.GITHUB_REPO}/contents/${env.TEMOIGNAGES_PATH}`;
  const body = {
    message,
    content: b64encode(JSON.stringify(list, null, 2) + '\n'),
    sha,
    branch: env.GITHUB_BRANCH,
  };
  const resp = await fetch(url, {
    method: 'PUT',
    headers: {
      'Authorization': `Bearer ${env.GITHUB_TOKEN}`,
      'User-Agent': 'harmony-flux-worker',
      'Accept': 'application/vnd.github+json',
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(body),
  });
  if (!resp.ok) {
    const txt = await resp.text();
    throw new Error(`GitHub PUT failed: ${resp.status} ${txt}`);
  }
  return resp.json();
}

// ---------- Handlers ----------

async function handleSubmit(request, env) {
  const ip = request.headers.get('CF-Connecting-IP') || 'unknown';

  if (!await checkRateLimit(ip, env)) {
    return json({ error: 'rate_limited', message: 'Trop de soumissions, réessayez plus tard.' }, 429, env);
  }

  let payload;
  try { payload = await request.json(); }
  catch { return json({ error: 'invalid_json' }, 400, env); }

  // Honeypot
  if (payload.website || payload.url || payload._gotcha) {
    return json({ ok: true }, 200, env); // silencieux
  }

  // Turnstile
  const tsOk = await verifyTurnstile(payload.turnstileToken, ip, env);
  if (!tsOk) return json({ error: 'turnstile_failed' }, 403, env);

  // Validation
  const prenom   = sanitize(payload.prenom, MAX_FIELD_LEN);
  const ville    = sanitize(payload.ville, MAX_FIELD_LEN);
  const soin     = sanitize(payload.soin, MAX_FIELD_LEN);
  const modalite = sanitize(payload.modalite, MAX_FIELD_LEN);
  const texte    = sanitize(payload.texte, MAX_TEXT_LEN);
  const note     = parseInt(payload.note, 10);

  if (!prenom || !texte || !Number.isInteger(note) || note < 1 || note > 5) {
    return json({ error: 'invalid_fields' }, 400, env);
  }

  const id = uuid();
  const entry = {
    id,
    prenom, ville, soin, modalite, texte, note,
    submitted_at: new Date().toISOString(),
    ip_hash: await sha256(ip + (env.ADMIN_TOKEN || '')),
  };

  await env.MOD_KV.put(`pending:${id}`, JSON.stringify(entry), {
    expirationTtl: PENDING_TTL_SECONDS,
  });

  return json({ ok: true, id }, 200, env);
}

async function sha256(str) {
  const buf = await crypto.subtle.digest('SHA-256', new TextEncoder().encode(str));
  return Array.from(new Uint8Array(buf)).map(b => b.toString(16).padStart(2, '0')).join('').slice(0, 16);
}

async function handlePending(request, env) {
  if (!isAdmin(request, env)) return json({ error: 'unauthorized' }, 401, env);
  const list = await env.MOD_KV.list({ prefix: 'pending:' });
  const items = [];
  for (const k of list.keys) {
    const v = await env.MOD_KV.get(k.name);
    if (v) items.push(JSON.parse(v));
  }
  items.sort((a, b) => (a.submitted_at < b.submitted_at ? 1 : -1));
  return json({ items }, 200, env);
}

async function handleApprove(request, env) {
  if (!isAdmin(request, env)) return json({ error: 'unauthorized' }, 401, env);
  let body;
  try { body = await request.json(); } catch { return json({ error: 'invalid_json' }, 400, env); }
  const id = sanitize(body.id, 64);
  if (!id) return json({ error: 'missing_id' }, 400, env);

  const raw = await env.MOD_KV.get(`pending:${id}`);
  if (!raw) return json({ error: 'not_found' }, 404, env);
  const entry = JSON.parse(raw);

  // Lecture + commit GitHub
  const { sha, list } = await ghGetTemoignages(env);
  const published = {
    prenom: entry.prenom,
    ville: entry.ville,
    note: entry.note,
    soin: entry.soin,
    modalite: entry.modalite,
    texte: entry.texte,
    date: entry.submitted_at.slice(0, 10),
  };
  list.push(published);
  await ghPutTemoignages(env, list, sha, `Approuve avis de ${entry.prenom}`);
  await env.MOD_KV.delete(`pending:${id}`);

  return json({ ok: true }, 200, env);
}

async function handleReject(request, env) {
  if (!isAdmin(request, env)) return json({ error: 'unauthorized' }, 401, env);
  let body;
  try { body = await request.json(); } catch { return json({ error: 'invalid_json' }, 400, env); }
  const id = sanitize(body.id, 64);
  if (!id) return json({ error: 'missing_id' }, 400, env);
  await env.MOD_KV.delete(`pending:${id}`);
  return json({ ok: true }, 200, env);
}

// ---------- Router ----------

export default {
  async fetch(request, env) {
    const url = new URL(request.url);

    if (request.method === 'OPTIONS') {
      return new Response(null, { status: 204, headers: corsHeaders(env) });
    }

    try {
      if (url.pathname === '/health') {
        return json({ ok: true, ts: Date.now() }, 200, env);
      }
      if (url.pathname === '/submit' && request.method === 'POST') {
        return await handleSubmit(request, env);
      }
      if (url.pathname === '/pending' && request.method === 'GET') {
        return await handlePending(request, env);
      }
      if (url.pathname === '/approve' && request.method === 'POST') {
        return await handleApprove(request, env);
      }
      if (url.pathname === '/reject' && request.method === 'POST') {
        return await handleReject(request, env);
      }
      return json({ error: 'not_found' }, 404, env);
    } catch (err) {
      return json({ error: 'internal', message: err.message }, 500, env);
    }
  },
};
