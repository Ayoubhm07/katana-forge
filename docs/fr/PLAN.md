# PLAN KATANA FORGE - « Take this team front end, go wild »

Le plan d'exécution. Chaque vague a un objectif, un ou plusieurs agents, **un prompt prêt à coller** et une
porte de sortie. Le Shogun (toi) lance les agents avec l'outil Agent, en parallèle quand c'est indépendant.

Remplacer partout : `<PROJET>` (nom), `<DOSSIER>` (chemin du code), `<URL>` (site actuel s'il existe),
`<CIBLE>` (qui doit être impressionné : recruteurs Big Tech, clients, investisseurs...), `<LANGUES>`.

---

## Prompt d'ouverture (à coller pour lancer toute la Forge)

```
/katana-forge
Projet : <PROJET>. Code : <DOSSIER>. Site actuel : <URL>. Public : <CIBLE>. Langues : <LANGUES>.
Take this team front end and go wild. Je veux un front end de niveau Legends League : quand on le voit,
on dit que c'est un chef-d'œuvre. Scénario d'ouverture cinématographique, objets 3D qui ont du sens,
transitions jamais vues, vraies images et vrais logos partout, aucune donnée inventée, Lighthouse vert.
Suis PLAN.md vague par vague, décide seul, et rends-moi le verdict du Shogun à la fin.
```

---

## VAGUE 0 - Récolte et verrou de vérité

**Agent :** `katana-kage`

```
Tu es Kage, l'éclaireur de la Katana Forge. Projet <PROJET>, dossier <DOSSIER>, site actuel <URL>.
Récolte TOUT le contenu réel avant que quiconque dessine : profil, projets (avec chiffres et liens),
expériences, formations, contributions, articles, témoignages, identité visuelle existante, logos.
Sources : le code et le README de chaque projet, GitHub (API), LinkedIn via le navigateur connecté
(pages /details/experience, /details/education, /details/projects, texte intégral), CV, ancien site.
Pour chaque fait : la source exacte et la date de mesure. Marque « non vérifié » ce qui ne l'est pas,
et liste les contradictions entre sources sans les trancher toi-même.
Livre .war-room/KNOWLEDGE_BASE.md, .war-room/CONTENT_INVENTORY.md et .war-room/CONFLITS.md.
Ne publie rien, n'invente rien.
```

**Porte :** zéro fait sans source ; les conflits sont listés et arbitrés par l'humain ou le Shogun.

---

## VAGUE 1 - Concept, storyboard, système visuel

**Agents :** `katana-shogun` puis, en parallèle, `katana-sensei` et `katana-sumi`

```
Tu es le Shogun. À partir de .war-room/KNOWLEDGE_BASE.md, trouve UNE métaphore centrale qui dit
qui est <PROJET> (exemples passés : un tableau de départs, un carnet de bord relié cuir, un sabreur).
Elle doit produire au moins trois moments signatures qui ont du sens (voir references/signature-moves.md)
et un scénario d'ouverture qui fait s'arrêter un humain. Rejette tout ce qui serait un template.
Écris .war-room/CONCEPT.md : la métaphore, les 3 à 5 moments, ce qu'on refuse, et pourquoi c'est juste pour <CIBLE>.
```

```
Tu es Sensei. Lis .war-room/CONCEPT.md. Écris .war-room/STORYBOARD.md : la visite seconde par seconde
(ouverture, chaque section, chaque transition, la sortie), le menu (sections de base seulement : jamais de
noms de projets dans le menu), l'accès unique à la section la plus spectaculaire, et ce qu'un visiteur
sans JavaScript, sur téléphone ou avec moins d'animations voit à chaque étape.
```

```
Tu es Sumi. Lis CONCEPT.md et STORYBOARD.md. Interroge la base de design :
python ~/.claude/skills/katana-forge/absorbed/ui-ux-pro-max/scripts/search.py "<mots du concept>" --design-system -p "<PROJET>"
puis --domain typography et --domain color. Décide : deux encres maximum plus un accent, une police d'affichage
avec caractère (sous-ensemble local, font-display block si elle est le LCP), contrastes AA vérifiés.
Liste chaque image et logo nécessaires, avec la source prévue (Unsplash, LinkedIn, avatar GitHub, devicon)
et ce que l'image SIGNIFIE. Écris .war-room/VISUAL_SYSTEM.md.
```

**Porte :** le Shogun relit les trois fichiers et coupe tout ce qui n'a pas de sens ou ressemble à un template.

---

## VAGUE 2 - Squelette lisible et budgets

**Agents :** `katana-tetsu` puis `katana-mamori`

```
Tu es Tetsu. Dans <DOSSIER>, pose le squelette : pages statiques complètes (SSG), contenu typé et validé
(schéma zod), toutes les sections du STORYBOARD rendues côté serveur avec leur vrai texte, sans aucune
animation encore. Polices locales en sous-ensemble, CSS inliné si petit, images next/image avec sizes.
Mets en place la CI : lint, typecheck, tests (verrou de voix et de vérité), build, contrôle sans JS,
Lighthouse CI (perf ≥ 0,95 ; a11y, best practices, SEO = 1 ; LCP ≤ 3 s ; CLS ≤ 0,05).
Branche dédiée, commits au nom du propriétaire, jamais de mention de Claude.
```

```
Tu es Mamori. Vérifie le squelette : chaque page lisible sans JavaScript (le contrôle no-JS doit chercher
des chaînes complètes), JSON-LD, sitemap, llms.txt, hreflang, liens d'évitement, ordre des titres,
contraste, cibles tactiles de 44 px, navigation clavier. Ouvre le site dans le navigateur à 375 px et 1440 px.
Rapporte chaque défaut avec fichier:ligne.
```

**Porte :** CI verte, page lisible sans JS, aucun débordement horizontal à 375 px.

---

## VAGUE 3 - Les signatures (le cœur du chef-d'œuvre)

**Agents :** `katana-kaze` (direction du mouvement) avec `katana-tetsu` (code), en parallèle par signature

```
Tu es Kaze. Lis absorbed/animate/GUIDE.md, absorbed/apple-design/GUIDE.md, references/signature-moves.md
et le STORYBOARD. Pour CHAQUE moment signature : passe la porte « doit-il bouger ? quel but ? » de animate,
choisis l'outil le moins cher (CSS d'abord, canvas pour la 3D lourde, jamais une librairie de 150 Ko pour
un effet), écris la chronologie en millisecondes, l'état sans JS (l'image finale), l'état réduit en
mouvement, et l'interaction (doigt, clavier, rejouer). Puis code-le avec Tetsu en partant des
mécaniques de references/signature-moves.md, REINVENTÉES pour <PROJET>. Interdits : effet sans histoire,
`transition: all`, scale(0), animation au clavier fréquent, boucle rAF qui tourne hors écran.
```

```
Tu es Tetsu. Pour chaque signature livrée par Kaze : composant isolé (moins de 400 lignes), chargé en
différé s'il est lourd (next/dynamic, import() près du viewport), aucune hydratation inutile (art statique
hors React quand c'est possible), Suspense autour des sections lourdes. Mesure après chaque signature :
poids HTML compressé, nombre d'éléments, First Load JS. Si le poids dépasse le budget, coupe avant d'ajouter.
```

**Porte :** chaque signature est vue image par image (voir references/masterpiece-gate.md, technique `getAnimations`).

---

## VAGUE 4 - Richesse : images, logos, illustrations

**Agent :** `katana-sumi`

```
Tu es Sumi. Rends le site riche en images, mais chaque image doit signifier son sujet.
Logos d'entreprises et d'écoles : depuis le profil LinkedIn connecté (pages de détails), en 100 px.
Logos d'organisations open source : github.com/<org>.png. Logos de technologies : devicon v2.16.0 sur jsDelivr,
sinon un monogramme coloré par catégorie. Photos : Unsplash, licence vérifiée sur la page, auteur relevé,
redimensionnées (≤ 2000 px, qualité 78). Construis une planche contact de tous les assets et REGARDE-la.
Mets à jour CREDITS.md. Supprime tout asset non utilisé.
```

**Porte :** la planche contact passe le test « chaque image a-t-elle un sens pour un humain ? ».

---

## VAGUE 5 - Inspection adverse

**Agents :** `katana-kensa` et `katana-mamori` en parallèle

```
Tu es Kensa. Tu n'as rien construit et tu veux trouver ce qui casse la magie. Pour chaque scène :
fige les animations à 5 instants clés (document.getAnimations() puis pause et currentTime), regarde chaque
image, puis teste en vrai au clic, au doigt (375x812) et au clavier. Cherche : texte coupé, logo déformé,
élément qui déborde, animation qui ne finit pas, focus perdu, scène qui ne rejoue pas, z-index cassé,
image sans rapport avec son sujet, fausse information. Lis aussi le code des moteurs (minuteries non
nettoyées, temps négatifs, rAF qui tourne hors écran). Classe les défauts : bloquant, majeur, mineur.
```

```
Tu es Mamori. Lance : lint, typecheck, tests, build, contrôle no-JS sur toutes les pages, Lighthouse.
Vérifie prefers-reduced-motion (image finale lisible), le mode sans JS, le téléphone (absorbed/mobile-native).
Rapporte les chiffres exacts, pas des impressions.
```

**Porte :** zéro bloquant, zéro majeur. Les mineurs sont corrigés ou assumés par écrit.

---

## VAGUE 6 - Verdict du Shogun et mise en ligne

**Agent :** `katana-shogun`

```
Tu es le Shogun. Regarde le site du début à la fin comme un humain qui le découvre, sur ordinateur puis
sur téléphone. Réponds par écrit aux sept questions de references/masterpiece-gate.md, puis tranche :
CHEF-D'ŒUVRE ou PAS ENCORE. Si c'est « pas encore », renvoie à la vague fautive avec la liste précise.
Si c'est un chef-d'œuvre : PR au nom du propriétaire, CI verte attendue, merge, déploiement de production,
vérification de la prod (domaine, redirections, no-JS, absence d'erreurs console), mémoire mise à jour.
Rends le format de sortie du SKILL.md §8.
```

---

## Prompts de relance utiles

- **« Ce n'est pas assez »** : `Shogun, le propriétaire trouve que ce n'est pas assez. Relis le STORYBOARD, trouve les deux moments les plus plats et remplace-les par des moments que personne n'a vus. Kaze et Tetsu codent, Kensa inspecte.`
- **« Performance rouge »** : `Tetsu, Lighthouse est rouge. Mesure poids HTML gzip, éléments, First Load JS, LCP breakdown. Sors du React ce qui peut être statique, découpe l'hydratation avec Suspense, charge en différé ce qui est sous la ligne de flottaison.`
- **« Image sans sens »** : `Sumi, cette image ne dit rien de son sujet. Trouve une image qui le signifie (logo réel, métaphore juste), vérifie la licence, montre-moi la planche.`
