import urllib.parse, datetime
BASE="https://caro123-create.github.io/chat-appartement-connecte/"
TAG="rappelalertes-21"
SITE="Chat Appartement Connecté"
TODAY="2026-10-27"
def amz(q,label=None):
    u="https://www.amazon.fr/s?k="+urllib.parse.quote_plus(q)+"&tag="+TAG
    return f'<a class="btn" href="{u}" rel="sponsored nofollow noopener" target="_blank">Voir sur Amazon{(" – "+label) if label else ""}</a>'
NAV=[("meilleure-litiere-automatique-2026.html","Litière automatique"),
     ("gps-chat-tractive-vs-airtag.html","GPS chat"),
     ("meilleure-fontaine-eau-chat-2026.html","Fontaine à eau"),
     ("distributeur-croquettes-connecte.html","Distributeur connecté"),
     ("litter-robot-4-vs-petkit-pura-max-2.html","Litter-Robot 4 vs PetKit")]
DISC='<p class="disc"><strong>Liens affiliés :</strong> en tant que Partenaire Amazon, nous réalisons un bénéfice sur les achats remplissant les conditions requises. Cela ne change pas le prix pour vous. Prix et disponibilités variables : vérifiez toujours sur la page du vendeur.</p>'
def page(fn,title,desc,h1,body,related=True):
    nav="".join(f'<a href="{f}">{n}</a>' for f,n in NAV)
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
</head><body>
<header><a class="logo" href="./">🐱 {SITE}</a><nav>{nav}</nav></header>
<main>
<h1>{h1}</h1>
{DISC if fn not in ("affiliation.html",) else ""}
{body}
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
 "Guides d’achat indépendants pour chat d’appartement : litière automatique, GPS Tractive ou AirTag, fontaine à eau, distributeur de croquettes connecté.",
 "Équiper son chat d’appartement avec des objets connectés utiles",
 f'''<p class="lead">Un chat qui vit en intérieur dépend entièrement de son environnement : une litière propre, de l’eau qui donne envie de boire, des repas réguliers même quand vous rentrez tard. Les objets connectés peuvent aider — à condition de bien les choisir. Ici, on compare les modèles réels du marché, sans promesse miracle, avec les points qui comptent vraiment en appartement : bruit, encombrement, coût d’usage et sécurité.</p>
<h2>Nos guides</h2>
<ul class="cards">{cards}</ul>
<h2>Notre méthode</h2>
<p>Nous partons des fiches et manuels des fabricants, des retours d’utilisateurs et des contraintes concrètes d’un logement (surface, prises, Wi-Fi 2,4 GHz). Quand une donnée n’est pas claire ou varie selon les versions, nous le disons plutôt que d’inventer un chiffre. Les prix changent souvent : nous n’en affichons pas de précis, vérifiez-les sur la page du vendeur.</p>
<h2>Par où commencer ?</h2>
<ul>
<li>Vous travaillez de longues journées : commencez par le <a href="distributeur-croquettes-connecte.html">distributeur de croquettes connecté</a> et la <a href="meilleure-fontaine-eau-chat-2026.html">fontaine à eau</a>.</li>
<li>L’odeur de litière envahit le studio : lisez notre <a href="meilleure-litiere-automatique-2026.html">guide des litières automatiques</a>, puis le duel <a href="litter-robot-4-vs-petkit-pura-max-2.html">Litter-Robot 4 vs PetKit</a>.</li>
<li>Votre chat a accès au balcon ou s’échappe parfois : comparez <a href="gps-chat-tractive-vs-airtag.html">Tractive et AirTag</a>.</li>
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

# ---------- affiliation
page("affiliation.html",
 "Affiliation et mentions légales – Chat Appartement Connecté",
 "Mentions légales, politique d’affiliation (Partenaire Amazon) et confidentialité du site Chat Appartement Connecté.",
 "Affiliation, mentions légales et confidentialité",
 '''<h2>Liens affiliés</h2>
<p>Ce site contient des liens affiliés, signalés par les boutons « Voir sur Amazon ». <strong>En tant que Partenaire Amazon, nous réalisons un bénéfice sur les achats remplissant les conditions requises.</strong> Si vous achetez après avoir cliqué, nous pouvons percevoir une commission, sans surcoût pour vous. Cette rémunération n’influence pas nos recommandations ; les marques citées ne nous ont pas payés pour apparaître.</p>
<p>Les prix, disponibilités et caractéristiques sont susceptibles d’évoluer : la page du vendeur fait foi au moment de l’achat.</p>
<h2>Éditeur</h2>
<p>Site édité à titre personnel par la responsable de publication du projet Chat Appartement Connecté. Contact : via le dépôt GitHub du projet.</p>
<h2>Hébergement</h2>
<p>GitHub Pages — GitHub, Inc., 88 Colin P. Kelly Jr. Street, San Francisco, CA 94107, États-Unis.</p>
<h2>Contenu</h2>
<p>Les guides sont fournis à titre informatif et ne constituent pas un avis vétérinaire. En cas de doute sur la santé de votre chat, consultez un vétérinaire.</p>
<h2>Confidentialité et cookies</h2>
<p>Ce site ne dépose pas de cookie publicitaire et n’utilise pas d’outil de mesure d’audience. En cliquant sur un lien Amazon, vous êtes soumis à la politique de confidentialité d’Amazon, qui peut utiliser des cookies pour attribuer la commission.</p>''',related=False)

urls=["","meilleure-litiere-automatique-2026.html","gps-chat-tractive-vs-airtag.html","meilleure-fontaine-eau-chat-2026.html","distributeur-croquettes-connecte.html","litter-robot-4-vs-petkit-pura-max-2.html","affiliation.html"]
open("sitemap.xml","w").write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'+"".join(f"  <url><loc>{BASE}{u}</loc><lastmod>{TODAY}</lastmod></url>\n" for u in urls)+"</urlset>\n")
open("robots.txt","w").write(f"User-agent: *\nAllow: /\nSitemap: {BASE}sitemap.xml\n")
