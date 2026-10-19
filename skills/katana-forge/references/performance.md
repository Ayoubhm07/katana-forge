# Performance budgets and lessons

## Budgets enforced in CI (lighthouserc)

- Performance ≥ 0.95 (simulated mobile; lhci keeps the best of 3 runs, so watch the median too).
- Accessibility, best practices, SEO = 1.
- LCP ≤ 3,000 ms, CLS ≤ 0.05.
- No-JS check: every page reaches a visible-text threshold and contains its key strings.

## Measurements to take after every signature move

```bash
curl -s -H "Accept-Encoding: gzip" http://localhost:3000/en -o /dev/null -w "gz=%{size_download}\n"
```

Plus the element count (`<[a-zA-Z]` excluding script/style) and the build's "First Load JS".
ayoubhammoudi.com reference: production went from 49 KB gzip / 880 elements to 76 KB / 1,340, and
performance dropped to 0.92. The fixes brought it back to green.

## Levers, from highest to lowest payoff

1. **Move static content out of React** (SVG art, illustrations): a file in `public/`, loaded on demand.
2. **`<Suspense>` around every heavy section**: hydration gets split up and TBT drops.
3. **`next/dynamic` / `import()` near the viewport** for demos, canvas engines and globes.
4. **Fonts**: local subset (fontTools), `font-display: block` for the LCP font, `optional` for the mono font; a single preload.
5. **Inlined CSS** (`experimental.inlineCss`) when the stylesheet is small.
6. **Images**: `next/image` with an exact `sizes`; never a full-size JPEG displayed at 40 px.
7. **rAF loops**: stopped when off screen (IntersectionObserver) and when the tab is hidden.

## Lessons paid for

- Font CLS (0.33 in production) did not show up in localhost CI: measure production.
- The LCP element can become a paragraph whose rendering waits for the font: 85% "render delay".
- An opacity-0 animation on the H1 at load delays LCP if the H1 becomes the candidate.
- The RSC payload duplicates the HTML: every server component rendered inside a client component counts twice.
- The preview page can keep cached HTML across a restart: reload with a query parameter.
