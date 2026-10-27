import urllib.parse, datetime, json, os
BASE="https://caro123-create.github.io/chat-appartement-connecte/"
TAG="rappelalertes-21"
AFF=json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)),"data","affiliate.json")))
def secondary(merchant, url_path=""):
    """Bouton Zooplus/Tractive : rendu UNIQUEMENT si activé et IDs réels présents."""
    a=AFF.get("awin",{}); mid=a.get("merchants",{}).get(merchant,{}).get("mid")
    label={"zooplus":"Voir chez Zooplus","tractive":"Voir chez Tractive"}[merchant]
    if a.get("enabled") and a.get("awinaffid") and mid and url_path:
        u=f"https://www.awin1.com/cread.php?awinmid={mid}&awinaffid={a['awinaffid']}&ued="+urllib.parse.quote(url_path,safe="")
    elif merchant=="tractive" and AFF.get("tractive_direct",{}).get("enabled") and AFF["tractive_direct"].get("url"):
        u=AFF["tractive_direct"]["url"]
    else:
        return ""
    return f' <a class="btn btn-secondary" href="{u}" rel="sponsored nofollow noopener" target="_blank">{label}</a>'
SITE="Chat Appartement Connecté"
TODAY="2026-10-27"
def amz(q,label=None):
    u="https://www.amazon.fr/s?k="+urllib.parse.quote_plus(q)+"&tag="+TAG
    return f'<a class="btn" href="{u}" rel="sponsored nofollow noopener" target="_blank">Voir sur Amazon{(" – "+label) if label else ""}</a>'
NAV=[("top-5-equipements-chat-appartement-2026.html","Top 5 équipements 2026"),
     ("meilleure-litiere-automatique-2026.html","Litière automatique"),
     ("gps-chat-tractive-vs-airtag.html","GPS chat"),
     ("meilleure-fontaine-eau-chat-2026.html","Fontaine à eau"),
     ("distributeur-croquettes-connecte.html","Distributeur connecté"),
     ("litter-robot-4-vs-petkit-pura-max-2.html","Litter-Robot 4 vs PetKit"),
     ("camera-surveillance-chat-appartement.html","Caméra chat"),
     ("collier-gps-chat-sans-abonnement.html","GPS sans abonnement"),
     ("litiere-automatique-petit-appartement.html","Litière petit appart"),
     ("budget-kit-chat-appartement-connecte.html","Kit débutant & budget")]
GUMROAD="https://fluenthub.gumroad.com/l/jvlfm"
PRODUCT="Chat d’appartement connecté : le plan en 7 jours"
PRICE="12 €"
CHECKLIST_GUMROAD="https://fluenthub.gumroad.com/l/dcbmyx"
CHECKLIST_PRICE="6,90 €"
CTA_BANNER=f'''<aside class="paid-cta"><p><strong>Guide payant — {PRODUCT} ({PRICE})</strong><br>En 7 jours, équipez votre chat d’appart (litière, eau, repas, sécurité, budget) sans tout acheter d’un coup.</p><p><a class="btn-paid" href="guide.html">Découvrir le plan en 7 jours</a></p><p class="note">Produit numérique payant, vendu séparément via Gumroad. Ce n’est pas un lien d’affiliation Amazon.</p></aside>'''
AUDIT_LINK='<p class="note">Pas encore prêt à acheter ? Commencez par notre <a href="telechargement-audit.html">audit gratuit en 1 jour (PDF)</a>.</p>'
DISC='<p class="disc"><strong>Liens affiliés :</strong> en tant que Partenaire Amazon, nous réalisons un bénéfice sur les achats remplissant les conditions requises. Cela ne change pas le prix pour vous. Prix et disponibilités variables : vérifiez toujours sur la page du vendeur.</p>'
def page(fn,title,desc,h1,body,related=True,head_extra=""):
    nav="".join(f'<a href="{f}">{n}</a>' for f,n in NAV)+'<a class="nav-paid" href="guide.html">Plan 7 jours (12 €)</a><a class="nav-paid" href="checklist.html">Checklist (6,90 €)</a><a href="telechargement-audit.html">Audit gratuit (PDF)</a>'
    rel=""
    if related:
        rel='<section class="related"><h2>À lire aussi</h2><ul>'+"".join(f'<li><a href="{f}">{n}</a></li>' for f,n in NAV if f!=fn)+'</ul></section>'
    canon=BASE+("" if fn=="index.html" else fn)
    html=f'''<!doctype html>
<html lang="fr"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{canon}">
<meta property="og:title" content="{title}"><meta property="og:description" content="{desc}"><meta property="og:type" content="article"><meta property="og:url" content="{canon}">
<link rel="stylesheet" href="styles.css">
{head_extra}</head><body>
<header><a class="logo" href="./">🐱 {SITE}</a><nav>{nav}</nav></header>
<main>
<h1>{h1}</h1>
{DISC if fn not in ("affiliation.html","guide.html","telechargement-audit.html","checklist.html") else ""}
{body}
{(CTA_BANNER+AUDIT_LINK) if fn not in ("index.html","guide.html","affiliation.html","telechargement-audit.html","checklist.html") else ""}
{rel}
</main>
<footer><p>{SITE} — guides indépendants pour équiper un chat d’intérieur. Mis à jour le 27 octobre 2026.</p>
<p>En tant que Partenaire Amazon, nous réalisons un bénéfice sur les achats remplissant les conditions requises. <a href="affiliation.html">Affiliation &amp; mentions légales</a></p>
<p>Nos guides ne remplacent pas l’avis d’un vétérinaire.</p></footer>
</body></html>'''
    open(fn,"w").write(html)

# ---------- index
cards="".join(f'<li><a href="{f}"><strong>{n}</strong></a></li>' for f,n in NAV)
page("index.html",
 "Chat Appartement Connecté – guides litières auto, GPS, fontaines 2026",
 "Guides d’achat indépendants pour chat d’appartement : litière automatique, GPS Tractive ou AirTag, fontaine à eau, distributeur de croquettes, caméra, kit débutant.",
 "Équiper son chat d’appartement avec des objets connectés utiles",
 f'''<p class="lead">Un chat qui vit en intérieur dépend entièrement de son environnement : une litière propre, de l’eau qui donne envie de boire, des repas réguliers même quand vous rentrez tard. Les objets connectés peuvent aider — à condition de bien les choisir. Ici, on compare les modèles réels du marché, sans promesse miracle, avec les points qui comptent vraiment en appartement : bruit, encombrement, coût d’usage et sécurité.</p>
<section class="paid-cta home"><h2>Nouveau : le plan en 7 jours (guide payant, 12 €)</h2>
<p>En 7 jours, équipez votre chat d’appart (litière, eau, repas, sécurité, budget) sans tout acheter d’un coup. Une étape par jour, dans le bon ordre, avec checklist et tableau budget.</p>
<p><a class="btn-paid" href="guide.html">Voir le contenu du plan</a> <a class="btn-paid alt" href="{GUMROAD}" target="_blank" rel="noopener">Acheter sur Gumroad – 12 €</a></p>
<p class="note">Produit numérique payant édité par Chat Appartement Connecté et vendu séparément via Gumroad. Il est distinct des liens d’affiliation Amazon du site.</p>
<p class="note">Envie de commencer gratuitement ? Téléchargez notre <a href="telechargement-audit.html">audit en 1 jour (checklist PDF gratuite)</a>.</p>
<p class="note">Besoin seulement de savoir quoi acheter ? <a href="checklist.html">Checklist shopping du chat connecté</a> (produit payant, 6,90 € via Gumroad).</p></section>
<h2>Nos guides</h2>
<ul class="cards">{cards}</ul>
<h2>Notre méthode</h2>
<p>Nous partons des fiches et manuels des fabricants, des retours d’utilisateurs et des contraintes concrètes d’un logement (surface, prises, Wi-Fi 2,4 GHz). Quand une donnée n’est pas claire ou varie selon les versions, nous le disons plutôt que d’inventer un chiffre. Les prix changent souvent : nous n’en affichons pas de précis, vérifiez-les sur la page du vendeur.</p>
<h2>Par où commencer ?</h2>
<ul>
<li>Vous voulez l’essentiel en une page : notre <a href="top-5-equipements-chat-appartement-2026.html">Top 5 des équipements pour chat d’appartement 2026</a>.</li>
<li>Vous travaillez de longues journées : commencez par le <a href="distributeur-croquettes-connecte.html">distributeur de croquettes connecté</a> et la <a href="meilleure-fontaine-eau-chat-2026.html">fontaine à eau</a>.</li>
<li>L’odeur de litière envahit le studio : lisez notre <a href="meilleure-litiere-automatique-2026.html">guide des litières automatiques</a>, puis le duel <a href="litter-robot-4-vs-petkit-pura-max-2.html">Litter-Robot 4 vs PetKit</a>.</li>
<li>Votre chat a accès au balcon ou s’échappe parfois : comparez <a href="gps-chat-tractive-vs-airtag.html">Tractive et AirTag</a>, ou voyez les options de <a href="collier-gps-chat-sans-abonnement.html">GPS sans abonnement</a>.</li>
<li>Vous vivez dans un studio : notre guide <a href="litiere-automatique-petit-appartement.html">litière automatique en petit appartement</a> (bruit, taille, odeurs).</li>
<li>Vous voulez voir votre chat en journée : notre guide <a href="camera-surveillance-chat-appartement.html">caméra de surveillance pour chat</a>.</li>
<li>Vous débutez et voulez maîtriser le budget : notre <a href="budget-kit-chat-appartement-connecte.html">kit débutant chat connecté</a>.</li>
</ul>''',related=False)

