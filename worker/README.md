# Harmony-Flux — Moderation Worker

Cloudflare Worker qui sert de backend de modération pour les avis visiteurs.

## Architecture

```
index.html  ──POST /submit──►  Worker  ──KV pending:*──►  (file d'attente)
admin.html  ──GET  /pending──► Worker  ──liste KV
admin.html  ──POST /approve──► Worker  ──PUT GitHub──►  temoignages.json (commit)
admin.html  ──POST /reject──►  Worker  ──delete KV
```

## Prérequis

- Compte Cloudflare gratuit
- Node.js ≥ 18
- Wrangler CLI : `npm install -g wrangler`
- Connexion : `wrangler login`

## Déploiement (10 minutes)

### 1. Créer le namespace KV

```bash
cd worker
npm install
wrangler kv:namespace create MOD_KV
```

Copier l'`id` retourné dans `wrangler.toml` (champ `id` du `[[kv_namespaces]]`).

### 2. Générer un fine-grained Personal Access Token GitHub

1. https://github.com/settings/personal-access-tokens/new
2. Repository access : **Only select repositories** → `phm045/harmony-flux`
3. Permissions → Repository permissions → **Contents : Read and write**
4. Expiration : 90 jours (à renouveler)
5. Copier le token (commence par `github_pat_...`)

### 3. Générer un ADMIN_TOKEN

```bash
node -e "console.log(require('crypto').randomBytes(32).toString('hex'))"
```

Garder ce token : il sera saisi 1 fois dans `admin.html`.

### 4. (Optionnel mais recommandé) Cloudflare Turnstile

1. https://dash.cloudflare.com → Turnstile → Add site
2. Mode : **Managed**, domaines : `phm045.github.io` (+ domaine custom)
3. Récupérer **Site Key** (publique, à mettre dans `index.html`) et **Secret Key**

### 5. Configurer les secrets

```bash
wrangler secret put GITHUB_TOKEN
# coller le PAT GitHub
wrangler secret put ADMIN_TOKEN
# coller le token aléatoire généré à l'étape 3
wrangler secret put TURNSTILE_SECRET
# coller le Secret Key Turnstile (ou laisser vide si non utilisé)
```

### 6. Déployer

```bash
wrangler deploy
```

L'URL retournée ressemble à :
`https://harmony-flux-moderation.<sous-domaine>.workers.dev`

### 7. Mettre à jour les fronts

- `index.html` : remplacer `WORKER_URL` (ligne ~1925) par l'URL du Worker
- `index.html` : remplacer `TURNSTILE_SITE_KEY` par la Site Key publique
- `admin.html` : remplacer `WORKER_URL` (ligne ~2460) par l'URL du Worker

Au premier accès admin, saisir l'`ADMIN_TOKEN` quand demandé. Il est stocké en `localStorage`.

## Endpoints

| Méthode | Chemin     | Auth         | Description                          |
|---------|------------|--------------|--------------------------------------|
| GET     | /health    | —            | Sanity check                         |
| POST    | /submit    | Turnstile    | Reçoit un avis visiteur              |
| GET     | /pending   | ADMIN_TOKEN  | Liste des avis en attente            |
| POST    | /approve   | ADMIN_TOKEN  | Approuve et commit dans le repo      |
| POST    | /reject    | ADMIN_TOKEN  | Supprime un avis en attente          |

## Sécurité

- ✅ Rate-limit : 3 soumissions/heure/IP
- ✅ Honeypot anti-bot
- ✅ Turnstile (challenge invisible Cloudflare)
- ✅ Sanitization stricte (longueurs max, caractères de contrôle filtrés)
- ✅ ADMIN_TOKEN comparé en temps constant
- ✅ PAT GitHub jamais exposé côté client
- ✅ CORS restreint à `ALLOWED_ORIGIN`
- ✅ KV TTL 30 jours sur les `pending:*`

## Coûts

Plan gratuit Cloudflare :
- Workers : 100 000 requêtes/jour
- KV : 100 000 reads/jour, 1 000 writes/jour, 1 Go stockage

Largement suffisant pour un site cabinet de soins.

## Maintenance

- **Tail des logs** : `wrangler tail`
- **Renouveler le PAT GitHub** : tous les 90 jours, refaire `wrangler secret put GITHUB_TOKEN`
- **Rotation ADMIN_TOKEN** : `wrangler secret put ADMIN_TOKEN` puis ressaisir dans admin.html
