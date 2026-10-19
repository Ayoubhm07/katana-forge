# Signature moves arsenal

Thirteen moves shipped to production on ayoubhammoudi.com, described in words. The site's source code is not part of this skill.
For each one: **the meaning** (why it exists), **the timeline**, **the ingredients**, **the lessons paid for**.
Never copy a move as is: keep the mechanics and reinvent the story for the subject.

---

## 1. "Entering their screen" splash

**Meaning:** the visitor literally steps into the creator's world.
**Timeline (3.4 s):** 0 to 0.75 s the scene comes out of blur; code scrolls, hands type, the command writes itself;
2 s the camera dives into the monitor (scale 1 → 4.8, strong ease-in-out); 2.6 s the screen turns into the site's black;
3.15 s fade out. "Skip" button, Escape, click.
**Ingredients:** a 1600x900 SVG (gradient wall, blurred neon lights, window and city, lamp and light cone, developer
seen from behind, headset, RGB keyboard, steaming mug), every animation in CSS (off the main thread).
**Delivery:** a **static** SVG in `public/splash.svg`, injected by a head script **only when it plays**
(once per session, home page, no reduced-motion). A dark `body::before` holds the frame until the art
arrives. The end is driven by `animationend`, with a 7 s fallback timer.
**Portrait:** `@media (max-aspect-ratio: 3/4)` reframes to show both the developer AND the screen, with a stronger zoom and a shifted origin.
**Lessons paid for:** inside the React tree, the splash added ~300 elements to hydrate plus its duplicate in the payload;
`orientation: portrait` also matches nearly square windows; a timer started before the first paint can
cut the animation short on a slow network.

## 2. Portal transition between sections

**Meaning:** moving from one section to the next feels like stepping through a door, opening from where you clicked.
**Mechanics:** `document.startViewTransition`, `--portal-x/--portal-y` variables set on click, the old view goes
`scale(0.84) blur(10px) brightness(0.3)`, the new one opens with `clip-path: circle(0 → 150vmax at x y)`, 780 ms.
Keyboard: center of the screen. Instant fallback without View Transitions or with reduced-motion.
**Lessons paid for:** do not `pushState` if the hash is already correct (duplicate history entries).

## 3. A 3D book that really opens

**Meaning:** projects read as chapters; the book turns a resume into a story.
**Mechanics:** leaves = 2 faces (`backface-visibility: hidden`, back face at `rotateY(180deg)`), pivoting on the
spine, `rotateY(-180deg)` to turn. Wide: double spread (photo plate on the left, evidence on the right);
narrow (< 900 px): one page at a time, turned leaves fade out. Opens automatically at 55% visibility.
Drag: the page follows the finger and completes past 30%. Arrows, buttons and ribbons to jump (turns
staggered by 140 ms). Hidden faces are `inert` + `aria-hidden`, and the region is announced via `aria-live`.
**Materials:** leather cover (NYPL photo) + medallion + animated gilding (`background-clip: text`), dark plate
for the author, cream pages `#efe7d6` with a spine shadow, drop cap, striped page-edge block, ground shadow.
**Lessons paid for:** `preserve-3d` on the scene ignores z-index (z-fighting): put perspective on the scene and preserve-3d on
each leaf only; multi-jump timers must be cleaned up and bounded; disabled buttons steal
focus (use `aria-disabled`); ribbons covered the header: hang them below the book instead.

## 4. The swordsman who slices the screen