# ---------- 1 litière
page("meilleure-litiere-automatique-2026.html",
 "Meilleure litière automatique 2026 : notre sélection pour appartement",
 "Litière automatique autonettoyante en 2026 : Litter-Robot 4, PetKit Pura Max 2 et alternatives. Critères, poids minimum du chat, bruit, coût d’usage.",
 "Meilleure litière automatique 2026 : laquelle choisir en appartement ?",
 f'''<p class="lead">Une litière automatique sépare les selles et urines agglomérées du reste du sable après chaque passage, puis les stocke dans un tiroir fermé. En appartement, le bénéfice principal est l’odeur : les déchets ne restent pas à l’air libre. Mais ces appareils sont encombrants, coûteux, et tous les chats ne les acceptent pas.</p>
<h2>Les critères qui comptent vraiment</h2>
<ul>
<li><strong>Poids minimum du chat</strong> : les capteurs de présence reposent en partie sur le poids. Le Litter-Robot 4 exige au moins 1,36 kg en mode automatique, la PetKit Pura Max 2 environ 1,5 kg et un chat de plus de 6 mois (selon les manuels). Pas d’automatique pour un chaton.</li>
<li><strong>Encombrement</strong> : comptez la hauteur, la profondeur <em>et</em> la place pour sortir le tiroir. Le Litter-Robot 4 fait environ 75 cm de haut ; la Pura Max 2 environ 55 cm.</li>
<li><strong>Type de litière</strong> : il faut une litière agglomérante. Certains modèles tolèrent le tofu, d’autres préfèrent l’argile ; vérifiez la notice.</li>
<li><strong>Sécurité</strong> : capteurs de poids, infrarouges ou laser, anti-pincement. Désactivez tout mode de rotation « forcée » et observez les premiers cycles.</li>
<li><strong>Coût d’usage</strong> : sacs propriétaires ou non, filtres, désodorisants. Sur 2–3 ans, cela pèse autant que le prix d’achat.</li>
<li><strong>Application</strong> : la plupart fonctionnent en Wi-Fi 2,4 GHz uniquement et suivent nombre de passages et poids — pratique pour repérer un changement à signaler au vétérinaire.</li>
</ul>
<h2>Notre sélection</h2>
<div class="pick"><h3>1. Litter-Robot 4 (Whisker) — le haut de gamme éprouvé</h3>
<p>Globe rotatif avec grande entrée (environ 40 × 40 cm), capteurs laser de niveau et de présence, application Whisker très complète. Accepte des sacs standards selon l’assistance de la marque. Inconvénients : prix élevé et hauteur importante, à mesurer avant achat.</p>
<p><strong>Pour qui :</strong> grands chats, foyers multi-chats, budget confortable.</p>{amz("Litter-Robot 4")}</div>
<div class="pick"><h3>2. PetKit Pura Max 2 — le meilleur compromis</h3>
<p>Plus basse et plus large, entrée plus étroite (environ 25 × 20 cm), désodorisant intégré, application PetKit qui centralise aussi fontaines et distributeurs de la marque. Bon choix pour un chat de taille moyenne dans un logement où la hauteur compte.</p>
<p><strong>Pour qui :</strong> chats de 3 à 6 kg environ, appartement avec peu de place en hauteur.</p>{amz("PetKit Pura Max 2")}</div>
<div class="pick"><h3>3. Alternatives à regarder</h3>
<p>Le marché compte d’autres modèles (Neakasa, PetSafe ScoopFree, Catlink…). Leurs principes diffèrent (râteau, tapis roulant, globe). Avant d’acheter, vérifiez le poids minimum, le type de litière accepté et le prix des consommables.</p>{amz("litière automatique autonettoyante chat")}</div>
<h2>Bien réussir la transition</h2>
<ol><li>Installez l’appareil éteint à côté de l’ancien bac, avec un peu de litière usagée pour l’odeur.</li>
<li>Laissez le chat l’explorer quelques jours avant d’activer les cycles.</li>
<li>Gardez un bac classique tant que l’adoption n’est pas totale.</li>
<li>Ne posez pas l’appareil sur un tapis épais : les capteurs de poids se dérèglent.</li></ol>
<h2>Notre avis</h2>
<p>Pour la majorité des appartements, la <strong>PetKit Pura Max 2</strong> offre le meilleur équilibre. Si vous avez un grand chat ou plusieurs chats et le budget, le <strong>Litter-Robot 4</strong> reste la référence. Détail complet dans notre <a href="litter-robot-4-vs-petkit-pura-max-2.html">comparatif Litter-Robot 4 vs PetKit</a>.</p>''')

# ---------- 2 GPS
page("gps-chat-tractive-vs-airtag.html",
 "GPS chat : Tractive ou AirTag ? Comparatif 2026",
 "Tractive CAT 6 Mini ou AirTag pour suivre son chat ? Différences de technologie, abonnement, autonomie, poids et sécurité du collier.",
 "GPS pour chat : Tractive ou AirTag, que choisir ?",
 f'''<p class="lead">Un chat d’appartement peut fuguer par une fenêtre, un balcon ou une porte restée ouverte. Deux solutions reviennent souvent : un vrai traceur GPS comme Tractive, ou un AirTag d’Apple accroché au collier. Elles ne fonctionnent pas du tout de la même manière.</p>
<h2>La différence essentielle</h2>
<table><thead><tr><th></th><th>Tractive CAT 6 Mini</th><th>AirTag</th></tr></thead><tbody>
<tr><td>Technologie</td><td>GPS + réseau mobile (carte SIM intégrée)</td><td>Bluetooth, repéré par les appareils Apple à proximité (réseau Localiser)</td></tr>
<tr><td>Suivi en temps réel</td><td>Oui, mode LIVE</td><td>Non : position mise à jour quand un iPhone passe à côté</td></tr>
<tr><td>Abonnement</td><td>Obligatoire (formules Basic ou Premium)</td><td>Aucun</td></tr>
<tr><td>Autonomie annoncée</td><td>Jusqu’à 7 jours (selon usage)</td><td>Environ un an (pile bouton)</td></tr>
<tr><td>Chats visés</td><td>3 à 8 kg selon Tractive</td><td>Non conçu pour les animaux par Apple</td></tr>
<tr><td>Téléphone</td><td>iPhone et Android</td><td>iPhone/iPad uniquement</td></tr>
</tbody></table>
<h2>Tractive : le vrai GPS</h2>
<p>Le CAT 6 Mini intègre le traceur dans un collier de sécurité. Il permet de définir des zones (alerte si le chat sort), de suivre l’animal en direct et propose un suivi d’activité et de sommeil. L’abonnement couvre les frais de réseau mobile : c’est le vrai coût sur la durée, à intégrer dès le départ. La couverture dépend du réseau mobile là où se trouve le chat (caves, parkings souterrains = signal faible).</p>{amz("Tractive GPS chat CAT 6 Mini")}
<h2>AirTag : la solution sans abonnement</h2>
<p>En ville, l’AirTag peut être localisé grâce aux nombreux iPhone qui passent à proximité. Mais la position n’est pas continue, la précision dépend du passage d’appareils Apple, et Apple ne le conçoit pas pour les animaux. Il peut aussi déclencher des alertes « AirTag inconnu » chez des passants. Il faut un porte-AirTag adapté, sur un collier à <strong>ouverture de sécurité</strong>.</p>{amz("Apple AirTag","AirTag")} {amz("porte AirTag collier chat sécurité","porte-AirTag")}
<h2>Sécurité du collier</h2>
<p>Quel que soit le choix, le collier doit s’ouvrir sous la traction (boucle anti-étranglement). Ajustez-le pour passer deux doigts, et surveillez les premiers jours. Si votre chat ne supporte pas le collier, aucun traceur ne sera une bonne solution.</p>
<h2>Notre avis</h2>
<ul><li><strong>Chat qui sort ou qui a déjà fugué</strong> : Tractive, malgré l’abonnement — c’est le seul des deux qui suit en temps réel.</li>
<li><strong>Chat strictement d’intérieur, propriétaire sur iPhone, en ville</strong> : un AirTag peut servir de filet de sécurité bon marché.</li></ul>
<p>Pour sécuriser aussi la maison pendant vos absences, voyez notre guide <a href="distributeur-croquettes-connecte.html">distributeur connecté</a> (certains intègrent une caméra).</p>''')

