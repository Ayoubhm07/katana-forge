# Chronique : la forge d'ayoubhammoudi.com (2026-10-18 et 2026-10-19)

Ce que la Forge a réellement fait, dans l'ordre, avec ce que le propriétaire a dit à chaque étape.
C'est la preuve que la méthode marche, et la liste des réactions humaines à anticiper.

| Étape | Livré | Réaction du propriétaire | Leçon |
|---|---|---|---|
| Récolte | LinkedIn, GitHub, CV FR/EN, ancien site (73 caractères de HTML lisible) dans `.war-room/harvest/` | « mets tout en mémoire » | la récolte précède tout ; conflits listés et tranchés par lui |
| S0 à S5 | contenu verrouillé (zod, sources, tests de vérité), pages lisibles sans JS, 3 démos sur vraies données, CI Lighthouse, CV avec téléphone | « mais c'est quoi ce design ? niveau débutant » | la rigueur ne se voit pas : il faut du spectaculaire visible |
| S6 | polices : CLS 0,33 en prod corrigé (block + optional) | | mesurer la prod |
| S7 | photos Unsplash partout, portrait, carte d'embarquement 3D, orbite, coverflow, globe WebGL, transitions page de livre | « great mais pas assez », menu sans noms de projets, cases split-flap « moches », image Phantera « sans sens » | chaque image doit signifier son sujet ; supprimer le basique |
| S8 | splash coloré qui plonge dans l'écran, livre 3D qui s'ouvre, transition portail, logos réels (LinkedIn, GitHub), labo à onglets, blog (4 articles vérifiés dans les diffs), tigre blanc + logo pour Phantera | « merged ! » | le livre et le splash ont emporté l'adhésion |
| S8 perf | perf 0,92 : splash sorti de React en SVG statique, Suspense par section | | le poids revient vite, couper avant d'ajouter |
| S9 | avatar qui danse sous le livre | « un avatar qui a de l'aura, pas un petit garçon », « un homme au katana qui tranche l'écran » | un personnage doit avoir de l'aura ; un geste fort vaut mieux qu'une danse |
| S9 bis | sabreur qui fend l'écran des 12 autres projets, galaxie de 43 compétences tirées des 15 projets LinkedIn (vortex, hyperespace), images d'articles liés réparées | « merged ! » | un accès unique à la section phare marque les esprits |
| Contenu | hackathon puis distinction retirés, FirstDown Tech corrigé (pas Spar-X) | | le propriétaire corrige les faits : enregistrer ses corrections |
| Domaine | ayoubhammoudi.com acheté par lui chez Vercel, branché, www et ancien alias en 301 | « okay cool !! » | l'humain paie, la Forge branche et vérifie |

## Ce qui a impressionné (à reproduire)

- Un objet réel qui s'ouvre (le livre) plutôt qu'un carrousel.
- Une ouverture qui raconte (on entre dans l'écran du créateur).
- Un personnage avec de l'aura qui fait un geste lourd de sens (trancher l'écran pour révéler la suite).
- Une visualisation où chaque élément est relié à une preuve (compétence vers projet).
- Les vrais logos et les vraies photos, partout où ils ont un sens.

## Ce qui a été rejeté (à ne jamais refaire)

- Un design sobre « correct » sans images ni 3D.
- Des cases split-flap pour les titres.
- Des noms de projets dans le menu.
- Une image décorative sans rapport avec le sujet.
- Un personnage mignon qui danse.
