# Budgets et leçons de performance

## Budgets imposés en CI (lighthouserc)

- Performance ≥ 0,95 (mobile simulé, lhci garde le meilleur de 3 runs : surveiller aussi la médiane).
- Accessibilité, bonnes pratiques, SEO = 1.
- LCP ≤ 3 000 ms, CLS ≤ 0,05.
- Contrôle no-JS : chaque page atteint un seuil de texte visible et contient ses chaînes clés.

## Mesures à prendre après chaque signature

```bash
curl -s -H "Accept-Encoding: gzip" http://localhost:3000/en -o /dev/null -w "gz=%{size_download}\n"
```
Plus le nombre d'éléments (`<[a-zA-Z]` hors script/style) et le « First Load JS » du build.
Référence ayoubhammoudi.com : la prod est passée de 49 Ko gzip / 880 éléments à 76 Ko / 1 340, et la
performance est tombée à 0,92. Les corrections l'ont ramenée au vert.

## Leviers, du plus rentable au moins rentable

1. **Sortir de React ce qui est statique** (art SVG, illustrations) : fichier dans `public/`, chargé à la demande.
2. **`<Suspense>` autour de chaque section lourde** : l'hydratation se découpe, le TBT baisse.
3. **`next/dynamic` / `import()` près du viewport** pour les démos, moteurs canvas, globes.
4. **Polices** : sous-ensemble local (fontTools), `font-display: block` pour la police du LCP, `optional` pour la mono ; preload unique.
5. **CSS inliné** (`experimental.inlineCss`) quand la feuille est petite.
6. **Images** : `next/image` avec `sizes` exact ; jamais un JPEG plein format affiché en 40 px.
7. **Boucles rAF** : arrêtées hors écran (IntersectionObserver) et onglet caché.

## Pièges payés

- Le CLS des polices (0,33 en prod) n'apparaissait pas en CI localhost : mesurer la production.
- L'élément LCP peut devenir un paragraphe dont le rendu attend la police : 85 % de « render delay ».
- Une animation d'opacité 0 sur le H1 au chargement retarde le LCP s'il en devient le candidat.
- Le payload RSC duplique le HTML : tout composant serveur rendu dans un client compte deux fois.
- La page de prévisualisation peut garder un HTML en cache pendant un redémarrage : recharger avec un paramètre.