# ---------- 3 fontaine
page("meilleure-fontaine-eau-chat-2026.html",
 "Meilleure fontaine à eau pour chat 2026 : guide d’achat",
 "Fontaine à eau pour chat en 2026 : PetKit Eversweet, Petlibro, Xiaomi, Catit. Pompe sans fil, filtre, bruit, entretien et capacité.",
 "Meilleure fontaine à eau pour chat 2026",
 f'''<p class="lead">Beaucoup de chats boivent peu, surtout s’ils mangent des croquettes. Une fontaine fait circuler et filtre l’eau, ce qui incite souvent à boire davantage. En appartement, le bruit et l’entretien font la différence.</p>
<h2>Les critères</h2>
<ul>
<li><strong>Pompe</strong> : les modèles à pompe sans fil (alimentée par induction) évitent qu’un câble trempe dans l’eau et sont plus faciles à nettoyer.</li>
<li><strong>Bruit</strong> : un ronronnement léger est normal ; un bruit qui augmente signale souvent un niveau d’eau bas ou une pompe encrassée.</li>
<li><strong>Capacité</strong> : environ 1,5 à 3 L pour un chat ; plus si plusieurs chats ou absences d’un week-end.</li>
<li><strong>Matériau</strong> : l’inox ou la céramique se nettoient mieux que le plastique, sensible aux rayures.</li>
<li><strong>Filtres</strong> : vérifiez le prix et la disponibilité des filtres de rechange avant d’acheter.</li>
<li><strong>Connectée ou non</strong> : l’application peut alerter sur le niveau d’eau ou le changement de filtre ; utile, pas indispensable.</li>
</ul>
<h2>Modèles à considérer</h2>
<div class="pick"><h3>PetKit Eversweet</h3><p>Gamme populaire avec pompe sans fil sur les versions récentes, compatible avec l’application PetKit pour certaines versions. Pratique si vous avez déjà une litière ou un distributeur de la marque.</p>{amz("PetKit Eversweet fontaine chat")}</div>
<div class="pick"><h3>Petlibro (gamme Dockstream et autres)</h3><p>Fontaines avec ou sans connexion, options en inox. Bonne alternative si vous voulez suivre la consommation d’eau via une application.</p>{amz("Petlibro fontaine chat")}</div>
<div class="pick"><h3>Xiaomi Smart Pet Fountain</h3><p>Design sobre, pilotage via l’application Xiaomi Home. Intéressant dans un appartement déjà équipé de l’écosystème Xiaomi.</p>{amz("Xiaomi Smart Pet Fountain")}</div>
<div class="pick"><h3>Catit Pixi / Catit Flower</h3><p>Modèles simples et répandus, non ou peu connectés, filtres faciles à trouver. Parfaits pour tester si votre chat aime l’eau courante.</p>{amz("Catit fontaine chat")}</div>
<h2>Entretien : le point qu’on oublie</h2>
<p>Changez l’eau et rincez le réservoir régulièrement (plusieurs fois par semaine), nettoyez la pompe selon la notice et remplacez le filtre au rythme indiqué. Une fontaine mal entretenue est pire qu’une gamelle propre. Placez-la loin de la litière et de la gamelle de nourriture.</p>
<h2>Notre avis</h2>
<p>Pour la plupart des chats d’appartement, une fontaine à <strong>pompe sans fil</strong> d’environ 2 L, facile à démonter, suffit. La connexion est un bonus pour les foyers déjà équipés (PetKit, Xiaomi). Complétez avec un <a href="distributeur-croquettes-connecte.html">distributeur de croquettes connecté</a> pour les longues journées.</p>
<p class="note">Un chat qui boit soudainement beaucoup plus ou beaucoup moins doit être montré au vétérinaire.</p>''')

# ---------- 4 distributeur
page("distributeur-croquettes-connecte.html",
 "Distributeur de croquettes connecté pour chat : guide 2026",
 "Bien choisir un distributeur de croquettes connecté (Wi-Fi, caméra, batterie de secours) : Petlibro, PetKit, Xiaomi. Critères et pièges.",
 "Distributeur de croquettes connecté : comment bien choisir ?",
 f'''<p class="lead">Un distributeur programmable sert des portions à heures fixes, même quand vous rentrez tard. La version connectée ajoute le pilotage à distance, des alertes (bourrage, réservoir bas) et parfois une caméra. Idéal pour un chat d’appartement qui réclame à 5 h du matin.</p>
<h2>Les critères</h2>
<ul>
<li><strong>Fiabilité de distribution</strong> : vérifiez la taille de croquettes acceptée ; les grosses croquettes ou formes irrégulières peuvent bloquer.</li>
<li><strong>Alimentation de secours</strong> : piles ou batterie en plus du secteur, pour continuer à servir en cas de coupure. Sans Wi-Fi, le programme local doit continuer à fonctionner.</li>
<li><strong>Réservoir hermétique</strong> : joint et sachet déshydratant préservent les croquettes.</li>
<li><strong>Bol inox amovible</strong> : plus hygiénique, passe souvent au lave-vaisselle.</li>
<li><strong>Caméra</strong> : pratique pour voir si le chat mange, mais pose la question de la vie privée (où partent les images ? abonnement cloud ?).</li>
<li><strong>Multi-chats</strong> : un distributeur à deux bols ou un modèle à puce par chat si les régimes diffèrent.</li>
</ul>
<h2>Modèles à considérer</h2>
<div class="pick"><h3>Petlibro (Granary, Air…)</h3><p>Marque très présente sur ce segment, avec des versions Wi-Fi, à caméra et à double bol. Bonne option pour démarrer.</p>{amz("Petlibro distributeur croquettes chat wifi")}</div>
<div class="pick"><h3>PetKit Fresh Element</h3><p>S’intègre à l’application PetKit avec la litière et la fontaine de la marque : tout est au même endroit.</p>{amz("PetKit Fresh Element distributeur")}</div>
<div class="pick"><h3>Xiaomi Smart Pet Food Feeder</h3><p>Pilotage via Xiaomi Home, design compact. Cohérent si vous avez déjà la fontaine Xiaomi.</p>{amz("Xiaomi Smart Pet Food Feeder")}</div>
<div class="pick"><h3>Avec caméra</h3><p>Plusieurs marques proposent un distributeur avec caméra intégrée. Vérifiez si l’enregistrement nécessite un abonnement.</p>{amz("distributeur croquettes chat caméra wifi")}</div>
<h2>Les limites</h2>
<p>Un distributeur ne remplace pas une présence : au-delà d’un week-end, faites passer quelqu’un (litière, eau, santé). Testez le programme plusieurs jours en votre présence avant de compter dessus. Respectez la ration journalière conseillée par votre vétérinaire et répartissez-la en petits repas.</p>
<h2>Notre avis</h2>
<p>Un modèle Wi-Fi avec <strong>batterie de secours</strong> et <strong>bol inox</strong> couvre l’essentiel. Prenez une caméra seulement si elle vous rassure vraiment. Associez-le à une <a href="meilleure-fontaine-eau-chat-2026.html">fontaine à eau</a> pour des absences sereines.</p>''')

# ---------- 5 comparatif
page("litter-robot-4-vs-petkit-pura-max-2.html",
 "Litter-Robot 4 vs PetKit Pura Max 2 : comparatif 2026",
 "Litter-Robot 4 ou PetKit Pura Max 2 ? Dimensions, entrée, poids minimum du chat, application, sacs et consommables : notre comparatif.",
 "Litter-Robot 4 vs PetKit Pura Max 2 : le comparatif",
 f'''<p class="lead">Ce sont les deux litières automatiques qu’on compare le plus souvent. Elles reposent sur le même principe (rotation pour tamiser la litière agglomérante) mais diffèrent nettement par la taille, l’entrée et l’écosystème.</p>
<h2>Fiche comparée</h2>
<table><thead><tr><th></th><th>Litter-Robot 4</th><th>PetKit Pura Max 2</th></tr></thead><tbody>
<tr><td>Dimensions (environ)</td><td>75 × 56 × 69 cm (H × L × P)</td><td>55 × 62 × 54 cm (H × L × P)</td></tr>
<tr><td>Poids de l’appareil</td><td>~10,9 kg</td><td>~10 kg</td></tr>
<tr><td>Entrée</td><td>~40 × 40 cm</td><td>~25 × 20 cm</td></tr>
<tr><td>Poids mini du chat (auto)</td><td>1,36 kg</td><td>~1,5 kg, chat de plus de 6 mois</td></tr>
<tr><td>Application</td><td>Whisker</td><td>PetKit</td></tr>
<tr><td>Connexion</td><td>Wi-Fi 2,4 GHz</td><td>Wi-Fi 2,4 GHz + Bluetooth</td></tr>
<tr><td>Prix</td><td colspan="2">Variables — vérifiez sur Amazon ou chez le fabricant</td></tr>
</tbody></table>
<p class="note">Données issues des manuels fabricants ; elles peuvent varier selon les révisions.</p>
<h2>Taille et confort du chat</h2>
<p>Le Litter-Robot 4 est nettement plus haut mais offre une très grande entrée : c’est l’avantage pour un grand chat (type Maine Coon) ou un chat qui refuse les ouvertures étroites. La Pura Max 2 est plus basse, plus facile à loger sous une fenêtre ou dans une salle de bain, mais son entrée plus étroite peut gêner un gros gabarit.</p>
<h2>Sécurité</h2>
<p>Le Litter-Robot 4 utilise des capteurs laser à l’entrée et une mesure du poids. La PetKit annonce plusieurs capteurs (poids, infrarouge) et une structure anti-pincement. Dans les deux cas : laissez désactivés les modes qui forcent la rotation, observez les premiers cycles et gardez un bac classique pendant la transition.</p>
<h2>Application et suivi</h2>
<p>L’application Whisker est très complète (historique, poids, niveau du tiroir et de la litière). PetKit fait presque aussi bien et a l’avantage de regrouper fontaine et distributeur de la marque. Pour plusieurs chats, la reconnaissance par le poids fonctionne mieux s’ils ont des poids bien différents.</p>
<h2>Consommables</h2>
<p>Selon l’assistance Whisker, le Litter-Robot 4 accepte des sacs-poubelle standards de taille adaptée. PetKit propose ses propres sacs et cartouches désodorisantes. Faites le calcul sur deux ou trois ans avant de décider.</p>
<div class="duo"><div class="pick"><h3>Litter-Robot 4</h3><p>Pour : grands chats, multi-chats, suivi détaillé.</p>{amz("Litter-Robot 4")}</div>
<div class="pick"><h3>PetKit Pura Max 2</h3><p>Pour : chat moyen, peu de hauteur disponible, budget plus serré, écosystème PetKit.</p>{amz("PetKit Pura Max 2")}</div></div>
<h2>Verdict</h2>
<p>Budget et grand chat : <strong>Litter-Robot 4</strong>. Appartement compact et chat de taille moyenne : <strong>PetKit Pura Max 2</strong>. Pour d’autres options, voyez notre <a href="meilleure-litiere-automatique-2026.html">sélection des meilleures litières automatiques 2026</a>.</p>''')

