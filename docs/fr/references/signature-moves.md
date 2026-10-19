# Arsenal de signatures

Treize moves livrés en production sur ayoubhammoudi.com, décrits avec des mots. Le code source du site ne fait pas partie de ce skill.
Pour chacun : **le sens** (pourquoi il existe), **la chronologie**, **les ingrédients**, **les pièges payés**.
On ne recopie jamais un move tel quel : on garde la mécanique et on réinvente l'histoire pour le sujet.

---

## 1. Splash « on entre dans son écran »

**Sens :** le visiteur entre littéralement dans le monde du créateur.
**Chronologie (3,4 s) :** 0-0,75 s la scène sort du flou ; le code défile, les mains tapent, la commande s'écrit ;
2 s la caméra plonge dans le moniteur (scale 1 → 4,8, ease-in-out fort) ; 2,6 s l'écran devient noir site ;
3,15 s fondu de sortie. Bouton « Skip », Échap, clic.
**Ingrédients :** SVG 1600x900 (mur dégradé, néons flous, fenêtre et ville, lampe et cône de lumière, développeur
de dos, casque, clavier RGB, mug fumant), toutes les animations en CSS (hors fil principal).
**Livraison :** SVG **statique** dans `public/splash.svg`, injecté par un script de tête **seulement s'il joue**
(une fois par session, page d'accueil, pas de reduced-motion). Un `body::before` sombre tient l'image jusqu'à
l'arrivée de l'art. Fin pilotée par `animationend`, minuterie de secours à 7 s.
**Portrait :** `@media (max-aspect-ratio: 3/4)` recadre pour montrer le dev ET l'écran, zoom plus fort, origine décalée.
**Pièges :** dans l'arbre React, le splash ajoutait ~300 éléments à hydrater et son double dans le payload ;
`orientation: portrait` capture aussi les fenêtres presque carrées ; un timer démarré avant le premier rendu peut
couper l'animation sur réseau lent.

## 2. Transition portail entre sections

**Sens :** passer d'une section à l'autre comme on franchit une porte, depuis l'endroit où l'on a cliqué.
**Mécanique :** `document.startViewTransition`, variables `--portal-x/--portal-y` posées au clic, l'ancienne vue
`scale(0.84) blur(10px) brightness(0.3)`, la nouvelle s'ouvre en `clip-path: circle(0 → 150vmax at x y)`, 780 ms.
Clavier : centre de l'écran. Repli instantané sans View Transitions ou avec reduced-motion.
**Pièges :** ne pas `pushState` si le hash est déjà le bon (historique dupliqué).

## 3. Livre 3D qui s'ouvre vraiment

**Sens :** des projets se lisent en chapitres ; le livre transforme un CV en récit.
**Mécanique :** feuillets = 2 faces (`backface-visibility: hidden`, la face arrière `rotateY(180deg)`), pivot sur la
reliure, `rotateY(-180deg)` pour tourner. Large : double page (planche photo à gauche, preuves à droite) ;
étroit (< 900 px) : une page à la fois, les feuillets tournés s'effacent. Ouverture automatique à 55 % de visibilité.
Glisser : la page suit le doigt, se termine au-delà de 30 %. Flèches, boutons, rubans pour sauter (tours
décalés de 140 ms). Faces cachées `inert` + `aria-hidden`, région annoncée en `aria-live`.
**Matières :** couverture cuir (photo NYPL) + médaillon + dorure animée (`background-clip: text`), plaque sombre
pour l'auteur, pages crème `#efe7d6` avec ombre de reliure, lettrine, bloc de tranche rayé, ombre au sol.
**Pièges :** `preserve-3d` sur la scène ignore les z-index (z-fighting) : perspective sur la scène, preserve-3d sur
chaque feuillet seulement ; minuteries de saut multiple à nettoyer et à borner ; boutons désactivés qui volent
le focus (utiliser `aria-disabled`) ; rubans qui cachent l'en-tête : les faire pendre sous le livre.

## 4. Le sabreur qui tranche l'écran

**Sens :** « ce livre n'est qu'un extrait » ; il fend l'écran qui liste les autres projets et en libère GitHub et LinkedIn.
**Chronologie (2,8 s + boucle) :** entrée 0 ; bulle mot à mot 0,3 s ; l'aura s'embrase 0,9 s (accroupi) ;
dégainé 1,5 s (la lame sort du fourreau en `scaleY`) ; armé au-dessus de la tête ; 1,93 s ruée + coupe diagonale
(traînée `stroke-dashoffset`, flash blanc) ; 2,08 s l'écran se sépare en deux moitiés (`clipPath` le long de la
droite y = 50 + (x - 380) * 0,76) ; 2,25 s les logos jaillissent de la fente (anneau, éclat) ; retour en garde basse.
Boucle : flammes, braises, écharpe, logos qui flottent. Bouton « rejouer ».
**Ingrédients :** un seul SVG 900x500 (personnage adulte en silhouette avec liseré doré, aura floutée, écran
dupliqué dans deux clipPath), logos en `<a>` HTML positionnés en % au-dessus. États : statique (image finale,
sans JS), `is-armed`, `is-playing`.
**Pièges :** l'utilisateur a refusé « un petit garçon qui danse » : un personnage doit avoir de l'aura ; le bandeau
cachait l'œil lumineux ; une faute de frappe dans le tracé GitHub (`-33.920`) ne se voit qu'au rendu.

