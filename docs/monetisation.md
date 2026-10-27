# Monétisation

Config centrale : `data/affiliate.json` (lue par `build.py`).

## Actif
- **Amazon Partenaires FR** : tag `rappelalertes-21` (partagé avec Rappel Alertes). Liens de recherche amazon.fr, `rel="sponsored nofollow"`.
- **Guide payant Gumroad** : https://fluenthub.gumroad.com/l/jvlfm (produit propre, pas d'affiliation).
- **À faire (Carole)** : compléter les informations fiscales Amazon Partenaires, sinon pas de paiement.

## À venir — rien d'actif, aucun ID inventé

### Étapes Carole
1. **Awin** : créer un compte éditeur sur https://www.awin.com/fr (site déclaré : https://caro123-create.github.io/chat-appartement-connecte/, thème animaux / chat connecté). Frais d'inscription éventuels remboursés selon Awin.
2. Dans Awin → *Annonceurs* → chercher **Zooplus FR** et **Tractive** → *Rejoindre le programme*. Attendre l'acceptation (quelques jours).
3. **Alternative Tractive direct** : si Tractive n'est pas sur Awin pour la France, s'inscrire au programme partenaire sur le site Tractive (page « Affiliés / Partenaires » en pied de page).

### Ce qu'il faut me renvoyer
- **awinaffid** : ton ID éditeur Awin (nombre, visible en haut à droite du tableau de bord).
- **mid** de chaque marchand accepté (Zooplus, Tractive) : visible dans la fiche annonceur.
- Idéalement 1–2 **deep links** générés par Awin (*Outils → Générateur de liens*) vers les pages produits Tractive GPS CAT et la catégorie fontaines/litières Zooplus, pour vérifier le format.
- Tractive direct : l'**URL de suivi** fournie par Tractive.

### Ensuite (agent)
Renseigner `data/affiliate.json`, passer `enabled` à `true`, `python3 build.py`, vérifier un clic, push. Les boutons secondaires n'apparaissent qu'à ce moment-là.