# ---------- 6 caméra
page("camera-surveillance-chat-appartement.html",
 "Caméra de surveillance pour chat en appartement : guide 2026",
 "Quelle caméra pour surveiller son chat en appartement en 2026 ? Caméra motorisée, vision nocturne, stockage local ou cloud, distributeur de friandises, vie privée.",
 "Caméra de surveillance pour chat d’appartement : comment choisir en 2026",
 f'''<p class="lead">Voir son chat dans la journée, vérifier qu’il a mangé, qu’il n’est pas resté coincé dans un placard ou qu’il ne s’attaque pas aux rideaux : une caméra intérieure rassure beaucoup de propriétaires. Les modèles « spécial animaux » existent, mais une bonne caméra domestique suffit souvent. Voici comment choisir sans payer pour des fonctions inutiles.</p>
<h2>Les critères qui comptent</h2>
<ul>
<li><strong>Champ de vision</strong> : un chat bouge partout. Une caméra <em>motorisée</em> (rotation horizontale et verticale, souvent appelée « pan/tilt ») couvre une pièce entière depuis un seul point ; une caméra fixe grand angle convient à un studio.</li>
<li><strong>Vision nocturne</strong> : indispensable si vous regardez le soir ou si la pièce est sombre en hiver.</li>
<li><strong>Stockage</strong> : carte microSD (local, sans abonnement) ou cloud (souvent payant). Pour un simple coup d’œil en direct, aucun stockage n’est nécessaire.</li>
<li><strong>Audio bidirectionnel</strong> : parler au chat amuse surtout le propriétaire ; certains chats s’en inquiètent. Testez-le en votre présence.</li>
<li><strong>Détection</strong> : la détection de mouvement ou d’animal envoie des alertes. Dans un appartement avec un chat actif, réglez la sensibilité, sinon votre téléphone vibrera toute la journée.</li>
<li><strong>Wi-Fi</strong> : beaucoup de caméras ne fonctionnent qu’en 2,4 GHz. Vérifiez la portée dans la pièce visée.</li>
</ul>
<h2>Trois familles de caméras</h2>
<div class="pick"><h3>1. Caméra intérieure motorisée « généraliste »</h3>
<p>C’est le meilleur rapport utilité/prix : des marques comme TP-Link (gamme Tapo), Xiaomi ou Eufy proposent des caméras pan/tilt avec vision nocturne et emplacement microSD. Vous pilotez l’orientation depuis l’application pour suivre le chat d’une pièce à l’autre.</p>
<p><strong>Pour qui :</strong> la plupart des appartements, budget maîtrisé, pas d’abonnement voulu.</p>{amz("caméra surveillance intérieure motorisée wifi microSD","caméras motorisées")}</div>
<div class="pick"><h3>2. Caméra pour animaux avec lanceur de friandises</h3>
<p>Furbo, Petcube et d’autres proposent des caméras qui lancent une friandise à distance. Ludique, et utile pour associer la caméra à quelque chose de positif. Attention : certaines fonctions avancées (alertes intelligentes, historique vidéo) passent par un abonnement. Lisez la fiche produit avant d’acheter.</p>
<p><strong>Pour qui :</strong> chat gourmand, propriétaire qui veut interagir et pas seulement regarder.</p>{amz("caméra chat distributeur friandises","caméras à friandises")}</div>
<div class="pick"><h3>3. Distributeur de croquettes avec caméra</h3>
<p>Un seul appareil pour nourrir et voir : la caméra est placée au-dessus du bol, donc vous voyez surtout le chat… quand il mange. Bon choix si vous vouliez de toute façon un distributeur. Détails dans notre <a href="distributeur-croquettes-connecte.html">guide des distributeurs connectés</a>.</p>{amz("distributeur croquettes chat caméra wifi","distributeurs avec caméra")}</div>
<h2>Où placer la caméra ?</h2>
<ol><li>En hauteur (étagère, haut d’un meuble), hors de portée des pattes : un chat curieux fait tomber les caméras posées au bord.</li>
<li>Orientée vers les zones de vie : arbre à chat, gamelles, fenêtre préférée. Évitez de filmer la litière en continu, peu utile.</li>
<li>Loin d’un contre-jour (fenêtre en face de l’objectif) qui rend l’image illisible en journée.</li>
<li>Câble d’alimentation protégé ou caché : certains chats mâchonnent les fils.</li></ol>
<h2>Vie privée : les bons réflexes</h2>
<p>Une caméra intérieure filme aussi les humains. Si d’autres personnes viennent chez vous (colocataire, aide-ménagère, pet-sitter), prévenez-les : filmer quelqu’un à son insu chez vous peut poser un problème juridique. Côté sécurité, changez le mot de passe par défaut, activez la double authentification du compte quand elle existe et faites les mises à jour. Le mode « confidentialité » (objectif masqué quand vous êtes à la maison) est un vrai plus.</p>
<h2>Notre avis</h2>
<p>Pour la majorité des chats d’appartement, une <strong>caméra intérieure motorisée avec microSD</strong> suffit : pas d’abonnement, une pièce entière couverte. La caméra à friandises vaut le coup si vous voulez jouer à distance. Pour un équipement complet, voyez notre <a href="budget-kit-chat-appartement-connecte.html">kit débutant chat connecté</a>.</p>''')