## 5. Galaxie de compétences (accès par saut en hyperespace)

**Sens :** chaque compétence reliée aux projets qui l'ont réellement utilisée ; on n'affiche pas une liste, on montre un univers.
**Accès unique :** vortex scellé (trou noir doré, disque de particules) → bouton ou section bien en vue →
hyperespace (traînées d'étoiles qui accélèrent, 1,4 s) → flash → la galaxie jaillit en spirale (1,5 s, easeOutBack).
**Moteur :** canvas 2D, projection perspective maison, 6 constellations (une par domaine) en calottes sphériques
(angle d'or), anneau incliné des projets, noyau lumineux, fils animés (`setLineDash` + `lineDashOffset`),
glisser avec inertie, survol et épinglage, filtres par domaine. Chargé par `import()` près de la section, boucle
arrêtée hors écran. Liste HTML rendue serveur = alternative accessible et SEO (survol d'une puce = épinglage).
**Pièges :** le premier timestamp rAF peut précéder `performance.now()` → temps négatif → `createRadialGradient`
jette et tue la boucle (borner à 0, rAF planifié avant de dessiner) ; les variables CSS ne marchent pas dans
`ctx.font` ; observer le canvas (pas tout le bloc) pour le déclenchement à 60 % ; étiquettes bornées au cadre.

## 6. Titres qui se décodent

**Mécanique :** au premier passage dans le viewport (60 %), les caractères sortent du bruit de gauche à droite en
rAF ; le vrai texte reste dans le DOM, l'overlay est `aria-hidden`. Jamais sur le H1 au-dessus de la ligne de
flottaison (retarde le LCP).
**Crédit :** idée inspirée d'un composant communautaire 21st.dev.

## 7. Compteurs à rouleaux

**Mécanique :** chaque caractère est une colonne qui monte d'un flou au changement de valeur (`key` liée à la
valeur, délai 28 ms par colonne). Remplace les cases split-flap, jugées datées.

## 8. Frises de logos

**Mécanique :** piste en `translate3d` pilotée par rAF, vitesse qui ralentit en douceur (constante 0,19 s) sous le
pointeur ou le focus, copies calculées selon la largeur, masque en dégradé sur les bords ; statique et défilable
au clavier avec reduced-motion.
**Crédit :** idée inspirée d'un composant communautaire 21st.dev.

## 9. Cartes éclairées par le pointeur

**Mécanique :** un seul écouteur délégué écrit `--spot-x/--spot-y` sur la carte survolée, un `::before` dessine un
`radial-gradient` ; souris seulement (`hover: hover and pointer: fine`).

## 10. Ligne du temps qui se dessine

**Mécanique :** `view-timeline-name` sur la liste, `animation-timeline` sur le rail (`scaleY 0 → 1`), cartes en
`animation-timeline: view()`, cartes alternées qui se chevauchent sur desktop (`margin-top: -72px`). Zéro JS.

## 11. Couvertures photo de section

**Mécanique :** `clip-path: inset()` qui s'ouvre et zoom lent liés à `view()`, grand numéro fantôme, dégradé vers le
fond. Photo de section choisie pour son sens (quai de gare pour les contributions, Paris de nuit pour le parcours).

## 12. Carte d'embarquement 3D

**Mécanique :** inclinaison via `--tilt-x/--tilt-y`, reflet `--glare-x/--glare-y`, entrée `rotateX(18deg) → 0`.
Portrait réel du propriétaire (avatar GitHub 460 px).

## 13. Console labo

**Mécanique :** fenêtre avec barre de titre, statut « en marche » pulsé, onglets ARIA (flèches gauche/droite),
seule la démo de l'onglet ouvert est montée ; les liens « lancer dans le labo » du livre choisissent l'onglet
avant que le portail s'ouvre. Démos sur données réelles épinglées à un commit.
