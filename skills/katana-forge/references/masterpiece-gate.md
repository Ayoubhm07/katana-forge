# The masterpiece gate

## Frame-by-frame inspection technique

In the built-in browser, on the scene being inspected:

```js
const root = document.querySelector('.ka'); // the scene
window.__seek = (t) => root.getAnimations({ subtree: true }).forEach((a) => { a.pause(); a.currentTime = t; });
__seek(1500); // then capture
```

Capture 4 to 6 key moments per scene. Careful: the screenshot may show the previous moment, so take another one.
For a canvas: trigger the real state (click, focus on a chip) and capture after 1 to 3 s.
Always test for real afterwards, without freezing anything: click, finger (375x812), keyboard, replay.

## The Shogun's seven questions (answer in writing)

1. **The stopping moment**: at what exact instant does a stranger stop scrolling? If there is none, it is not finished.
2. **Meaning**: does every image, logo and illustration say something true about its subject? (a network cable for an AI platform: no; a white tiger emerging from the shadows for "Phantera": yes)
3. **The flaw**: what defect breaks the magic (clipped text, distorted logo, jump, a scene that never ends)?
4. **The phone**: does the scene hold up at 375 px, by finger, with no horizontal overflow?
5. **Without JavaScript and with reduced motion**: do you see the final frame, readable and complete?
6. **Budgets**: are Lighthouse, weight, CLS and LCP measured and green?
7. **Truth**: is there a single unsourced fact, a single exaggeration?

Two-line verdict: what holds, what does not, MASTERPIECE or NOT YET.

## Defects actually found on ayoubhammoudi.com (look for these first)

- A grid without `minmax(0,1fr)` widens the column to 416 px on a 375 px screen.
- The scrolling code ran over the editor's title bar in the splash.
- The book's ribbons hid the header of the right-hand page.
- The author's name was unreadable over the cover's gold ornament.
- An orphan card on the last row of a 7-item grid.
- Related-article images were invisible (negative z-index without `isolate`).
- The galaxy froze after the jump (exception inside the rAF loop).
- The home link had no accessible name when its text was hidden on mobile (a11y 0.97).