# ---------- 7 GPS sans abonnement
page("collier-gps-chat-sans-abonnement.html",
 "Collier GPS pour chat sans abonnement : est-ce possible ? (2026)",
 "Existe-t-il un vrai GPS pour chat sans abonnement ? Limites de l’AirTag, traceurs Bluetooth Android, localisateurs radio : ce qui marche vraiment pour un chat d’appartement.",
 "Collier GPS pour chat sans abonnement : ce qui existe vraiment",
 f'''<p class="lead">C’est la question la plus fréquente : « je veux un GPS pour mon chat, mais sans abonnement ». La réponse honnête est qu’un <strong>vrai suivi GPS à distance</strong> nécessite presque toujours un abonnement, parce que le traceur doit envoyer sa position par le réseau mobile. Il existe en revanche plusieurs alternatives sans frais mensuels, chacune avec de vraies limites. Voici comment choisir selon votre situation.</p>
<h2>Pourquoi un GPS « sans abonnement » est rare</h2>
<p>Un traceur GPS calcule sa position grâce aux satellites, mais il doit ensuite la <em>transmettre</em> à votre téléphone. Pour cela, il utilise une carte SIM et un réseau mobile, ce qui a un coût récurrent : c’est ce que couvre l’abonnement de Tractive ou de ses concurrents. Méfiez-vous des produits présentés comme « GPS sans abonnement » : il s’agit le plus souvent de traceurs Bluetooth, d’un abonnement inclus pour une durée limitée, ou d’une carte SIM à acheter et recharger vous-même.</p>
<h2>Les alternatives sans abonnement</h2>
<table><thead><tr><th>Solution</th><th>Comment ça marche</th><th>Points forts</th><th>Limites</th></tr></thead><tbody>
<tr><td>AirTag (Apple)</td><td>Bluetooth, localisé par les appareils Apple à proximité</td><td>Pas d’abonnement, grand réseau en ville</td><td>iPhone obligatoire, positions ponctuelles, non conçu pour les animaux</td></tr>
<tr><td>Traceurs « Localiser » Android (réseau Google) et Galaxy SmartTag (Samsung)</td><td>Bluetooth, localisé par les téléphones Android ou Samsung à proximité</td><td>Équivalent de l’AirTag pour Android</td><td>Mêmes limites : pas de temps réel, dépend du passage de téléphones</td></tr>
<tr><td>Localisateur radio (type Loc8tor)</td><td>Un boîtier émetteur sur le collier, un récepteur portatif qui indique la direction</td><td>Aucun réseau ni téléphone requis, utile pour fouiller un immeuble, une cave, un jardin</td><td>Portée limitée, il faut déjà être dans le secteur</td></tr>
<tr><td>Médaille avec QR code / numéro</td><td>La personne qui trouve le chat scanne ou appelle</td><td>Très léger, très bon marché</td><td>Aucune localisation : dépend d’un passant</td></tr>
</tbody></table>
<h2>Les limites de l’AirTag pour un chat</h2>
<ul>
<li><strong>Pas de suivi en direct</strong> : la position n’est mise à jour que lorsqu’un appareil Apple passe à proximité. En zone calme, dans une cave ou un local technique, elle peut rester figée longtemps.</li>
<li><strong>Précision variable</strong> : la recherche précise ne fonctionne qu’à courte distance avec un iPhone compatible.</li>
<li><strong>Alertes anti-pistage</strong> : l’AirTag est conçu pour éviter de suivre quelqu’un à son insu. Un AirTag séparé de son propriétaire peut émettre un son et déclencher une alerte chez des personnes proches, ce qui peut être déroutant pour vos voisins.</li>
<li><strong>Taille et poids</strong> : sur un petit chat, l’AirTag dans son support reste un objet volumineux au cou. Choisissez un support plat et léger.</li>
<li><strong>Usage non prévu</strong> : Apple présente l’AirTag pour des objets, pas pour des animaux.</li>
</ul>
{amz("Apple AirTag","AirTag")} {amz("porte AirTag collier chat sécurité","porte-AirTag")}
<h2>Les alternatives pour Android</h2>
<p>Si vous êtes sur Android, regardez les traceurs compatibles avec le réseau « Localiser » de Google (plusieurs marques comme Chipolo ou Pebblebee en proposent) ou, si vous avez un téléphone Samsung, le Galaxy SmartTag. Le principe et les limites sont les mêmes que pour l’AirTag : utile en ville, pas de suivi en temps réel. Vérifiez la compatibilité exacte avec votre téléphone avant d’acheter.</p>
{amz("traceur Bluetooth compatible Google Localiser","traceurs Android")} {amz("Samsung Galaxy SmartTag2","Galaxy SmartTag")}
<h2>Le localisateur radio : sous-estimé pour un chat d’intérieur</h2>
<p>La plupart des chats d’appartement qui « disparaissent » ne vont pas loin : ils se cachent dans la cage d’escalier, une cave, un local poubelle ou chez un voisin. Dans ces cas, un localisateur radio qui indique la direction par un signal sonore ou lumineux est souvent plus efficace qu’un AirTag, puisqu’il ne dépend d’aucun téléphone ni réseau. Sa portée reste limitée : c’est un outil de recherche de proximité, pas un suivi à distance.</p>
{amz("localisateur radio chat Loc8tor","localisateurs radio")}
<h2>Et si votre chat sort vraiment ?</h2>
<p>Si votre chat a accès à l’extérieur, a déjà fugué ou vit près d’une zone dangereuse (route, chantier), un vrai traceur GPS avec abonnement reste la seule solution qui suit en temps réel. Notre comparatif <a href="gps-chat-tractive-vs-airtag.html">Tractive vs AirTag</a> détaille ce choix.</p>
<h2>Les indispensables, quel que soit le traceur</h2>
<ul>
<li><strong>Identification</strong> : en France, l’identification (puce électronique ou tatouage) est obligatoire pour les chats de plus de 7 mois nés après le 1<sup>er</sup> janvier 2012. C’est votre meilleure chance de récupérer un chat trouvé. Vérifiez que vos coordonnées sont à jour au fichier I-CAD.</li>
<li><strong>Collier à ouverture de sécurité</strong> : il doit se détacher sous la traction pour éviter l’étranglement.</li>
<li><strong>Prévention</strong> : un filet de balcon ou des moustiquaires renforcées évitent plus de fugues qu’aucun traceur.</li>
</ul>
<h2>Notre avis</h2>
<p>Pour un <strong>chat strictement d’intérieur</strong>, sans abonnement : un traceur Bluetooth adapté à votre téléphone (AirTag ou équivalent Android) <em>plus</em> une identification à jour, éventuellement complétés d’un localisateur radio pour fouiller l’immeuble. Pour un <strong>chat qui sort</strong>, acceptez l’abonnement d’un vrai GPS.</p>''')

# ---------- 8 litière petit appart
page("litiere-automatique-petit-appartement.html",
 "Litière automatique pour petit appartement : bruit, taille, odeurs (2026)",
 "Litière automatique dans un studio ou petit appartement : quel modèle compact, quel niveau de bruit, où la placer et comment limiter les odeurs. Nos conseils 2026.",
 "Litière automatique en petit appartement : bruit, taille et odeurs",
 f'''<p class="lead">Dans un studio ou un deux-pièces, la litière est souvent à quelques mètres du lit ou du canapé. Une litière automatique peut nettement améliorer l’odeur, mais elle prend de la place et fait du bruit à chaque cycle. Ce guide se concentre sur ces trois contraintes. Pour une sélection générale, voyez notre <a href="meilleure-litiere-automatique-2026.html">guide des meilleures litières automatiques 2026</a>.</p>
<h2>1. La taille : mesurez avant tout</h2>
<p>Les litières automatiques sont beaucoup plus grandes qu’un bac classique. Avant d’acheter, mesurez :</p>
<ul>
<li><strong>la hauteur disponible</strong> (sous une fenêtre, un plan de travail, une étagère) ;</li>
<li><strong>la profondeur</strong>, plus la place pour sortir le tiroir à déchets ;</li>
<li><strong>l’espace devant l’entrée</strong>, pour que le chat puisse entrer sans se contorsionner ;</li>
<li><strong>une prise électrique</strong> à proximité, sans rallonge qui traîne au sol.</li>
</ul>
<p>Pour donner un ordre d’idée d’après les manuels des fabricants, la PetKit Pura Max 2 mesure environ 55 cm de haut, contre environ 75 cm pour le Litter-Robot 4. Dans un petit logement, les modèles bas ou à toit ouvert se logent plus facilement.</p>
<h2>2. Le bruit : à quoi s’attendre</h2>
<p>Toutes les litières automatiques font du bruit pendant le cycle de nettoyage (rotation du globe, déplacement d’un râteau ou d’un tapis). Les fabricants publient rarement des mesures comparables, donc méfiez-vous des chiffres non sourcés. Ce qui compte en pratique :</p>
<ul>
<li><strong>Le délai avant nettoyage</strong> : la plupart des applications permettent de régler l’attente après le passage du chat. Un délai plus long évite de surprendre le chat et regroupe les cycles.</li>
<li><strong>Le mode nuit ou « ne pas déranger »</strong> : plusieurs modèles (dont le Litter-Robot 4 et les litières PetKit, selon leurs applications) permettent de suspendre les cycles automatiques sur une plage horaire. Indispensable si la litière est près de la chambre.</li>
<li><strong>Le sol</strong> : posée sur un sol dur et stable, la litière vibre moins. Évitez les tapis épais, qui perturbent aussi les capteurs de poids.</li>
</ul>
<h2>3. Les odeurs : l’automatique ne fait pas tout</h2>
<ul>
<li><strong>Videz le tiroir régulièrement</strong>, sans attendre qu’il soit plein : c’est lui qui sent, pas le globe.</li>
<li><strong>Choisissez une bonne litière agglomérante</strong> compatible avec votre modèle : des agglomérats qui s’effritent laissent des résidus et des odeurs.</li>
<li><strong>Nettoyez à fond</strong> l’appareil selon la notice (souvent toutes les quelques semaines), car l’urine finit par imprégner les parois.</li>
<li><strong>Aérez la pièce</strong> et évitez les placards fermés sans ventilation.</li>
<li><strong>Prudence avec les parfums</strong> : les chats ont l’odorat très sensible ; un désodorisant trop parfumé peut les détourner de la litière.</li>
</ul>
<h2>Modèles à considérer pour un petit espace</h2>
<div class="pick"><h3>PetKit Pura Max 2 — compacte en hauteur</h3>
<p>Plus basse que la plupart des globes, avec désodorisant intégré et mode « ne pas déranger » dans l’application. Son entrée est plus étroite : à vérifier pour un grand chat.</p>{amz("PetKit Pura Max 2")}</div>
<div class="pick"><h3>Litières automatiques à toit ouvert</h3>
<p>Certains modèles récents (Neakasa M1 par exemple) n’ont pas de toit : ils paraissent moins imposants et conviennent aux chats qui refusent les espaces fermés. En contrepartie, les projections de litière sont moins contenues. Vérifiez les dimensions, le poids minimum du chat et le type de litière accepté.</p>{amz("litière automatique chat ouverte sans toit","modèles ouverts")}</div>
<div class="pick"><h3>Litter-Robot 4 — si vous avez la hauteur</h3>
<p>Référence pour les grands chats et les foyers multi-chats, mais haute : réservée aux appartements où un emplacement d’environ 75 cm de hauteur est disponible. Comparaison complète dans notre duel <a href="litter-robot-4-vs-petkit-pura-max-2.html">Litter-Robot 4 vs PetKit</a>.</p>{amz("Litter-Robot 4")}</div>
<h2>Où placer la litière dans un petit logement ?</h2>
<ol><li><strong>Salle de bain</strong> : souvent le meilleur choix (sol dur, ventilation), si la porte reste accessible au chat.</li>
<li><strong>Entrée ou couloir</strong> : bien si une prise est proche et que le passage n’est pas trop fréquent.</li>
<li><strong>À éviter</strong> : à côté des gamelles ou de la fontaine, dans un placard sans aération, ou au pied du lit.</li></ol>
<h2>Notre avis</h2>
<p>Dans un petit appartement, privilégiez un <strong>modèle bas avec mode nuit</strong>, posé sur un sol dur dans une pièce ventilée, et videz le tiroir avant qu’il soit plein. Si la hauteur manque vraiment ou si votre chat n’est pas prêt, un bac classique bien entretenu reste une solution honnête.</p>
<p class="note">Un chat qui se met soudain à éviter sa litière ou à y aller beaucoup plus souvent doit être vu par un vétérinaire.</p>''')

