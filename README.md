# Chat Appartement Connecté

Site statique FR (GitHub Pages) : guides d'équipement pour chat d'intérieur.
Générer : `python3 build.py`. Pas de secret dans ce dépôt. Voir docs/monetisation.md.

## Publication d'un nouvel article (routine quotidienne, vers 11h35)

Le site est généré uniquement par `build.py`. Un article ajouté en dehors de ce fichier (HTML écrit à la main, ancien gabarit) n'aura pas le design actuel.

Pour publier un nouvel article, le flux habituel reste valable, à condition de passer par `build.py` :

1. `git pull --ff-only` sur `main`.
2. Mettre à jour `TODAY` (date du jour, format `YYYY-MM-DD`) : la date du pied de page s'en déduit.
3. Ajouter le slug et le libellé à la fin de la liste `NAV` (cette liste sert à l'accueil, au sitemap et à « À lire aussi », plus à la navigation).
4. Ajouter une ligne sous l'ancre exacte suivante (ne pas la renommer ni la déplacer hors de `build.py`) :

   `<h2>Par où commencer ?</h2>`
   puis `<ul>`

5. Ajouter un appel `page("slug.html", titre, description, h1, corps, head_extra=...)` juste avant la ligne `urls=[`.
6. Insérer le slug dans `urls=` juste avant `"guide.html"`.
7. Ajouter les images dans `images/` (WebP de préférence) et une entrée `IMGMAP` (l'image d'ouverture en premier). Le fichier `sitemap-images.xml` est régénéré à partir de `IMGMAP`.
8. Dans le corps de l'article : tutoiement, aucun tiret cadratin ni demi-cadratin, une image principale en ouverture (`<figure><img ...>`) et, si possible, `og:image` dans `head_extra`.
9. Optionnel : ajouter le slug dans le bon groupe de `RELATED_GROUPS` pour un « À lire aussi » plus pertinent. Sinon, l'article recevra les 4 guides généraux.
10. Ne pas recréer l'ancienne navigation longue, ni multiplier les encarts payants ou les mentions « pas un lien d'affiliation ». `page()` pose déjà le menu court, un encart payant discret en fin d'article, et une seule ligne d'affiliation Amazon en bas.
11. Lancer `python3 build.py`, vérifier les liens Amazon `rappelalertes-21`, puis commit et `git push origin main` (images, `build.py`, HTML générés, `sitemap.xml`, `sitemap-images.xml`).

Le formulaire MailerLite (`Um0Zqt`), le consentement AdSense et les URLs existantes doivent rester en place. Ne supprimer aucune page.
