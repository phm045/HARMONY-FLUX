#!/usr/bin/env python3
"""
Build the fully i18n-translated version of index.html.
Strategy: read the file, apply targeted replacements for each text section,
then replace the script block wholesale.
"""

with open('/home/user/workspace/harmony-flux/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# ─────────────────────────────────────────────────────────────
# SECTION: HERO texts
# ─────────────────────────────────────────────────────────────

# hero_sub
html = html.replace(
    '<p class="hero-sub">Magnétisme &amp; Soins Énergétiques</p>',
    '<p class="hero-sub" data-i18n="hero_sub">Magnétisme &amp; Soins Énergétiques</p>'
)

# hero_desc
html = html.replace(
    '<p class="hero-desc">Séances courtes · efficaces · sur mesure</p>',
    '<p class="hero-desc" data-i18n="hero_desc">Séances courtes · efficaces · sur mesure</p>'
)

# badges
html = html.replace(
    '<span class="badge accent">10 à 15 minutes</span>',
    '<span class="badge accent" data-i18n="badge_min">10 à 15 minutes</span>'
)
html = html.replace(
    '<span class="badge">À domicile</span>',
    '<span class="badge" data-i18n="badge_home">À domicile</span>'
)
html = html.replace(
    '<span class="badge">À distance</span>',
    '<span class="badge" data-i18n="badge_remote">À distance</span>'
)
html = html.replace(
    '<span class="badge">20 min autour de St-Saturnin-lès-Avignon</span>',
    '<span class="badge" data-i18n="badge_radius">20 min autour de St-Saturnin-lès-Avignon</span>'
)

# hero_scroll
html = html.replace(
    '<div class="hero-scroll">Découvrir</div>',
    '<div class="hero-scroll" data-i18n="hero_scroll">Découvrir</div>'
)

# ─────────────────────────────────────────────────────────────
# SECTION: ABOUT (intro) — already partially done
# about_tag already has data-i18n="about_tag" ✓
# about_title already has data-i18n="about_title" ✓
# about_text1 already has data-i18n="about_text1" ✓
# about_text2 already has data-i18n="about_text2" ✓
# stat_min / stat_max / stat_radius already done ✓
# ─────────────────────────────────────────────────────────────

# ─────────────────────────────────────────────────────────────
# SECTION: ABOUT IMAGE — img_tag, img_title already done
# img_text already done, img_cta already done ✓
# ─────────────────────────────────────────────────────────────

# ─────────────────────────────────────────────────────────────
# SECTION: DUREE
# ─────────────────────────────────────────────────────────────
html = html.replace(
    '<p class="duree-label">Durée d\'une séance</p>',
    '<p class="duree-label" data-i18n="duree_label">Durée d\'une séance</p>'
)
html = html.replace(
    '<p class="duree-note">Des soins brefs, profonds et efficaces — sans rendez-vous long</p>',
    '<p class="duree-note" data-i18n="duree_note">Des soins brefs, profonds et efficaces — sans rendez-vous long</p>'
)

# ─────────────────────────────────────────────────────────────
# SECTION: SOINS (seances)
# ─────────────────────────────────────────────────────────────
html = html.replace(
    '<p class="intro-tag">Soins proposés</p>',
    '<p class="intro-tag" data-i18n="soins_tag">Soins proposés</p>'
)
html = html.replace(
    '<h2 class="intro-title">Ce que je<br>vous <em>offre</em></h2>',
    '<h2 class="intro-title" data-i18n="soins_title">Ce que je<br>vous <em>offre</em></h2>'
)

# Soin cards - titles, texts, pills
# Card 1: Traitement Magnétique Global
html = html.replace(
    '<h3 class="seance-title">Traitement Magnétique Global</h3>',
    '<h3 class="seance-title" data-i18n="s1_title">Traitement Magnétique Global</h3>'
)
html = html.replace(
    '<p class="seance-text">Rééquilibrage des flux vitaux de l\'ensemble du corps. En 10 à 15 minutes, une reconnexion profonde à votre énergie naturelle.</p>',
    '<p class="seance-text" data-i18n="s1_text">Rééquilibrage des flux vitaux de l\'ensemble du corps. En 10 à 15 minutes, une reconnexion profonde à votre énergie naturelle.</p>'
)
html = html.replace(
    '<span class="seance-pill">Présentiel · Distance</span>\n    </div>\n    <div class="seance-card',
    '<span class="seance-pill" data-i18n="s1_pill">Présentiel · Distance</span>\n    </div>\n    <div class="seance-card'
)

# Card 2: Soulagement des Douleurs
html = html.replace(
    '<h3 class="seance-title">Soulagement des Douleurs</h3>',
    '<h3 class="seance-title" data-i18n="s2_title">Soulagement des Douleurs</h3>'
)
html = html.replace(
    '<p class="seance-text">Intervention ciblée sur les zones douloureuses : articulations, migraines, tensions. Action rapide, résultats ressentis dès la première séance.</p>',
    '<p class="seance-text" data-i18n="s2_text">Intervention ciblée sur les zones douloureuses : articulations, migraines, tensions. Action rapide, résultats ressentis dès la première séance.</p>'
)
html = html.replace(
    '<span class="seance-pill">Présentiel</span>\n    </div>\n    <div class="seance-card',
    '<span class="seance-pill" data-i18n="s2_pill">Présentiel</span>\n    </div>\n    <div class="seance-card'
)

# Card 3: Stress & Anxiété
html = html.replace(
    '<h3 class="seance-title">Stress &amp; Anxiété</h3>',
    '<h3 class="seance-title" data-i18n="s3_title">Stress &amp; Anxiété</h3>'
)
html = html.replace(
    '<p class="seance-text">Apaisement du système nerveux énergétique. Quelques minutes suffisent pour retrouver calme, clarté et ancrage dans le présent.</p>',
    '<p class="seance-text" data-i18n="s3_text">Apaisement du système nerveux énergétique. Quelques minutes suffisent pour retrouver calme, clarté et ancrage dans le présent.</p>'
)
html = html.replace(
    '<span class="seance-pill">Présentiel · Distance</span>\n    </div>\n    <div class="seance-card reveal">\n    <div class="seance-num">04</div>',
    '<span class="seance-pill" data-i18n="s3_pill">Présentiel · Distance</span>\n    </div>\n    <div class="seance-card reveal">\n    <div class="seance-num">04</div>'
)

# Card 4: Blocages Émotionnels
html = html.replace(
    '<h3 class="seance-title">Blocages Émotionnels</h3>',
    '<h3 class="seance-title" data-i18n="s4_title">Blocages Émotionnels</h3>'
)
html = html.replace(
    '<p class="seance-text">Libération des tensions émotionnelles profondes. Idéal lors de transitions, deuils ou périodes d\'instabilité intérieure.</p>',
    '<p class="seance-text" data-i18n="s4_text">Libération des tensions émotionnelles profondes. Idéal lors de transitions, deuils ou périodes d\'instabilité intérieure.</p>'
)
html = html.replace(
    '<span class="seance-pill">Présentiel · Distance</span>\n    </div>\n    <div class="seance-card reveal">\n    <div class="seance-num">05</div>',
    '<span class="seance-pill" data-i18n="s4_pill">Présentiel · Distance</span>\n    </div>\n    <div class="seance-card reveal">\n    <div class="seance-num">05</div>'
)

# Card 5: Soin Enfant
html = html.replace(
    '<h3 class="seance-title">Soin Enfant</h3>',
    '<h3 class="seance-title" data-i18n="s5_title">Soin Enfant</h3>'
)
html = html.replace(
    '<p class="seance-text">Approche douce pour les plus jeunes : sommeil, concentration, anxiété scolaire. Séance adaptée à leur sensibilité particulière.</p>',
    '<p class="seance-text" data-i18n="s5_text">Approche douce pour les plus jeunes : sommeil, concentration, anxiété scolaire. Séance adaptée à leur sensibilité particulière.</p>'
)
html = html.replace(
    '<span class="seance-pill">Présentiel · Domicile</span>',
    '<span class="seance-pill" data-i18n="s5_pill">Présentiel · Domicile</span>'
)

# Card 6: Suivi Personnalisé
html = html.replace(
    '<h3 class="seance-title">Suivi Personnalisé</h3>',
    '<h3 class="seance-title" data-i18n="s6_title">Suivi Personnalisé</h3>'
)
html = html.replace(
    '<p class="seance-text">Plusieurs séances rapprochées pour un travail en profondeur. Le format court se prête à un suivi régulier, intégré au quotidien.</p>',
    '<p class="seance-text" data-i18n="s6_text">Plusieurs séances rapprochées pour un travail en profondeur. Le format court se prête à un suivi régulier, intégré au quotidien.</p>'
)
html = html.replace(
    '<span class="seance-pill">Sur mesure</span>',
    '<span class="seance-pill" data-i18n="s6_pill">Sur mesure</span>'
)

# ─────────────────────────────────────────────────────────────
# SECTION: MODALITES
# ─────────────────────────────────────────────────────────────
html = html.replace(
    '<p class="mod-tag">Modalité 01</p>',
    '<p class="mod-tag" data-i18n="mod1_tag">Modalité 01</p>'
)
html = html.replace(
    '<h2 class="mod-title">À domicile<br><em>chez vous</em></h2>',
    '<h2 class="mod-title" data-i18n="mod1_title">À domicile<br><em>chez vous</em></h2>'
)
html = html.replace(
    '<p class="mod-text">Je me déplace directement à votre domicile dans les départements 84, 13 et 30. Vous restez dans votre environnement, sans effort de déplacement.</p>',
    '<p class="mod-text" data-i18n="mod1_text">Je me déplace directement à votre domicile dans les départements 84, 13 et 30. Vous restez dans votre environnement, sans effort de déplacement.</p>'
)

# mod1 list items
html = html.replace(
    '      <li>Déplacement inclus dans 3 dpts</li>\n      <li>Séance de 10 à 15 minutes</li>\n      <li>Aucun matériel nécessaire</li>\n      <li>Horaires flexibles</li>',
    '      <li data-i18n="mod1_li1">Déplacement inclus dans 3 dpts</li>\n      <li data-i18n="mod1_li2">Séance de 10 à 15 minutes</li>\n      <li data-i18n="mod1_li3">Aucun matériel nécessaire</li>\n      <li data-i18n="mod1_li4">Horaires flexibles</li>'
)

html = html.replace(
    '<p class="mod-tag">Modalité 02</p>',
    '<p class="mod-tag" data-i18n="mod2_tag">Modalité 02</p>'
)
html = html.replace(
    '<h2 class="mod-title">À distance<br><em>depuis chez vous</em></h2>',
    '<h2 class="mod-title" data-i18n="mod2_title">À distance<br><em>depuis chez vous</em></h2>'
)
html = html.replace(
    '<p class="mod-text">Le magnétisme à distance est aussi efficace qu\'en présence physique. Depuis n\'importe où en France, recevez un soin complet par téléphone ou visio.</p>',
    '<p class="mod-text" data-i18n="mod2_text">Le magnétisme à distance est aussi efficace qu\'en présence physique. Depuis n\'importe où en France, recevez un soin complet par téléphone ou visio.</p>'
)

# mod2 list items
html = html.replace(
    '      <li>Par téléphone ou visioconférence</li>\n      <li>Partout en France</li>\n      <li>10 à 15 minutes chrono</li>\n      <li>Idéal pour mobilité réduite</li>',
    '      <li data-i18n="mod2_li1">Par téléphone ou visioconférence</li>\n      <li data-i18n="mod2_li2">Partout en France</li>\n      <li data-i18n="mod2_li3">10 à 15 minutes chrono</li>\n      <li data-i18n="mod2_li4">Idéal pour mobilité réduite</li>'
)

# ─────────────────────────────────────────────────────────────
# SECTION: ZONES
# ─────────────────────────────────────────────────────────────
html = html.replace(
    '      <p class="intro-tag">Zone de déplacement</p>',
    '      <p class="intro-tag" data-i18n="zones_tag">Zone de déplacement</p>'
)
html = html.replace(
    '      <h2 class="intro-title">Je viens<br>jusqu\'à <em>vous</em></h2>',
    '      <h2 class="intro-title" data-i18n="zones_title">Je viens<br>jusqu\'à <em>vous</em></h2>'
)
html = html.replace(
    '      <p class="intro-text" style="margin-top:1rem;">Basé à <strong style="color:var(--gold2);font-weight:400;">Saint-Saturnin-lès-Avignon (84450)</strong>, je me déplace à domicile dans un rayon de <strong style="color:var(--gold2);font-weight:400;">20 minutes</strong> autour de chez moi. Pour tout le reste, la séance à distance est tout aussi efficace.</p>',
    '      <p class="intro-text" data-i18n="zones_desc" style="margin-top:1rem;">Basé à <strong style="color:var(--gold2);font-weight:400;">Saint-Saturnin-lès-Avignon (84450)</strong>, je me déplace à domicile dans un rayon de <strong style="color:var(--gold2);font-weight:400;">20 minutes</strong> autour de chez moi. Pour tout le reste, la séance à distance est tout aussi efficace.</p>'
)

# dept cards codes and names
html = html.replace(
    '          <p class="dept-code">Vaucluse — Grand Avignon</p>\n          <h3 class="dept-name">Avignon &amp; Sorgues</h3>',
    '          <p class="dept-code" data-i18n="dept1_code">Vaucluse — Grand Avignon</p>\n          <h3 class="dept-name" data-i18n="dept1_name">Avignon &amp; Sorgues</h3>'
)
html = html.replace(
    '          <p class="dept-code">Vaucluse — Pays des Sorgues</p>\n          <h3 class="dept-name">Sorgues &amp; Luberon</h3>',
    '          <p class="dept-code" data-i18n="dept2_code">Vaucluse — Pays des Sorgues</p>\n          <h3 class="dept-name" data-i18n="dept2_name">Sorgues &amp; Luberon</h3>'
)
html = html.replace(
    '          <p class="dept-code">Gard &amp; Bouches-du-Rhône</p>\n          <h3 class="dept-name">Villeneuve &amp; alentours</h3>',
    '          <p class="dept-code" data-i18n="dept3_code">Gard &amp; Bouches-du-Rhône</p>\n          <h3 class="dept-name" data-i18n="dept3_name">Villeneuve &amp; alentours</h3>'
)

# distance card
html = html.replace(
    '          <p class="dist-text"><strong>Hors zone ou toute la France — séance à distance.</strong> Au-delà de 20 minutes de Saint-Saturnin-lès-Avignon, je vous reçois par téléphone ou visio pour un soin complet de 10 à 15 minutes, aussi efficace qu\'en présentiel.</p>',
    '          <p class="dist-text" data-i18n="dist_text"><strong data-i18n="dist_strong">Hors zone ou toute la France — séance à distance.</strong> Au-delà de 20 minutes de Saint-Saturnin-lès-Avignon, je vous reçois par téléphone ou visio pour un soin complet de 10 à 15 minutes, aussi efficace qu\'en présentiel.</p>'
)

# ─────────────────────────────────────────────────────────────
# SECTION: TARIFS
# ─────────────────────────────────────────────────────────────
html = html.replace(
    '    <p class="intro-tag">Tarifs</p>',
    '    <p class="intro-tag" data-i18n="tarifs_tag">Tarifs</p>'
)
html = html.replace(
    '    <h2 class="intro-title">Simple &amp; <em>transparent</em></h2>',
    '    <h2 class="intro-title" data-i18n="tarifs_title">Simple &amp; <em>transparent</em></h2>'
)

# Tarif 1
html = html.replace(
    '      <p class="tarif-lbl">Séance à distance</p>',
    '      <p class="tarif-lbl" data-i18n="t1_lbl">Séance à distance</p>'
)
html = html.replace(
    '      <p class="tarif-u">10 à 15 min · visio ou tél</p>',
    '      <p class="tarif-u" data-i18n="t1_u">10 à 15 min · visio ou tél</p>'
)
html = html.replace(
    '        <li>Toute la France</li>\n        <li>Bilan énergétique inclus</li>\n        <li>Retour après séance</li>',
    '        <li data-i18n="t1_f1">Toute la France</li>\n        <li data-i18n="t1_f2">Bilan énergétique inclus</li>\n        <li data-i18n="t1_f3">Retour après séance</li>'
)

# Tarif 2
html = html.replace(
    '      <p class="tarif-lbl">Séance à domicile</p>',
    '      <p class="tarif-lbl" data-i18n="t2_lbl">Séance à domicile</p>'
)
html = html.replace(
    '      <p class="tarif-u">10 à 15 min · rayon 20 min de St-Saturnin</p>',
    '      <p class="tarif-u" data-i18n="t2_u">10 à 15 min · rayon 20 min de St-Saturnin</p>'
)
html = html.replace(
    '        <li>Déplacement inclus</li>\n        <li>Soin à votre domicile</li>\n        <li>Bilan &amp; conseils</li>',
    '        <li data-i18n="t2_f1">Déplacement inclus</li>\n        <li data-i18n="t2_f2">Soin à votre domicile</li>\n        <li data-i18n="t2_f3">Bilan &amp; conseils</li>'
)

# Tarif 3
html = html.replace(
    '      <p class="tarif-lbl">Forfait 5 séances</p>',
    '      <p class="tarif-lbl" data-i18n="t3_lbl">Forfait 5 séances</p>'
)
html = html.replace(
    '      <p class="tarif-u">soit 36€/séance · −10%</p>',
    '      <p class="tarif-u" data-i18n="t3_u">soit 36€/séance · −10%</p>'
)
html = html.replace(
    '        <li>Présentiel ou distance</li>\n        <li>Suivi personnalisé</li>\n        <li>Valable 3 mois</li>',
    '        <li data-i18n="t3_f1">Présentiel ou distance</li>\n        <li data-i18n="t3_f2">Suivi personnalisé</li>\n        <li data-i18n="t3_f3">Valable 3 mois</li>'
)

# tarif buttons (all 3)
html = html.replace(
    'data-cal-config=\'{"layout":"month_view","theme":"dark"}\' class="tarif-btn">Réserver</button>',
    'data-cal-config=\'{"layout":"month_view","theme":"dark"}\' class="tarif-btn" data-i18n="btn_reserver">Réserver</button>',
    3  # replace all 3 instances
)

# ─────────────────────────────────────────────────────────────
# SECTION: CONTACT
# ─────────────────────────────────────────────────────────────
html = html.replace(
    '    <p class="intro-tag">Contact</p>',
    '    <p class="intro-tag" data-i18n="contact_tag">Contact</p>'
)
html = html.replace(
    '    <h2 class="intro-title">Prenez <em>rendez-vous</em></h2>',
    '    <h2 class="intro-title" data-i18n="contact_title">Prenez <em>rendez-vous</em></h2>'
)
html = html.replace(
    '    <p class="intro-text" style="margin-top:1rem;">Disponible du lundi au samedi, de 9h à 19h. Réponse rapide garantie.</p>',
    '    <p class="intro-text" data-i18n="contact_sub" style="margin-top:1rem;">Disponible du lundi au samedi, de 9h à 19h. Réponse rapide garantie.</p>'
)

# contact address line
html = html.replace(
    '      <li><span class="ico">◉</span><span>Rayon 20 min autour de Saint-Saturnin-lès-Avignon (84450)<br>Avignon · Le Pontet · Vedène · Le Thor · L\'Isle-sur-la-Sorgue…<br>+ distance : toute la France</span></li>',
    '      <li><span class="ico">◉</span><span data-i18n="contact_addr">Rayon 20 min autour de Saint-Saturnin-lès-Avignon (84450)<br>Avignon · Le Pontet · Vedène · Le Thor · L\'Isle-sur-la-Sorgue…<br>+ distance : toute la France</span></li>'
)

# contact hours
html = html.replace(
    '      <li><span class="ico">◷</span><span>Lundi – Samedi · 9h–19h</span></li>',
    '      <li><span class="ico">◷</span><span data-i18n="contact_hours">Lundi – Samedi · 9h–19h</span></li>'
)

# ─────────────────────────────────────────────────────────────
# SECTION: WHATSAPP
# ─────────────────────────────────────────────────────────────
html = html.replace(
    '    <p class="intro-tag">WhatsApp</p>',
    '    <p class="intro-tag" data-i18n="wa_tag">WhatsApp</p>'
)
html = html.replace(
    '    <h3 class="contact-wa-title">Contactez-moi<br><em>directement</em></h3>',
    '    <h3 class="contact-wa-title" data-i18n="wa_title">Contactez-moi<br><em>directement</em></h3>'
)
html = html.replace(
    '    <p class="contact-wa-sub">La façon la plus rapide de me joindre. Je réponds généralement en quelques minutes, du lundi au samedi de 9h à 19h.</p>',
    '    <p class="contact-wa-sub" data-i18n="wa_sub">La façon la plus rapide de me joindre. Je réponds généralement en quelques minutes, du lundi au samedi de 9h à 19h.</p>'
)

# WhatsApp message button - add id and data-i18n to the text span and update href handling
# We need to update the wa-msg href per language and add data-i18n to the text
html = html.replace(
    '    <a href="https://wa.me/33788301574?text=Bonjour%2C%20je%20souhaite%20prendre%20rendez-vous%20pour%20une%20s%C3%A9ance%20de%20magn%C3%A9tisme." target="_blank" rel="noopener noreferrer" class="wa-btn">',
    '    <a id="wa-msg-btn" href="https://wa.me/33788301574?text=Bonjour%2C%20je%20souhaite%20prendre%20rendez-vous%20pour%20une%20s%C3%A9ance%20de%20magn%C3%A9tisme." target="_blank" rel="noopener noreferrer" class="wa-btn">'
)

# wa-btn-label (WhatsApp tag in send button)
html = html.replace(
    '        <span class="wa-btn-label">WhatsApp</span>\n        <span class="wa-btn-text">Envoyer un message</span>',
    '        <span class="wa-btn-label" data-i18n="wa_tag">WhatsApp</span>\n        <span class="wa-btn-text" data-i18n="wa_msg">Envoyer un message</span>'
)

# wa call button - add id
html = html.replace(
    '    <a href="https://wa.me/33788301574" target="_blank" rel="noopener noreferrer" class="wa-btn">',
    '    <a id="wa-call-btn" href="https://wa.me/33788301574" target="_blank" rel="noopener noreferrer" class="wa-btn">'
)

# wa call button text
html = html.replace(
    '        <span class="wa-btn-label">WhatsApp</span>\n        <span class="wa-btn-text">Appeler via WhatsApp</span>',
    '        <span class="wa-btn-label" data-i18n="wa_tag">WhatsApp</span>\n        <span class="wa-btn-text" data-i18n="wa_call">Appeler via WhatsApp</span>'
)

# wa-note
html = html.replace(
    '    <p class="wa-note">Ou réservez directement en ligne via <button type="button" data-cal-link="ferreira-tony-niw1yi/secret" data-cal-namespace="harmony" data-cal-config=\'{"layout":"month_view","theme":"dark"}\' style="background:none;border:none;color:var(--gold2);font-size:0.7rem;cursor:pointer;padding:0;font-family:inherit;">le calendrier de réservation →</button></p>',
    '    <p class="wa-note"><span data-i18n="wa_note_pre">Ou réservez directement en ligne via</span> <button type="button" data-cal-link="ferreira-tony-niw1yi/secret" data-cal-namespace="harmony" data-cal-config=\'{"layout":"month_view","theme":"dark"}\' style="background:none;border:none;color:var(--gold2);font-size:0.7rem;cursor:pointer;padding:0;font-family:inherit;" data-i18n="wa_cal_btn">le calendrier de réservation →</button></p>'
)

# ─────────────────────────────────────────────────────────────
# SECTION: FOOTER
# ─────────────────────────────────────────────────────────────
html = html.replace(
    '  <span class="ft-copy">© 2025 Harmony Flux — Magnétisme</span>',
    '  <span class="ft-copy" data-i18n="footer_copy">© 2025 Harmony Flux — Magnétisme</span>'
)
html = html.replace(
    '    <a href="#">Mentions légales</a>\n    <a href="#">Confidentialité</a>',
    '    <a href="#" data-i18n="footer_legal">Mentions légales</a>\n    <a href="#" data-i18n="footer_privacy">Confidentialité</a>'
)

# ─────────────────────────────────────────────────────────────
# NOW REPLACE THE ENTIRE i18n script block
# ─────────────────────────────────────────────────────────────

old_script = '''<!-- i18n Traductions -->
<script>
const translations = {
  fr: {
    nav_about: 'À propos', nav_soins: 'Soins', nav_zones: 'Zones', nav_tarifs: 'Tarifs',
    hero_sub: 'Magnétisme &amp; Soins Énergétiques',
    hero_desc: 'Séances courtes · efficaces · sur mesure',
    about_tag: 'À propos',
    about_title: 'Une pratique<br>ancrée dans <em>l'essentiel</em>',
    about_text1: 'Le magnétisme agit sur les flux énergétiques qui traversent le corps. En quelques minutes seulement, un soin ciblé peut rétablir l'équilibre, soulager la douleur ou apaiser les tensions accumulées.',
    about_text2: 'Mes séances, volontairement courtes et intenses, sont pensées pour s'intégrer dans votre quotidien — sans vous demander du temps que vous n'avez pas.',
    stat_min: 'Durée minimale', stat_max: 'Durée maximale', stat_radius: 'Rayon domicile',
    img_tag: 'Soin &amp; Énergie', img_title: 'Ressentir<br>pour <em>guérir</em>',
    img_text: 'Le magnétiseur canalise et redistribue les énergies vitales avec les mains, sans contact ou à distance. Une approche douce, rapide et profonde pour retrouver votre équilibre intérieur.',
    img_cta: 'Réserver une séance →',
    contact_title: 'Prenez <em>rendez-vous</em>',
    contact_sub: 'Disponible du lundi au samedi, de 9h à 19h. Réponse rapide garantie.',
    wa_title: 'Contactez-moi<br><em>directement</em>',
    wa_sub: 'La façon la plus rapide de me joindre. Je réponds généralement en quelques minutes, du lundi au samedi de 9h à 19h.',
    wa_msg: 'Envoyer un message', wa_call: 'Appeler via WhatsApp',
  },
  en: {
    nav_about: 'About', nav_soins: 'Treatments', nav_zones: 'Areas', nav_tarifs: 'Pricing',
    hero_sub: 'Magnetism &amp; Energy Healing',
    hero_desc: 'Short sessions · effective · tailored',
    about_tag: 'About',
    about_title: 'A practice<br>rooted in <em>the essential</em>',
    about_text1: 'Magnetism acts on the energetic flows that run through the body. In just a few minutes, a targeted session can restore balance, relieve pain or calm accumulated tensions.',
    about_text2: 'My sessions, intentionally short and intense, are designed to fit into your daily life — without asking for time you don't have.',
    stat_min: 'Minimum duration', stat_max: 'Maximum duration', stat_radius: 'Home radius',
    img_tag: 'Care &amp; Energy', img_title: 'Feel<br>to <em>heal</em>',
    img_text: 'The magnetizer channels and redistributes vital energies through their hands, with or without contact, or remotely. A gentle, fast and deep approach to restoring your inner balance.',
    img_cta: 'Book a session →',
    contact_title: 'Book an <em>appointment</em>',
    contact_sub: 'Available Monday to Saturday, 9am to 7pm. Fast reply guaranteed.',
    wa_title: 'Contact me<br><em>directly</em>',
    wa_sub: 'The fastest way to reach me. I usually reply within minutes, Monday to Saturday, 9am to 7pm.',
    wa_msg: 'Send a message', wa_call: 'Call via WhatsApp',
  },
  pt: {
    nav_about: 'Sobre', nav_soins: 'Tratamentos', nav_zones: 'Áreas', nav_tarifs: 'Preços',
    hero_sub: 'Magnetismo &amp; Cuidados Energéticos',
    hero_desc: 'Sessões curtas · eficazes · personalizadas',
    about_tag: 'Sobre',
    about_title: 'Uma prática<br>enraizada no <em>essencial</em>',
    about_text1: 'O magnetismo atua sobre os fluxos energéticos que percorrem o corpo. Em apenas alguns minutos, um tratamento dirigido pode restaurar o equilíbrio, aliviar a dor ou acalmar as tensões acumuladas.',
    about_text2: 'As minhas sessões, intencionalmente curtas e intensas, foram pensadas para se integrar no seu quotidiano — sem lhe pedir tempo que não tem.',
    stat_min: 'Duração mínima', stat_max: 'Duração máxima', stat_radius: 'Raio domicilio',
    img_tag: 'Cuidado &amp; Energia', img_title: 'Sentir<br>para <em>curar</em>',
    img_text: 'O magnetizador canaliza e redistribui as energias vitais com as mãos, sem contacto ou à distância. Uma abordagem suave, rápida e profunda para recuperar o seu equilíbrio interior.',
    img_cta: 'Reservar uma sessão →',
    contact_title: 'Marque uma <em>consulta</em>',
    contact_sub: 'Disponível de segunda a sábado, das 9h às 19h. Resposta rápida garantida.',
    wa_title: 'Contacte-me<br><em>diretamente</em>',
    wa_sub: 'A forma mais rápida de me contactar. Respondo geralmente em poucos minutos, de segunda a sábado das 9h às 19h.',
    wa_msg: 'Enviar mensagem', wa_call: 'Ligar via WhatsApp',
  }
};

function setLang(lang) {
  document.querySelectorAll('.lang-btn').forEach(btn => btn.classList.remove('active'));
  document.querySelectorAll('.lang-btn').forEach(btn => {
    if (btn.textContent.trim().toLowerCase() === lang) btn.classList.add('active');
  });
  const t = translations[lang];
  document.querySelectorAll('[data-i18n]').forEach(el => {
    const key = el.getAttribute('data-i18n');
    if (t[key] !== undefined) el.innerHTML = t[key];
  });
  document.documentElement.lang = lang;
}
</script>'''

new_script = '''<!-- i18n Traductions -->
<script>
const translations = {
  fr: {
    nav_about: '\u00c0 propos', nav_soins: 'Soins', nav_zones: 'Zones', nav_tarifs: 'Tarifs',
    hero_sub: 'Magn\u00e9tisme &amp; Soins \u00c9nerg\u00e9tiques',
    hero_desc: 'S\u00e9ances courtes \u00b7 efficaces \u00b7 sur mesure',
    badge_min: '10 \u00e0 15 minutes',
    badge_home: '\u00c0 domicile',
    badge_remote: '\u00c0 distance',
    badge_radius: '20 min autour de St-Saturnin-l\u00e8s-Avignon',
    hero_scroll: 'D\u00e9couvrir',
    about_tag: '\u00c0 propos',
    about_title: 'Une pratique<br>ancr\u00e9e dans <em>l\u2019essentiel</em>',
    about_text1: 'Le magn\u00e9tisme agit sur les flux \u00e9nerg\u00e9tiques qui traversent le corps. En quelques minutes seulement, un soin cibl\u00e9 peut r\u00e9tablir l\u2019\u00e9quilibre, soulager la douleur ou apaiser les tensions accumul\u00e9es.',
    about_text2: 'Mes s\u00e9ances, volontairement courtes et intenses, sont pens\u00e9es pour s\u2019int\u00e9grer dans votre quotidien \u2014 sans vous demander du temps que vous n\u2019avez pas.',
    stat_min: 'Dur\u00e9e minimale', stat_max: 'Dur\u00e9e maximale', stat_radius: 'Rayon domicile',
    img_tag: 'Soin &amp; \u00c9nergie',
    img_title: 'Ressentir<br>pour <em>gu\u00e9rir</em>',
    img_text: 'Le magn\u00e9tiseur canalise et redistribue les \u00e9nergies vitales avec les mains, sans contact ou \u00e0 distance. Une approche douce, rapide et profonde pour retrouver votre \u00e9quilibre int\u00e9rieur.',
    img_cta: 'R\u00e9server une s\u00e9ance \u2192',
    duree_label: 'Dur\u00e9e d\u2019une s\u00e9ance',
    duree_note: 'Des soins brefs, profonds et efficaces \u2014 sans rendez-vous long',
    soins_tag: 'Soins propos\u00e9s',
    soins_title: 'Ce que je<br>vous <em>offre</em>',
    s1_title: 'Traitement Magn\u00e9tique Global',
    s1_text: 'R\u00e9\u00e9quilibrage des flux vitaux de l\u2019ensemble du corps. En 10 \u00e0 15 minutes, une reconnexion profonde \u00e0 votre \u00e9nergie naturelle.',
    s1_pill: 'Pr\u00e9sentiel \u00b7 Distance',
    s2_title: 'Soulagement des Douleurs',
    s2_text: 'Intervention cibl\u00e9e sur les zones douloureuses\u00a0: articulations, migraines, tensions. Action rapide, r\u00e9sultats ressentis d\u00e8s la premi\u00e8re s\u00e9ance.',
    s2_pill: 'Pr\u00e9sentiel',
    s3_title: 'Stress &amp; Anxi\u00e9t\u00e9',
    s3_text: 'Apaisement du syst\u00e8me nerveux \u00e9nerg\u00e9tique. Quelques minutes suffisent pour retrouver calme, clart\u00e9 et ancrage dans le pr\u00e9sent.',
    s3_pill: 'Pr\u00e9sentiel \u00b7 Distance',
    s4_title: 'Blocages \u00c9motionnels',
    s4_text: 'Lib\u00e9ration des tensions \u00e9motionnelles profondes. Id\u00e9al lors de transitions, deuils ou p\u00e9riodes d\u2019instabilit\u00e9 int\u00e9rieure.',
    s4_pill: 'Pr\u00e9sentiel \u00b7 Distance',
    s5_title: 'Soin Enfant',
    s5_text: 'Approche douce pour les plus jeunes\u00a0: sommeil, concentration, anxi\u00e9t\u00e9 scolaire. S\u00e9ance adapt\u00e9e \u00e0 leur sensibilit\u00e9 particuli\u00e8re.',
    s5_pill: 'Pr\u00e9sentiel \u00b7 Domicile',
    s6_title: 'Suivi Personnalis\u00e9',
    s6_text: 'Plusieurs s\u00e9ances rapproch\u00e9es pour un travail en profondeur. Le format court se pr\u00eate \u00e0 un suivi r\u00e9gulier, int\u00e9gr\u00e9 au quotidien.',
    s6_pill: 'Sur mesure',
    mod1_tag: 'Modalit\u00e9 01',
    mod1_title: '\u00c0 domicile<br><em>chez vous</em>',
    mod1_text: 'Je me d\u00e9place directement \u00e0 votre domicile dans les d\u00e9partements 84, 13 et 30. Vous restez dans votre environnement, sans effort de d\u00e9placement.',
    mod1_li1: 'D\u00e9placement inclus dans 3 dpts',
    mod1_li2: 'S\u00e9ance de 10 \u00e0 15 minutes',
    mod1_li3: 'Aucun mat\u00e9riel n\u00e9cessaire',
    mod1_li4: 'Horaires flexibles',
    mod2_tag: 'Modalit\u00e9 02',
    mod2_title: '\u00c0 distance<br><em>depuis chez vous</em>',
    mod2_text: 'Le magn\u00e9tisme \u00e0 distance est aussi efficace qu\u2019en pr\u00e9sence physique. Depuis n\u2019importe o\u00f9 en France, recevez un soin complet par t\u00e9l\u00e9phone ou visio.',
    mod2_li1: 'Par t\u00e9l\u00e9phone ou visioconf\u00e9rence',
    mod2_li2: 'Partout en France',
    mod2_li3: '10 \u00e0 15 minutes chrono',
    mod2_li4: 'Id\u00e9al pour mobilit\u00e9 r\u00e9duite',
    zones_tag: 'Zone de d\u00e9placement',
    zones_title: 'Je viens<br>jusqu\u2019\u00e0 <em>vous</em>',
    zones_desc: 'Bas\u00e9 \u00e0 <strong style="color:var(--gold2);font-weight:400;">Saint-Saturnin-l\u00e8s-Avignon (84450)</strong>, je me d\u00e9place \u00e0 domicile dans un rayon de <strong style="color:var(--gold2);font-weight:400;">20 minutes</strong> autour de chez moi. Pour tout le reste, la s\u00e9ance \u00e0 distance est tout aussi efficace.',
    dept1_code: 'Vaucluse \u2014 Grand Avignon',
    dept1_name: 'Avignon &amp; Sorgues',
    dept2_code: 'Vaucluse \u2014 Pays des Sorgues',
    dept2_name: 'Sorgues &amp; Luberon',
    dept3_code: 'Gard &amp; Bouches-du-Rh\u00f4ne',
    dept3_name: 'Villeneuve &amp; alentours',
    dist_strong: 'Hors zone ou toute la France \u2014 s\u00e9ance \u00e0 distance.',
    dist_text: '<strong data-i18n="dist_strong">Hors zone ou toute la France \u2014 s\u00e9ance \u00e0 distance.</strong> Au-del\u00e0 de 20 minutes de Saint-Saturnin-l\u00e8s-Avignon, je vous re\u00e7ois par t\u00e9l\u00e9phone ou visio pour un soin complet de 10 \u00e0 15 minutes, aussi efficace qu\u2019en pr\u00e9sentiel.',
    tarifs_tag: 'Tarifs',
    tarifs_title: 'Simple &amp; <em>transparent</em>',
    t1_lbl: 'S\u00e9ance \u00e0 distance',
    t1_u: '10 \u00e0 15 min \u00b7 visio ou t\u00e9l',
    t1_f1: 'Toute la France',
    t1_f2: 'Bilan \u00e9nerg\u00e9tique inclus',
    t1_f3: 'Retour apr\u00e8s s\u00e9ance',
    t2_lbl: 'S\u00e9ance \u00e0 domicile',
    t2_u: '10 \u00e0 15 min \u00b7 rayon 20 min de St-Saturnin',
    t2_f1: 'D\u00e9placement inclus',
    t2_f2: 'Soin \u00e0 votre domicile',
    t2_f3: 'Bilan &amp; conseils',
    t3_lbl: 'Forfait 5 s\u00e9ances',
    t3_u: 'soit 36\u20ac/s\u00e9ance \u00b7 \u221210%',
    t3_f1: 'Pr\u00e9sentiel ou distance',
    t3_f2: 'Suivi personnalis\u00e9',
    t3_f3: 'Valable 3 mois',
    btn_reserver: 'R\u00e9server',
    contact_tag: 'Contact',
    contact_title: 'Prenez <em>rendez-vous</em>',
    contact_sub: 'Disponible du lundi au samedi, de 9h \u00e0 19h. R\u00e9ponse rapide garantie.',
    contact_addr: 'Rayon 20 min autour de Saint-Saturnin-l\u00e8s-Avignon (84450)<br>Avignon \u00b7 Le Pontet \u00b7 Ved\u00e8ne \u00b7 Le Thor \u00b7 L\u2019Isle-sur-la-Sorgue\u2026<br>+ distance\u00a0: toute la France',
    contact_hours: 'Lundi \u2013 Samedi \u00b7 9h\u201319h',
    wa_tag: 'WhatsApp',
    wa_title: 'Contactez-moi<br><em>directement</em>',
    wa_sub: 'La fa\u00e7on la plus rapide de me joindre. Je r\u00e9ponds g\u00e9n\u00e9ralement en quelques minutes, du lundi au samedi de 9h \u00e0 19h.',
    wa_msg: 'Envoyer un message',
    wa_call: 'Appeler via WhatsApp',
    wa_note_pre: 'Ou r\u00e9servez directement en ligne via',
    wa_cal_btn: 'le calendrier de r\u00e9servation \u2192',
    footer_copy: '\u00a9 2025 Harmony Flux \u2014 Magn\u00e9tisme',
    footer_legal: 'Mentions l\u00e9gales',
    footer_privacy: 'Confidentialit\u00e9',
    wa_href_msg: 'https://wa.me/33788301574?text=Bonjour%2C%20je%20souhaite%20prendre%20rendez-vous%20pour%20une%20s%C3%A9ance%20de%20magn%C3%A9tisme.',
    wa_href_call: 'https://wa.me/33788301574',
  },
  en: {
    nav_about: 'About', nav_soins: 'Treatments', nav_zones: 'Areas', nav_tarifs: 'Pricing',
    hero_sub: 'Magnetism &amp; Energy Healing',
    hero_desc: 'Short sessions \u00b7 effective \u00b7 tailored',
    badge_min: '10 to 15 minutes',
    badge_home: 'Home visit',
    badge_remote: 'Remote',
    badge_radius: '20 min around St-Saturnin-l\u00e8s-Avignon',
    hero_scroll: 'Discover',
    about_tag: 'About',
    about_title: 'A practice<br>rooted in <em>the essential</em>',
    about_text1: 'Magnetism acts on the energetic flows that run through the body. In just a few minutes, a targeted session can restore balance, relieve pain or calm accumulated tensions.',
    about_text2: 'My sessions, intentionally short and intense, are designed to fit into your daily life \u2014 without asking for time you don\u2019t have.',
    stat_min: 'Minimum duration', stat_max: 'Maximum duration', stat_radius: 'Home radius',
    img_tag: 'Care &amp; Energy',
    img_title: 'Feel<br>to <em>heal</em>',
    img_text: 'The magnetizer channels and redistributes vital energies through their hands, with or without contact, or remotely. A gentle, fast and deep approach to restoring your inner balance.',
    img_cta: 'Book a session \u2192',
    duree_label: 'Session duration',
    duree_note: 'Brief, deep and effective sessions \u2014 no lengthy appointment',
    soins_tag: 'Treatments offered',
    soins_title: 'What I<br>offer <em>you</em>',
    s1_title: 'Global Magnetic Treatment',
    s1_text: 'Rebalancing of the body\u2019s vital flows. In 10 to 15 minutes, a deep reconnection to your natural energy.',
    s1_pill: 'In-person \u00b7 Remote',
    s2_title: 'Pain Relief',
    s2_text: 'Targeted intervention on painful areas: joints, migraines, tensions. Fast action, results felt from the first session.',
    s2_pill: 'In-person',
    s3_title: 'Stress &amp; Anxiety',
    s3_text: 'Calming of the energetic nervous system. A few minutes are enough to regain calm, clarity and groundedness.',
    s3_pill: 'In-person \u00b7 Remote',
    s4_title: 'Emotional Blockages',
    s4_text: 'Release of deep emotional tensions. Ideal during transitions, grief or periods of inner instability.',
    s4_pill: 'In-person \u00b7 Remote',
    s5_title: 'Child Treatment',
    s5_text: 'A gentle approach for the youngest: sleep, concentration, school anxiety. Session adapted to their particular sensitivity.',
    s5_pill: 'In-person \u00b7 Home',
    s6_title: 'Personalised Follow-up',
    s6_text: 'Several close sessions for in-depth work. The short format lends itself to regular follow-up, integrated into daily life.',
    s6_pill: 'Tailored',
    mod1_tag: 'Method 01',
    mod1_title: 'Home visit<br><em>at your place</em>',
    mod1_text: 'I come directly to your home in departments 84, 13 and 30. You stay in your own environment, without any travel effort.',
    mod1_li1: 'Travel included in 3 departments',
    mod1_li2: '10 to 15 minute session',
    mod1_li3: 'No equipment needed',
    mod1_li4: 'Flexible hours',
    mod2_tag: 'Method 02',
    mod2_title: 'Remote<br><em>from your home</em>',
    mod2_text: 'Distance magnetism is just as effective as physical presence. From anywhere in France, receive a full session by phone or video call.',
    mod2_li1: 'By phone or video call',
    mod2_li2: 'Anywhere in France',
    mod2_li3: '10 to 15 minutes',
    mod2_li4: 'Ideal for reduced mobility',
    zones_tag: 'Travel zone',
    zones_title: 'I come<br><em>to you</em>',
    zones_desc: 'Based in <strong style="color:var(--gold2);font-weight:400;">Saint-Saturnin-l\u00e8s-Avignon (84450)</strong>, I travel to your home within a <strong style="color:var(--gold2);font-weight:400;">20-minute</strong> radius. For everything else, remote sessions are just as effective.',
    dept1_code: 'Vaucluse \u2014 Greater Avignon',
    dept1_name: 'Avignon &amp; Sorgues',
    dept2_code: 'Vaucluse \u2014 Sorgues Valley',
    dept2_name: 'Sorgues &amp; Luberon',
    dept3_code: 'Gard &amp; Bouches-du-Rh\u00f4ne',
    dept3_name: 'Villeneuve &amp; surroundings',
    dist_strong: 'Outside the zone or anywhere in France \u2014 remote session.',
    dist_text: '<strong data-i18n="dist_strong">Outside the zone or anywhere in France \u2014 remote session.</strong> Beyond 20 minutes from Saint-Saturnin-l\u00e8s-Avignon, I receive you by phone or video for a complete 10 to 15-minute session, just as effective as in person.',
    tarifs_tag: 'Pricing',
    tarifs_title: 'Simple &amp; <em>transparent</em>',
    t1_lbl: 'Remote session',
    t1_u: '10 to 15 min \u00b7 video or phone',
    t1_f1: 'All of France',
    t1_f2: 'Energy assessment included',
    t1_f3: 'Follow-up after session',
    t2_lbl: 'Home session',
    t2_u: '10 to 15 min \u00b7 20 min radius from St-Saturnin',
    t2_f1: 'Travel included',
    t2_f2: 'Treatment at your home',
    t2_f3: 'Assessment &amp; advice',
    t3_lbl: '5-session package',
    t3_u: 'i.e. 36\u20ac/session \u00b7 \u221210%',
    t3_f1: 'In-person or remote',
    t3_f2: 'Personalised follow-up',
    t3_f3: 'Valid for 3 months',
    btn_reserver: 'Book',
    contact_tag: 'Contact',
    contact_title: 'Book an <em>appointment</em>',
    contact_sub: 'Available Monday to Saturday, 9am to 7pm. Fast reply guaranteed.',
    contact_addr: '20-min radius around Saint-Saturnin-l\u00e8s-Avignon (84450)<br>Avignon \u00b7 Le Pontet \u00b7 Ved\u00e8ne \u00b7 Le Thor \u00b7 L\u2019Isle-sur-la-Sorgue\u2026<br>+ remote: all of France',
    contact_hours: 'Mon \u2013 Sat \u00b7 9am \u2013 7pm',
    wa_tag: 'WhatsApp',
    wa_title: 'Contact me<br><em>directly</em>',
    wa_sub: 'The fastest way to reach me. I usually reply within minutes, Monday to Saturday, 9am to 7pm.',
    wa_msg: 'Send a message',
    wa_call: 'Call via WhatsApp',
    wa_note_pre: 'Or book directly online via',
    wa_cal_btn: 'the booking calendar \u2192',
    footer_copy: '\u00a9 2025 Harmony Flux \u2014 Magnetism',
    footer_legal: 'Legal notice',
    footer_privacy: 'Privacy',
    wa_href_msg: 'https://wa.me/33788301574?text=Hello%2C%20I%20would%20like%20to%20book%20an%20appointment%20for%20a%20magnetism%20session.',
    wa_href_call: 'https://wa.me/33788301574',
  },
  pt: {
    nav_about: 'Sobre', nav_soins: 'Tratamentos', nav_zones: '\u00c1reas', nav_tarifs: 'Pre\u00e7os',
    hero_sub: 'Magnetismo &amp; Cuidados Energ\u00e9ticos',
    hero_desc: 'Sess\u00f5es curtas \u00b7 eficazes \u00b7 personalizadas',
    badge_min: '10 a 15 minutos',
    badge_home: 'Ao domic\u00edlio',
    badge_remote: '\u00c0 dist\u00e2ncia',
    badge_radius: '20 min em redor de St-Saturnin-l\u00e8s-Avignon',
    hero_scroll: 'Descobrir',
    about_tag: 'Sobre',
    about_title: 'Uma pr\u00e1tica<br>enraizada no <em>essencial</em>',
    about_text1: 'O magnetismo atua sobre os fluxos energ\u00e9ticos que percorrem o corpo. Em apenas alguns minutos, um tratamento dirigido pode restaurar o equil\u00edbrio, aliviar a dor ou acalmar as tens\u00f5es acumuladas.',
    about_text2: 'As minhas sess\u00f5es, intencionalmente curtas e intensas, foram pensadas para se integrar no seu quotidiano \u2014 sem lhe pedir tempo que n\u00e3o tem.',
    stat_min: 'Dura\u00e7\u00e3o m\u00ednima', stat_max: 'Dura\u00e7\u00e3o m\u00e1xima', stat_radius: 'Raio domic\u00edlio',
    img_tag: 'Cuidado &amp; Energia',
    img_title: 'Sentir<br>para <em>curar</em>',
    img_text: 'O magnetizador canaliza e redistribui as energias vitais com as m\u00e3os, sem contacto ou \u00e0 dist\u00e2ncia. Uma abordagem suave, r\u00e1pida e profunda para recuperar o seu equil\u00edbrio interior.',
    img_cta: 'Reservar uma sess\u00e3o \u2192',
    duree_label: 'Dura\u00e7\u00e3o de uma sess\u00e3o',
    duree_note: 'Cuidados breves, profundos e eficazes \u2014 sem consultas demoradas',
    soins_tag: 'Tratamentos oferecidos',
    soins_title: 'O que eu<br><em>ofere\u00e7o</em>',
    s1_title: 'Tratamento Magn\u00e9tico Global',
    s1_text: 'Reequil\u00edbrio dos fluxos vitais de todo o corpo. Em 10 a 15 minutos, uma reconex\u00e3o profunda \u00e0 sua energia natural.',
    s1_pill: 'Presencial \u00b7 Dist\u00e2ncia',
    s2_title: 'Al\u00edvio das Dores',
    s2_text: 'Interven\u00e7\u00e3o dirigida nas zonas dolorosas: articula\u00e7\u00f5es, enxaquecas, tens\u00f5es. A\u00e7\u00e3o r\u00e1pida, resultados sentidos desde a primeira sess\u00e3o.',
    s2_pill: 'Presencial',
    s3_title: 'Stress &amp; Ansiedade',
    s3_text: 'Acalmar o sistema nervoso energ\u00e9tico. Poucos minutos bastam para recuperar calma, clareza e enraizamento no presente.',
    s3_pill: 'Presencial \u00b7 Dist\u00e2ncia',
    s4_title: 'Bloqueios Emocionais',
    s4_text: 'Liberta\u00e7\u00e3o de tens\u00f5es emocionais profundas. Ideal em transi\u00e7\u00f5es, lutos ou per\u00edodos de instabilidade interior.',
    s4_pill: 'Presencial \u00b7 Dist\u00e2ncia',
    s5_title: 'Tratamento Infantil',
    s5_text: 'Abordagem suave para os mais novos: sono, concentra\u00e7\u00e3o, ansiedade escolar. Sess\u00e3o adaptada \u00e0 sua sensibilidade particular.',
    s5_pill: 'Presencial \u00b7 Domic\u00edlio',
    s6_title: 'Acompanhamento Personalizado',
    s6_text: 'V\u00e1rias sess\u00f5es pr\u00f3ximas para um trabalho em profundidade. O formato curto presta-se a um acompanhamento regular, integrado no quotidiano.',
    s6_pill: 'Personalizado',
    mod1_tag: 'Modalidade 01',
    mod1_title: 'Ao domic\u00edlio<br><em>em sua casa</em>',
    mod1_text: 'Desloco-me diretamente ao seu domic\u00edlio nos departamentos 84, 13 e 30. Fica no seu ambiente, sem esfor\u00e7o de deslocamento.',
    mod1_li1: 'Deslocamento inclu\u00eddo nos 3 dpts',
    mod1_li2: 'Sess\u00e3o de 10 a 15 minutos',
    mod1_li3: 'Nenhum equipamento necess\u00e1rio',
    mod1_li4: 'Hor\u00e1rios flex\u00edveis',
    mod2_tag: 'Modalidade 02',
    mod2_title: '\u00c0 dist\u00e2ncia<br><em>de sua casa</em>',
    mod2_text: 'O magnetismo \u00e0 dist\u00e2ncia \u00e9 t\u00e3o eficaz quanto a presen\u00e7a f\u00edsica. De qualquer lugar em Fran\u00e7a, receba um tratamento completo por telefone ou videoconfer\u00eancia.',
    mod2_li1: 'Por telefone ou videoconfer\u00eancia',
    mod2_li2: 'Em toda a Fran\u00e7a',
    mod2_li3: '10 a 15 minutos',
    mod2_li4: 'Ideal para mobilidade reduzida',
    zones_tag: 'Zona de deslocamento',
    zones_title: 'Eu vou<br><em>at\u00e9 si</em>',
    zones_desc: 'Baseado em <strong style="color:var(--gold2);font-weight:400;">Saint-Saturnin-l\u00e8s-Avignon (84450)</strong>, desloco-me ao domic\u00edlio num raio de <strong style="color:var(--gold2);font-weight:400;">20 minutos</strong>. Para todo o resto, a sess\u00e3o \u00e0 dist\u00e2ncia \u00e9 igualmente eficaz.',
    dept1_code: 'Vaucluse \u2014 Grande Avignon',
    dept1_name: 'Avignon &amp; Sorgues',
    dept2_code: 'Vaucluse \u2014 Vale de Sorgues',
    dept2_name: 'Sorgues &amp; Luberon',
    dept3_code: 'Gard &amp; Bouches-du-Rh\u00f4ne',
    dept3_name: 'Villeneuve &amp; arredores',
    dist_strong: 'Fora da zona ou toda a Fran\u00e7a \u2014 sess\u00e3o \u00e0 dist\u00e2ncia.',
    dist_text: '<strong data-i18n="dist_strong">Fora da zona ou toda a Fran\u00e7a \u2014 sess\u00e3o \u00e0 dist\u00e2ncia.</strong> Al\u00e9m de 20 minutos de Saint-Saturnin-l\u00e8s-Avignon, recebo-o por telefone ou videoconfer\u00eancia para um tratamento completo de 10 a 15 minutos, t\u00e3o eficaz como em presen\u00e7a.',
    tarifs_tag: 'Pre\u00e7os',
    tarifs_title: 'Simples &amp; <em>transparente</em>',
    t1_lbl: 'Sess\u00e3o \u00e0 dist\u00e2ncia',
    t1_u: '10 a 15 min \u00b7 v\u00eddeo ou telefone',
    t1_f1: 'Toda a Fran\u00e7a',
    t1_f2: 'Balan\u00e7o energ\u00e9tico inclu\u00eddo',
    t1_f3: 'Retorno ap\u00f3s sess\u00e3o',
    t2_lbl: 'Sess\u00e3o ao domic\u00edlio',
    t2_u: '10 a 15 min \u00b7 raio 20 min de St-Saturnin',
    t2_f1: 'Deslocamento inclu\u00eddo',
    t2_f2: 'Tratamento no seu domic\u00edlio',
    t2_f3: 'Balan\u00e7o &amp; conselhos',
    t3_lbl: 'Pack 5 sess\u00f5es',
    t3_u: '36\u20ac/sess\u00e3o \u00b7 \u221210%',
    t3_f1: 'Presencial ou dist\u00e2ncia',
    t3_f2: 'Acompanhamento personalizado',
    t3_f3: 'V\u00e1lido 3 meses',
    btn_reserver: 'Reservar',
    contact_tag: 'Contacto',
    contact_title: 'Marque uma <em>consulta</em>',
    contact_sub: 'Dispon\u00edvel de segunda a s\u00e1bado, das 9h \u00e0s 19h. Resposta r\u00e1pida garantida.',
    contact_addr: 'Raio de 20 min em redor de Saint-Saturnin-l\u00e8s-Avignon (84450)<br>Avignon \u00b7 Le Pontet \u00b7 Ved\u00e8ne \u00b7 Le Thor \u00b7 L\u2019Isle-sur-la-Sorgue\u2026<br>+ dist\u00e2ncia: toda a Fran\u00e7a',
    contact_hours: 'Seg \u2013 S\u00e1b \u00b7 9h \u2013 19h',
    wa_tag: 'WhatsApp',
    wa_title: 'Contacte-me<br><em>diretamente</em>',
    wa_sub: 'A forma mais r\u00e1pida de me contactar. Respondo geralmente em poucos minutos, de segunda a s\u00e1bado das 9h \u00e0s 19h.',
    wa_msg: 'Enviar mensagem',
    wa_call: 'Ligar via WhatsApp',
    wa_note_pre: 'Ou reserve diretamente online via',
    wa_cal_btn: 'o calend\u00e1rio de reservas \u2192',
    footer_copy: '\u00a9 2025 Harmony Flux \u2014 Magnetismo',
    footer_legal: 'Aviso legal',
    footer_privacy: 'Privacidade',
    wa_href_msg: 'https://wa.me/33788301574?text=Ol%C3%A1%2C%20gostaria%20de%20marcar%20uma%20sess%C3%A3o%20de%20magnetismo.',
    wa_href_call: 'https://wa.me/33788301574',
  }
};

function setLang(lang) {
  document.querySelectorAll('.lang-btn').forEach(btn => {
    btn.classList.toggle('active', btn.textContent.trim().toLowerCase() === lang);
  });
  const t = translations[lang];
  if (!t) return;
  document.querySelectorAll('[data-i18n]').forEach(el => {
    const key = el.getAttribute('data-i18n');
    if (t[key] !== undefined) el.innerHTML = t[key];
  });
  // Update WhatsApp hrefs
  const msgBtn = document.getElementById('wa-msg-btn');
  if (msgBtn && t.wa_href_msg) msgBtn.href = t.wa_href_msg;
  const callBtn = document.getElementById('wa-call-btn');
  if (callBtn && t.wa_href_call) callBtn.href = t.wa_href_call;
  // Update document lang and title
  document.documentElement.lang = lang;
  const titles = { fr: 'Harmony Flux \u2014 Magn\u00e9tisme', en: 'Harmony Flux \u2014 Magnetism', pt: 'Harmony Flux \u2014 Magnetismo' };
  document.title = titles[lang] || document.title;
}
</script>'''

# Find and replace the script block
if old_script in html:
    html = html.replace(old_script, new_script)
    print("Script block replaced successfully")
else:
    print("WARNING: Could not find old script block exactly. Will try partial match.")
    # Try to find the script by markers
    start_marker = '<!-- i18n Traductions -->\n<script>'
    end_marker = '</script>\n\n<!-- Génération du ciel étoilé -->'
    
    start_idx = html.find(start_marker)
    end_idx = html.find(end_marker)
    
    if start_idx != -1 and end_idx != -1:
        end_idx_full = end_idx + len('</script>')
        html = html[:start_idx] + new_script + html[end_idx_full:]
        print(f"Script replaced via markers at positions {start_idx}:{end_idx_full}")
    else:
        print(f"ERROR: start_idx={start_idx}, end_idx={end_idx}")

# Write the result
with open('/home/user/workspace/harmony-flux/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("File written successfully.")
print(f"Total file size: {len(html)} bytes")

# Verify key replacements
checks = [
    'data-i18n="hero_sub"',
    'data-i18n="hero_desc"',
    'data-i18n="badge_min"',
    'data-i18n="badge_home"',
    'data-i18n="badge_remote"',
    'data-i18n="badge_radius"',
    'data-i18n="hero_scroll"',
    'data-i18n="duree_label"',
    'data-i18n="duree_note"',
    'data-i18n="soins_tag"',
    'data-i18n="soins_title"',
    'data-i18n="s1_title"',
    'data-i18n="s2_title"',
    'data-i18n="s3_title"',
    'data-i18n="s4_title"',
    'data-i18n="s5_title"',
    'data-i18n="s6_title"',
    'data-i18n="s1_pill"',
    'data-i18n="s2_pill"',
    'data-i18n="s3_pill"',
    'data-i18n="s4_pill"',
    'data-i18n="s5_pill"',
    'data-i18n="s6_pill"',
    'data-i18n="mod1_tag"',
    'data-i18n="mod1_title"',
    'data-i18n="mod1_text"',
    'data-i18n="mod1_li1"',
    'data-i18n="mod1_li2"',
    'data-i18n="mod1_li3"',
    'data-i18n="mod1_li4"',
    'data-i18n="mod2_tag"',
    'data-i18n="mod2_title"',
    'data-i18n="mod2_text"',
    'data-i18n="mod2_li1"',
    'data-i18n="mod2_li2"',
    'data-i18n="mod2_li3"',
    'data-i18n="mod2_li4"',
    'data-i18n="zones_tag"',
    'data-i18n="zones_title"',
    'data-i18n="zones_desc"',
    'data-i18n="dept1_code"',
    'data-i18n="dept1_name"',
    'data-i18n="dept2_code"',
    'data-i18n="dept2_name"',
    'data-i18n="dept3_code"',
    'data-i18n="dept3_name"',
    'data-i18n="dist_strong"',
    'data-i18n="dist_text"',
    'data-i18n="tarifs_tag"',
    'data-i18n="tarifs_title"',
    'data-i18n="t1_lbl"',
    'data-i18n="t1_u"',
    'data-i18n="t1_f1"',
    'data-i18n="t1_f2"',
    'data-i18n="t1_f3"',
    'data-i18n="t2_lbl"',
    'data-i18n="t2_u"',
    'data-i18n="t2_f1"',
    'data-i18n="t2_f2"',
    'data-i18n="t2_f3"',
    'data-i18n="t3_lbl"',
    'data-i18n="t3_u"',
    'data-i18n="t3_f1"',
    'data-i18n="t3_f2"',
    'data-i18n="t3_f3"',
    'data-i18n="btn_reserver"',
    'data-i18n="contact_tag"',
    'data-i18n="contact_title"',
    'data-i18n="contact_sub"',
    'data-i18n="contact_addr"',
    'data-i18n="contact_hours"',
    'data-i18n="wa_tag"',
    'data-i18n="wa_title"',
    'data-i18n="wa_sub"',
    'data-i18n="wa_msg"',
    'data-i18n="wa_call"',
    'data-i18n="wa_note_pre"',
    'data-i18n="wa_cal_btn"',
    'data-i18n="footer_copy"',
    'data-i18n="footer_legal"',
    'data-i18n="footer_privacy"',
    'id="wa-msg-btn"',
    'id="wa-call-btn"',
]

missing = []
for check in checks:
    if check not in html:
        missing.append(check)

if missing:
    print(f"\nMISSING attributes ({len(missing)}):")
    for m in missing:
        print(f"  - {m}")
else:
    print(f"\nAll {len(checks)} checks passed!")