# ---------- 9 budget kit
page("budget-kit-chat-appartement-connecte.html",
 "Équiper son chat d’appartement en connecté : budget et kit débutant 2026",
 "Par quoi commencer pour équiper un chat d’appartement en objets connectés ? Kit débutant, priorités par budget, ce qui est utile et ce qui ne l’est pas.",
 "Budget : équiper un chat d’appartement en connecté (kit débutant)",
 f'''<p class="lead">Fontaine, distributeur, caméra, litière automatique, GPS… Tout acheter d’un coup coûte cher et n’est pas nécessaire. Ce guide vous aide à prioriser selon votre mode de vie et votre budget, en commençant par ce qui apporte le plus au chat. Nous n’affichons pas de prix précis, car ils changent souvent : vérifiez-les sur la page du vendeur.</p>
<h2>La règle : d’abord le chat, ensuite les gadgets</h2>
<p>Avant tout objet connecté, un chat d’intérieur a besoin d’un arbre à chat ou d’espaces en hauteur, de griffoirs, de jeux quotidiens avec vous et d’une litière propre. Le connecté vient <em>en plus</em>, pour vous faciliter la vie quand vous êtes absent.</p>
<h2>Niveau 1 — Kit débutant (petit budget)</h2>
<p>Les deux objets qui ont l’impact le plus direct sur le quotidien du chat :</p>
<div class="pick"><h3>Une fontaine à eau</h3><p>Elle incite beaucoup de chats à boire davantage. Un modèle simple non connecté suffit pour commencer ; la version connectée ajoute des alertes de niveau d’eau. Voir notre <a href="meilleure-fontaine-eau-chat-2026.html">guide des fontaines</a>.</p>{amz("fontaine à eau chat pompe sans fil","fontaines")}</div>
<div class="pick"><h3>Un distributeur de croquettes programmable</h3><p>Pour des repas réguliers en petites portions, même quand vous rentrez tard. Prenez un modèle avec batterie de secours. Voir notre <a href="distributeur-croquettes-connecte.html">guide des distributeurs</a>.</p>{amz("distributeur croquettes chat programmable wifi","distributeurs")}</div>
<h2>Niveau 2 — Confort (budget moyen)</h2>
<p>Ajoutez de quoi garder un œil sur le chat et le retrouver :</p>
<div class="pick"><h3>Une caméra intérieure</h3><p>Une caméra motorisée avec carte microSD, sans abonnement, couvre l’essentiel. Voir notre <a href="camera-surveillance-chat-appartement.html">guide des caméras pour chat</a>.</p>{amz("caméra surveillance intérieure motorisée wifi microSD","caméras")}</div>
<div class="pick"><h3>Un traceur sans abonnement</h3><p>Un AirTag ou un équivalent Android sur un collier de sécurité sert de filet de sécurité pour un chat d’intérieur. Voir <a href="collier-gps-chat-sans-abonnement.html">GPS chat sans abonnement</a>.</p>{amz("porte AirTag collier chat sécurité","porte-AirTag")}</div>
<h2>Niveau 3 — Équipement complet (gros budget)</h2>
<div class="pick"><h3>Une litière automatique</h3><p>C’est l’investissement le plus lourd, et celui qui change le plus le quotidien en appartement (odeurs, corvée). À réserver quand le reste est en place et que vous avez mesuré l’emplacement. Voir notre <a href="meilleure-litiere-automatique-2026.html">sélection 2026</a> et notre guide <a href="litiere-automatique-petit-appartement.html">litière auto en petit appartement</a>.</p>{amz("litière automatique autonettoyante chat","litières automatiques")}</div>
<div class="pick"><h3>Un vrai GPS avec abonnement</h3><p>Seulement si votre chat sort ou a déjà fugué. Comparez dans <a href="gps-chat-tractive-vs-airtag.html">Tractive vs AirTag</a>.</p>{amz("Tractive GPS chat CAT 6 Mini")}{secondary("tractive","https://tractive.com/fr")}</div>
<h2>Kit par profil</h2>
<table><thead><tr><th>Votre situation</th><th>Priorité</th><th>Ensuite</th></tr></thead><tbody>
<tr><td>Longues journées de travail</td><td>Distributeur + fontaine</td><td>Caméra</td></tr>
<tr><td>Studio, odeurs de litière</td><td>Litière automatique compacte</td><td>Fontaine</td></tr>
<tr><td>Week-ends fréquents à l’extérieur</td><td>Distributeur avec batterie + fontaine grande capacité</td><td>Caméra, et quelqu’un qui passe</td></tr>
<tr><td>Balcon ou chat fugueur</td><td>Filet de balcon + identification à jour</td><td>Traceur (Bluetooth ou GPS)</td></tr>
<tr><td>Premier chat, budget serré</td><td>Fontaine simple</td><td>Distributeur programmable</td></tr>
</tbody></table>
<h2>Économiser intelligemment</h2>
<ul>
<li><strong>Restez dans un seul écosystème</strong> (par exemple PetKit ou Xiaomi) : une seule application, et souvent des promotions groupées.</li>
<li><strong>Calculez le coût d’usage</strong> : filtres de fontaine, sacs et désodorisants de litière, abonnement GPS ou cloud caméra. Sur deux ou trois ans, il peut dépasser le prix d’achat.</li>
<li><strong>Évitez les abonnements inutiles</strong> : préférez une caméra avec stockage local et ne payez un abonnement GPS que si le chat sort.</li>
<li><strong>Surveillez les grandes périodes de promotions</strong> (Black Friday, Prime Day, soldes) pour les achats les plus chers comme la litière automatique.</li>
</ul>
<h2>Ce qui est rarement utile</h2>
<p>Les jouets laser automatiques peuvent frustrer certains chats (une proie qu’on n’attrape jamais) : terminez toujours une séance par un jouet qu’il peut attraper. Les colliers « d’activité » sans localisation intéressent surtout les curieux. Et aucun objet ne remplace une visite quand vous partez plus d’un week-end.</p>
<h2>Notre avis</h2>
<p>Commencez par une <strong>fontaine</strong> et un <strong>distributeur programmable</strong>, ajoutez une <strong>caméra sans abonnement</strong> si vous êtes souvent absent, et gardez la <strong>litière automatique</strong> pour quand vous serez sûr de votre emplacement et de votre budget.</p>''')

