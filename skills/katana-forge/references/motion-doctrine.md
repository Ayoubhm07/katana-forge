# Motion doctrine

How the Forge decides whether something moves, how it moves, and how it degrades. Written for this skill,
distilled from shipping ayoubhammoudi.com and from the public talks and writing of the people who taught the
industry to care about motion (Apple's WWDC sessions on fluid interfaces, Emil Kowalski, the web platform docs).

---

## 1. The gate: should it move at all?

| How often the user meets it | Decision |
|---|---|
| Hundreds of times a day (shortcuts, command menu) | Never animate. Instant is the feature. |
| Tens of times (hover, list navigation) | Barely: fast, subtle, or nothing. |
| Occasionally (drawers, modals, section changes) | Standard motion. |
| Once (opening, first visit, a signature moment) | This is where the spectacle budget lives. |

Then name the purpose in one word: **feedback**, **continuity** (where it came from and went), **state**,
**bridging** (something would otherwise teleport), **explanation**, or **delight** (rare moments only).
No purpose, no motion. "It looks cool" on something frequent is a reason to stop.

## 2. The cheapest tool that works

1. **CSS transition** for hover, press and class-driven state.
2. **CSS keyframes** for predetermined sequences (splash, the swordsman, the guide). They run off the main thread.
3. **CSS scroll-driven animations** (`animation-timeline: view()` / named view timelines) for scroll reveals and
   self-drawing lines. Zero JavaScript.
4. **View Transitions** (`document.startViewTransition`) for changes between views or sections.
5. **Web Animations API** for programmatic control without a library.
6. **Canvas 2D with your own projection** for heavy 3D scenes with many objects (the skill galaxy).
7. A motion library only for spring-driven, gesture-driven, interruptible UI that CSS cannot express.

## 3. Properties and curves

- Animate `transform`, `opacity`, `clip-path` and `filter`. Never `width`, `height`, `top`, `left`, margins.
- Never `scale(0)`: start from 0.9 to 0.97 with opacity 0.
- Never `transition: all`. Name the properties.
- Entering and exiting: strong ease-out `cubic-bezier(0.23, 1, 0.32, 1)`. Moving on screen: `cubic-bezier(0.77, 0, 0.175, 1)`.
  Overshoot (`cubic-bezier(0.34, 1.56, 0.64, 1)`) only where something is thrown or bursts (logos out of a cut).
- UI durations stay under 300 ms. Cinematic moments may run seconds, but must be skippable.
- Stagger lists by 30 to 80 ms. A word-by-word bubble at about 50 ms per word reads as speech.

## 4. Fluid, interruptible, physical

- Respond on press, not on release. Feedback within 100 ms.
- Direct manipulation is 1:1: a dragged page follows the finger from where it was grabbed, then finishes the turn
  past a threshold (30 % on the book) or falls back.
- Everything can be interrupted: never lock input during a transition, retarget from the current value.
- Momentum: inertia on drag-to-rotate (the galaxy keeps spinning and settles back to its idle speed).
- Spatial consistency: things leave the way they came; a portal opens from where you clicked.

## 5. Materials and depth

- Translucent layers (`backdrop-filter`) carry hierarchy; never stack light translucency on light translucency.
- Real-world materials sell an object: leather and gold foil on a cover, cream paper with a spine shadow, a page
  block made of thin stripes, a ground shadow under a floating book.
- Glow belongs to energy (a blade, an aura, a logo bursting out), not to every card.

## 6. Reduced motion and no JavaScript

- `prefers-reduced-motion: reduce` keeps meaning and drops travel: show the final frame, keep opacity changes,
  remove movement, parallax and loops.
- Without JavaScript the base CSS is the final frame: the book shows its cover, the swordsman stands in guard with
  the screen already cut and the links ready, the galaxy section shows its full skill list.
- A splash never runs without JavaScript, never twice in a session, never with reduced motion.

## 7. Native-feeling on phones

- Gate hover styles behind `@media (hover: hover) and (pointer: fine)`.
- `-webkit-tap-highlight-color: transparent` with a real `:active` state instead.
- `100svh` for heroes, `100dvh` for app shells.
- Inputs at 16 px minimum (no zoom on focus); never disable zoom.
- `touch-action: pan-y` on horizontal drag surfaces (the book, the galaxy) so vertical scrolling still works.
- Safe areas: `viewport-fit=cover` plus `env(safe-area-inset-*)` on fixed controls (the skip button).
- Grids use `minmax(0, 1fr)`; check 375 px for horizontal overflow.
- Test on a real phone before calling it done.

## 8. Inspecting motion

Freeze any CSS or WAAPI animation and look at it:

```js
const root = document.querySelector('.scene');
const seek = (t) => root.getAnimations({ subtree: true }).forEach((a) => { a.pause(); a.currentTime = t; });
seek(1500);
```

Review 4 to 6 instants per scene, then play it for real at full speed, by click, finger and keyboard.
