# Porte du chef-d'œuvre

## Technique d'inspection image par image

Dans le navigateur intégré, sur la scène à inspecter :

```js
const root = document.querySelector('.ka'); // la scène
window.__seek = (t) => root.getAnimations({ subtree: true }).forEach((a) => { a.pause(); a.currentTime = t; });
__seek(1500); // puis capture
```
Prendre 4 à 6 instants clés par scène. Attention : la capture peut afficher l'instant précédent, en reprendre une.
Pour un canvas : provoquer l'état réel (clic, focus d'une puce) et capturer après 1 à 3 s.
Toujours tester ensuite en vrai, sans figer : clic, doigt (375x812), clavier, rejouer.

## Les sept questions du Shogun (répondre par écrit)

1. **Le moment d'arrêt** : à quel instant précis un inconnu s'arrête-t-il ? S'il n'y en a pas, ce n'est pas fini.
2. **Le sens** : chaque image, logo, illustration dit-elle quelque chose de vrai sur son sujet ? (un câble réseau pour une plateforme d'IA : non ; un tigre blanc qui sort de l'ombre pour « Phantera » : oui)
3. **La faille** : quel défaut casse la magie (texte coupé, logo déformé, saut, scène qui ne finit pas) ?
4. **Le téléphone** : la scène tient-elle à 375 px, au doigt, sans débordement horizontal ?
5. **Sans JavaScript et avec moins d'animations** : voit-on l'image finale, lisible, complète ?
6. **Les budgets** : Lighthouse, poids, CLS, LCP sont-ils mesurés et verts ?
7. **La vérité** : un seul fait non sourcé, une seule exagération ?

Verdict en deux lignes : ce qui tient, ce qui ne tient pas, CHEF-D'ŒUVRE ou PAS ENCORE.

## Défauts trouvés en vrai sur ayoubhammoudi.com (à chercher en premier)

- Une grille sans `minmax(0,1fr)` élargit la colonne à 416 px sur un écran de 375 px.
- Le code qui défile passait par-dessus la barre de titre de l'éditeur dans le splash.
- Les rubans du livre masquaient l'en-tête de la page de droite.
- Le nom de l'auteur était illisible sur l'ornement doré de la couverture.
- Carte orpheline sur la dernière ligne d'une grille de 7.
- Images d'articles liés invisibles (z-index négatif sans `isolate`).
- Galaxie figée après le saut (exception dans la boucle rAF).
- Lien d'accueil sans nom accessible quand le texte est masqué sur mobile (a11y 0,97).