# ---------- 10 top 5
page("top-5-equipements-chat-appartement-2026.html",
 "Top 5 équipements chat d’appartement 2026 : l’essentiel connecté",
 "Les 5 équipements connectés les plus utiles pour un chat d’appartement en 2026 : litière automatique, fontaine, distributeur, GPS Tractive, caméra. Critères et pour qui.",
 "Top 5 équipements chat d’appartement 2026",
 f'''<p class="lead">Un chat d’intérieur dépend entièrement de ce que vous mettez à sa disposition. Parmi tous les objets connectés du marché, cinq familles apportent un vrai bénéfice en appartement. Voici, pour chacune, les critères à vérifier, pour qui elle vaut le coup, et le guide détaillé à lire avant d’acheter. Nous n’affichons pas de prix : ils changent souvent, vérifiez-les sur la page du vendeur.</p>
<h2>En résumé</h2>
<table><thead><tr><th>Équipement</th><th>Utile surtout si…</th><th>Priorité</th></tr></thead><tbody>
<tr><td>Fontaine à eau</td><td>votre chat boit peu ou mange des croquettes</td><td>Haute, petit budget</td></tr>
<tr><td>Distributeur de croquettes</td><td>vous rentrez tard ou le chat réclame tôt</td><td>Haute</td></tr>
<tr><td>Litière automatique</td><td>les odeurs gênent dans un petit logement</td><td>Moyenne, gros budget</td></tr>
<tr><td>Caméra intérieure</td><td>vous êtes souvent absent et voulez vérifier</td><td>Confort</td></tr>
<tr><td>GPS / traceur</td><td>balcon, fugue passée, chat qui sort</td><td>Selon le chat</td></tr>
</tbody></table>
<div class="pick"><h3>1. Litière automatique</h3>
<p><strong>Ce qu’elle apporte :</strong> les déchets sont tamisés et stockés dans un tiroir fermé après chaque passage. En studio, c’est le meilleur levier contre les odeurs.</p>
<p><strong>Critères :</strong> poids minimum du chat (pas de chaton), hauteur et place pour sortir le tiroir, litière agglomérante compatible, capteurs de sécurité, mode nuit, coût des sacs et filtres sur 2–3 ans, Wi-Fi 2,4 GHz.</p>
<p><strong>Pour qui :</strong> chat adulte, logement où la litière est proche des pièces de vie, budget confortable. À éviter si le chat est très craintif ou si l’emplacement n’est pas mesuré.</p>
<p>À lire : <a href="meilleure-litiere-automatique-2026.html">meilleures litières automatiques 2026</a>, <a href="litiere-automatique-petit-appartement.html">litière auto en petit appartement</a> et le duel <a href="litter-robot-4-vs-petkit-pura-max-2.html">Litter-Robot 4 vs PetKit</a>.</p>
{amz("litière automatique autonettoyante chat","litières automatiques")}</div>
<div class="pick"><h3>2. Fontaine à eau</h3>
<p><strong>Ce qu’elle apporte :</strong> une eau qui circule et filtrée incite beaucoup de chats à boire davantage.</p>
<p><strong>Critères :</strong> pompe sans fil (plus facile à nettoyer), bruit léger, 1,5 à 3 L pour un chat, inox ou céramique, filtres de rechange faciles à trouver. La connexion (alerte niveau d’eau) est un bonus.</p>
<p><strong>Pour qui :</strong> presque tous les chats d’appartement, surtout ceux nourris aux croquettes. C’est l’achat le plus rentable pour commencer.</p>
<p>À lire : <a href="meilleure-fontaine-eau-chat-2026.html">meilleure fontaine à eau pour chat 2026</a>.</p>
{amz("fontaine à eau chat pompe sans fil","fontaines")}</div>
<div class="pick"><h3>3. Distributeur de croquettes connecté</h3>
<p><strong>Ce qu’il apporte :</strong> des petits repas à heures fixes, même quand vous rentrez tard, et des alertes en cas de bourrage ou de réservoir bas.</p>
<p><strong>Critères :</strong> batterie ou piles de secours, programme qui continue sans Wi-Fi, réservoir hermétique, bol inox amovible, taille de croquettes acceptée, deux bols si plusieurs chats.</p>
<p><strong>Pour qui :</strong> longues journées de travail, chat qui réclame à l’aube, week-ends ponctuels (avec quelqu’un qui passe au-delà).</p>
<p>À lire : <a href="distributeur-croquettes-connecte.html">bien choisir un distributeur connecté</a>.</p>
{amz("distributeur croquettes chat programmable wifi","distributeurs")}</div>
<div class="pick"><h3>4. GPS pour chat (Tractive) ou traceur</h3>
<p><strong>Ce qu’il apporte :</strong> retrouver un chat qui a fugué. Un vrai GPS comme Tractive suit en temps réel via le réseau mobile (abonnement obligatoire) ; un AirTag ou un traceur Bluetooth sert de filet de sécurité sans abonnement, sans suivi continu.</p>
<p><strong>Critères :</strong> temps réel ou non, abonnement, autonomie, poids adapté au gabarit du chat, collier à ouverture de sécurité, compatibilité iPhone/Android.</p>
<p><strong>Pour qui :</strong> chat avec accès au balcon ou à l’extérieur, ou qui a déjà fugué : GPS. Chat strictement d’intérieur : traceur sans abonnement + identification à jour.</p>
<p>À lire : <a href="gps-chat-tractive-vs-airtag.html">Tractive ou AirTag</a> et <a href="collier-gps-chat-sans-abonnement.html">GPS chat sans abonnement</a>.</p>
{amz("Tractive GPS chat CAT 6 Mini")}{secondary("tractive","https://tractive.com/fr")}</div>
<div class="pick"><h3>5. Caméra intérieure</h3>
<p><strong>Ce qu’elle apporte :</strong> vérifier en journée que le chat va bien, a mangé ou n’est pas resté enfermé.</p>
<p><strong>Critères :</strong> motorisée (pan/tilt) pour couvrir une pièce, vision nocturne, stockage microSD sans abonnement, détection réglable, sécurité du compte (mot de passe, double authentification), mode confidentialité.</p>
<p><strong>Pour qui :</strong> propriétaires souvent absents qui veulent être rassurés. Les modèles à lanceur de friandises plaisent aux chats gourmands.</p>
<p>À lire : <a href="camera-surveillance-chat-appartement.html">caméra de surveillance pour chat</a>.</p>
{amz("caméra surveillance intérieure motorisée wifi microSD","caméras")}</div>
<h2>Par quoi commencer ?</h2>
<ol><li><strong>Fontaine</strong> et <strong>distributeur</strong> : impact direct sur le quotidien du chat, budget limité.</li>
<li><strong>Caméra</strong> si vous êtes souvent absent ; <strong>traceur</strong> si le chat a accès au balcon.</li>
<li><strong>Litière automatique</strong> quand l’emplacement est mesuré et le budget prêt.</li></ol>
<p>Pour un plan par budget et par profil, voyez notre <a href="budget-kit-chat-appartement-connecte.html">kit débutant chat connecté</a>.</p>
<p class="note">Aucun appareil ne remplace votre présence, des jeux quotidiens ni l’avis d’un vétérinaire. Un changement soudain de consommation d’eau, d’appétit ou de passages à la litière doit être signalé au vétérinaire.</p>''')

# ---------- guide payant
page("guide.html",
 "Chat d’appartement connecté : le plan en 7 jours – guide PDF 12 €",
 "Le plan en 7 jours pour équiper votre chat d’appartement (litière, eau, repas, sécurité, budget) sans tout acheter d’un coup. Guide numérique à 12 €.",
 PRODUCT,
 f'''<p class="paid-label"><strong>Produit payant</strong> — guide numérique vendu {PRICE} via Gumroad. Cette page n’est pas un lien d’affiliation.</p>
<p class="lead">En 7 jours, équipez votre chat d’appart (litière, eau, repas, sécurité, budget) sans tout acheter d’un coup.</p>
<p>Nos guides gratuits comparent les appareils un par un. Ce plan les remet <strong>dans l’ordre</strong> : une étape par jour, environ 20 à 45 minutes, pour observer d’abord, acheter ensuite et installer progressivement. Vous pouvez aussi l’étaler sur deux semaines.</p>
<h2>Ce que contient le plan</h2>
<ol>
<li><strong>Jour 1 — L’audit des besoins</strong> : votre logement, votre rythme, votre chat.</li>
<li><strong>Jour 2 — La litière</strong> : bac classique ou automatique, et où la placer.</li>
<li><strong>Jour 3 — L’eau</strong> : fontaine ou non, et comment la faire adopter.</li>
<li><strong>Jour 4 — Les repas</strong> : distributeur programmable, portions, absences.</li>
<li><strong>Jour 5 — Sécurité, caméra et GPS</strong> : ce qui est utile selon votre chat.</li>
<li><strong>Jour 6 — Le budget</strong> : trois scénarios (50 €, 200 € ou 500 €).</li>
<li><strong>Jour 7 — Installation, tests et checklist finale</strong>.</li>
</ol>
<p>En plus : les erreurs à éviter, une <strong>checklist imprimable</strong> et un <strong>tableau budget à remplir</strong>.</p>
<h2>Pour qui ?</h2>
<ul><li>Vous vivez en appartement ou en studio avec un ou deux chats d’intérieur.</li>
<li>Vous débutez avec les applis et le Wi-Fi et voulez des explications simples.</li>
<li>Vous voulez dépenser au bon endroit plutôt que tout acheter d’un coup.</li></ul>
<p class="note">Ce n’est pas un comparatif exhaustif de tous les modèles, ni un avis vétérinaire. Aucun appareil ne remplace votre présence ou un pet-sitter pour une longue absence. Les prix sont donnés en fourchettes indicatives.</p>
<div class="paid-cta"><p><strong>{PRODUCT}</strong><br>Guide numérique (PDF) — <strong>{PRICE}</strong></p>
<p><a class="btn-paid" href="{GUMROAD}" target="_blank" rel="noopener">Acheter le plan sur Gumroad – {PRICE}</a></p>
<p class="note">Paiement et livraison du fichier gérés par Gumroad. Prix TTC affiché sur Gumroad au moment de l’achat.</p></div>
<h2>Guide payant ou liens d’affiliation : quelle différence ?</h2>
<ul><li><strong>Ce guide</strong> est un produit payant édité par Chat Appartement Connecté et vendu séparément via Gumroad. En l’achetant, vous payez directement ce contenu.</li>
<li><strong>Les boutons « Voir sur Amazon »</strong> de nos autres pages sont des liens d’affiliation : en tant que Partenaire Amazon, nous réalisons un bénéfice sur les achats remplissant les conditions requises, sans surcoût pour vous. Amazon ne vend pas ce guide.</li></ul>
<p>Plus de détails sur notre page <a href="affiliation.html">affiliation &amp; mentions légales</a>. Vous préférez commencer gratuitement ? Lisez notre <a href="budget-kit-chat-appartement-connecte.html">kit débutant et budget</a>.</p>
<p class="note">Version courte : la <a href="checklist.html">checklist shopping du chat connecté</a> (quoi acheter, quoi éviter, combien prévoir) — produit payant, 6,90 € via Gumroad.</p>''',related=False)