**Meaning:** "this book is only an excerpt"; he splits the screen listing the other projects and releases GitHub and LinkedIn from it.
**Timeline (2.8 s + loop):** entrance at 0; speech bubble word by word at 0.3 s; the aura ignites at 0.9 s (crouched);
draw at 1.5 s (the blade leaves the scabbard via `scaleY`); raised overhead; 1.93 s rush + diagonal cut
(`stroke-dashoffset` trail, white flash); 2.08 s the screen splits into two halves (`clipPath` along the
line y = 50 + (x - 380) * 0.76); 2.25 s the logos burst out of the gap (ring, glint); back to a low guard.
Loop: flames, embers, scarf, floating logos. "Replay" button.
**Ingredients:** a single 900x500 SVG (adult character in silhouette with a gold rim light, blurred aura, screen
duplicated in two clipPaths), logos as HTML `<a>` elements positioned in % on top. States: static (final frame,
no JS), `is-armed`, `is-playing`.
**Lessons paid for:** the owner rejected "a little boy dancing": a character needs aura; the headband
hid the glowing eye; a typo in the GitHub path (`-33.920`) only shows up when rendered.

## 5. Skills galaxy (entered through a hyperspace jump)

**Meaning:** every skill is linked to the projects that actually used it; we do not show a list, we show a universe.
**Single entry point:** sealed vortex (golden black hole, particle disk) → button or prominent section →
hyperspace (star trails that accelerate, 1.4 s) → flash → the galaxy bursts out in a spiral (1.5 s, easeOutBack).
**Engine:** 2D canvas, hand-rolled perspective projection, 6 constellations (one per domain) on spherical caps
(golden angle), tilted ring of projects, glowing core, animated threads (`setLineDash` + `lineDashOffset`),
drag with inertia, hover and pinning, domain filters. Loaded via `import()` near the section, loop
stopped when off screen. A server-rendered HTML list is the accessible and SEO alternative (hovering a chip pins it).
**Lessons paid for:** the first rAF timestamp can precede `performance.now()` → negative time → `createRadialGradient`
throws and kills the loop (clamp to 0, schedule rAF before drawing); CSS variables do not work in
`ctx.font`; observe the canvas (not the whole block) for the 60% trigger; keep labels within the frame.

## 6. Decoding headings

**Mechanics:** on first entry into the viewport (60%), characters resolve out of noise from left to right via
rAF; the real text stays in the DOM, the overlay is `aria-hidden`. Never on an above-the-fold H1
(it delays LCP).
**Credit:** idea inspired by a 21st.dev community component.

## 7. Odometer counters

**Mechanics:** each character is a column that rises out of a blur when the value changes (`key` bound to the
value, 28 ms delay per column). Replaces split-flap tiles, which were judged dated.

## 8. Logo marquees

**Mechanics:** a `translate3d` track driven by rAF, speed that eases down smoothly (0.19 s constant) under the
pointer or focus, copies computed from the width, gradient mask on the edges; static and keyboard-scrollable
with reduced-motion.
**Credit:** idea inspired by a 21st.dev community component.

## 9. Pointer-lit cards

**Mechanics:** a single delegated listener writes `--spot-x/--spot-y` on the hovered card, a `::before` draws a
`radial-gradient`; mouse only (`hover: hover and pointer: fine`).

## 10. A timeline that draws itself

**Mechanics:** `view-timeline-name` on the list, `animation-timeline` on the rail (`scaleY 0 → 1`), cards with
`animation-timeline: view()`, alternating cards that overlap on desktop (`margin-top: -72px`). Zero JS.

## 11. Section photo covers

**Mechanics:** a `clip-path: inset()` that opens and a slow zoom tied to `view()`, a large ghost number, a gradient into the
background. Each section photo is chosen for its meaning (a train platform for contributions, Paris at night for the career path).

## 12. 3D boarding pass

**Mechanics:** tilt via `--tilt-x/--tilt-y`, glare via `--glare-x/--glare-y`, entrance `rotateX(18deg) → 0`.
The owner's real portrait (460 px GitHub avatar).

## 13. Lab console

**Mechanics:** a window with a title bar, a pulsing "running" status, ARIA tabs (left/right arrows),
only the open tab's demo is mounted; the book's "run in the lab" links select the tab
before the portal opens. Demos run on real data pinned to a commit.