# ---------- lead magnet gratuit
ML_HEAD='''<script>
    (function(w,d,e,u,f,l,n){w[f]=w[f]||function(){(w[f].q=w[f].q||[])
    .push(arguments);},l=d.createElement(e),l.async=1,l.src=u,
    n=d.getElementsByTagName(e)[0],n.parentNode.insertBefore(l,n);})
    (window,document,'script','https://assets.mailerlite.com/js/universal.js','ml');
    ml('account', '2748139');
</script>
'''
ML_FORM='<div class="ml-embedded" data-form="Um0Zqt"></div>'
page("telechargement-audit.html",
 "Audit gratuit en 1 jour : ce dont votre chat d’appartement a vraiment besoin",
 "Checklist gratuite d’une page : en une journée, découvrez ce dont votre chat d’appartement a besoin et ce qu’il est inutile d’acheter.",
 "L’audit gratuit en 1 jour",
 f'''<p class="paid-label"><strong>Gratuit</strong> — checklist PDF. Cette page ne contient pas de lien d’affiliation.</p>
<p class="lead">En une journée et une seule page à cocher, découvrez ce dont votre chat d’appartement a vraiment besoin — et surtout ce qu’il est inutile d’acheter.</p>
<p>Observez votre chat, votre logement et votre rythme, cochez, puis ne dépensez qu’au bon endroit. Comptez environ une heure d’observation répartie sur la journée.</p>
<h2>Ce que contient l’audit</h2>
<ul><li>Une checklist d’une page : litière, eau, repas, activité, sécurité, absences.</li>
<li>Un mini guide pour lire vos résultats, savoir quoi prioriser… et ce qu’il est souvent inutile d’acheter.</li></ul>
<h2>Recevoir l’audit par email</h2>
<p>Laissez votre email : on vous envoie le PDF et quelques conseils pour équiper votre chat d’appart (désinscription en 1 clic, votre email n’est ni vendu ni partagé).</p>
{ML_FORM}
<p class="note">Vous préférez sans inscription ? <a href="produits/lead-magnet-audit-1-jour.pdf" download>Télécharger le PDF directement</a> · <a href="produits/lead-magnet-audit-1-jour.html">Lire en ligne</a>.</p>
<h2>Et ensuite ?</h2>
<p>Une fois l’audit fait, le <a href="guide.html">plan en 7 jours</a> vous guide étape par étape (litière, eau, repas, sécurité, budget). <a href="{GUMROAD}" target="_blank" rel="noopener">Voir le guide sur Gumroad ({PRICE})</a> — produit payant, pas un lien d’affiliation. Ou commencez par notre <a href="budget-kit-chat-appartement-connecte.html">kit débutant gratuit</a>.</p>''',related=False,head_extra=ML_HEAD)

# ---------- affiliation
page("affiliation.html",
 "Affiliation et mentions légales – Chat Appartement Connecté",
 "Mentions légales, politique d’affiliation (Partenaire Amazon) et confidentialité du site Chat Appartement Connecté.",
 "Affiliation, mentions légales et confidentialité",
 '''<h2>Liens affiliés</h2>
<p>Ce site contient des liens affiliés, signalés par les boutons « Voir sur Amazon ». <strong>En tant que Partenaire Amazon, nous réalisons un bénéfice sur les achats remplissant les conditions requises.</strong> Si vous achetez après avoir cliqué, nous pouvons percevoir une commission, sans surcoût pour vous. Cette rémunération n’influence pas nos recommandations ; les marques citées ne nous ont pas payés pour apparaître.</p>
<p>Les prix, disponibilités et caractéristiques sont susceptibles d’évoluer : la page du vendeur fait foi au moment de l’achat.</p>
<h2>Produit payant</h2>
<p>Le guide « Chat d’appartement connecté : le plan en 7 jours » est un produit numérique payant, édité par Chat Appartement Connecté et vendu séparément via Gumroad (voir la <a href="guide.html">page du guide</a>). Les liens vers Gumroad ne sont pas des liens d’affiliation : ils mènent à notre propre produit.</p>
<h2>Réseaux à venir (Awin / Zooplus / Tractive)</h2>
<p>Nous prévoyons d’ajouter des liens d’affiliation vers <strong>Zooplus</strong> et <strong>Tractive</strong>, via le réseau <strong>Awin</strong> ou le programme partenaire de Tractive. <strong>Ces partenariats ne sont pas encore actifs</strong> : aucun lien de ce type n’est présent sur le site à ce jour. Lorsqu’ils le seront, les boutons concernés (« Voir chez Zooplus », « Voir chez Tractive ») seront signalés comme liens affiliés, avec la même règle : commission éventuelle, sans surcoût pour vous, sans influence sur nos recommandations.</p>
<h2>Éditeur</h2>
<p>Site édité à titre personnel par la responsable de publication du projet Chat Appartement Connecté. Contact : via le dépôt GitHub du projet.</p>
<h2>Hébergement</h2>
<p>GitHub Pages — GitHub, Inc., 88 Colin P. Kelly Jr. Street, San Francisco, CA 94107, États-Unis.</p>
<h2>Contenu</h2>
<p>Les guides sont fournis à titre informatif et ne constituent pas un avis vétérinaire. En cas de doute sur la santé de votre chat, consultez un vétérinaire.</p>
<h2>Confidentialité et cookies</h2>
<p>Ce site ne dépose pas de cookie publicitaire et n’utilise pas d’outil de mesure d’audience. En cliquant sur un lien Amazon, vous êtes soumis à la politique de confidentialité d’Amazon, qui peut utiliser des cookies pour attribuer la commission.</p>''',related=False)

page("checklist.html",
 "Checklist shopping du chat connecté – PDF 6,90 €",
 "Quoi acheter, quoi éviter, combien prévoir : litière automatique, fontaine, distributeur, GPS. Checklist numérique à 6,90 €.",
 "Checklist shopping du chat connecté",
 f'''<p class="paid-label"><strong>Produit payant</strong> — checklist numérique vendue 6,90 € via Gumroad. Cette page n’est pas un lien d’affiliation.</p>
<p class="lead">Quoi acheter, quoi éviter, combien prévoir — litière auto, fontaine, distributeur, GPS.</p>
<p>Avant de passer commande, une checklist courte pour vérifier chaque appareil : est-il adapté à votre chat et à votre appartement, quels pièges éviter, et quel budget réaliste prévoir.</p>
<h2>Ce que contient la checklist</h2>
<ul>
<li><strong>Litière automatique</strong> : critères d’encombrement, bruit, poids minimal du chat, coût des consommables.</li>
<li><strong>Fontaine à eau</strong> : capacité, entretien, filtres, bruit de pompe.</li>
<li><strong>Distributeur de croquettes</strong> : programmation, secours en cas de coupure Wi-Fi, taille des croquettes.</li>
<li><strong>GPS / traceur</strong> : abonnement ou non, autonomie, poids du collier.</li>
<li><strong>Les erreurs à éviter</strong> et des <strong>fourchettes de budget</strong> par appareil.</li>
</ul>
<p class="note">Fourchettes de prix indicatives. Ni comparatif exhaustif, ni avis vétérinaire.</p>
<div class="paid-cta"><p><strong>Checklist shopping du chat connecté</strong><br>Checklist numérique (PDF) — <strong>6,90 €</strong></p>
<p><a class="btn-paid" href="{CHECKLIST_GUMROAD}" target="_blank" rel="noopener">Acheter la checklist sur Gumroad – 6,90 €</a></p>
<p class="note">Paiement et livraison du fichier gérés par Gumroad. Prix TTC affiché sur Gumroad au moment de l’achat.</p></div>
<h2>Envie d’aller plus loin ?</h2>
<p>Pour tout mettre en place étape par étape (audit, litière, eau, repas, sécurité, budget), voyez le <a href="guide.html">plan en 7 jours</a> — guide PDF à 12 € (<a href="{GUMROAD}" target="_blank" rel="noopener">sur Gumroad</a>).</p>
<h2>Produit payant ou liens d’affiliation ?</h2>
<ul><li><strong>Cette checklist</strong> est un produit payant édité par Chat Appartement Connecté et vendu via Gumroad. Ce n’est pas de l’affiliation.</li>
<li><strong>Les boutons « Voir sur Amazon »</strong> de nos autres pages sont des liens d’affiliation : en tant que Partenaire Amazon, nous réalisons un bénéfice sur les achats remplissant les conditions requises, sans surcoût pour vous.</li></ul>
<p>Détails : <a href="affiliation.html">affiliation &amp; mentions légales</a>. Pour commencer gratuitement : <a href="telechargement-audit.html">audit gratuit (PDF)</a>.</p>''',related=False)

urls=["","top-5-equipements-chat-appartement-2026.html","meilleure-litiere-automatique-2026.html","gps-chat-tractive-vs-airtag.html","meilleure-fontaine-eau-chat-2026.html","distributeur-croquettes-connecte.html","litter-robot-4-vs-petkit-pura-max-2.html","camera-surveillance-chat-appartement.html","collier-gps-chat-sans-abonnement.html","litiere-automatique-petit-appartement.html","budget-kit-chat-appartement-connecte.html","guide.html","telechargement-audit.html","checklist.html","affiliation.html"]
open("sitemap.xml","w").write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'+"".join(f"  <url><loc>{BASE}{u}</loc><lastmod>{TODAY}</lastmod></url>\n" for u in urls)+"</urlset>\n")
open("robots.txt","w").write(f"User-agent: *\nAllow: /\nSitemap: {BASE}sitemap.xml\n")
