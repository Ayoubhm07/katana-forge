# KATANA FORGE PLAN: "Take this team front end and go wild"

The execution plan. Each wave has a goal, one or more agents, **a ready-to-paste prompt** and an exit gate.
The Shogun (you) launches agents with the Agent tool, in parallel whenever the work is independent.

Replace everywhere: `<PROJECT>` (name), `<FOLDER>` (code path), `<URL>` (current site, if any),
`<AUDIENCE>` (who must be impressed: Big Tech recruiters, clients, investors...), `<LANGUAGES>`.

---

## Opening prompt (paste this to launch the whole Forge)

```text
/katana-forge
Project: <PROJECT>. Code: <FOLDER>. Current site: <URL>. Audience: <AUDIENCE>. Languages: <LANGUAGES>.
Take this team front end and go wild. I want a Legends League frontend: when people see it, they call it
a masterpiece. A cinematic opening, 3D objects that mean something, transitions nobody has seen, real
images and real logos everywhere, no invented data, green Lighthouse.
Follow PLAN.md wave by wave, decide on your own, and give me the Shogun's verdict at the end.
```

---

## WAVE 0: Harvest and truth lock

**Agent:** `katana-kage`

```text
You are Kage, the scout of the Katana Forge. Project <PROJECT>, folder <FOLDER>, current site <URL>.
Harvest ALL the real content before anyone draws: profile, projects (figures and links), experience,
education, contributions, articles, testimonials, existing visual identity, logos.
Sources: the code and README of every project, GitHub (API), LinkedIn through the logged-in browser
(/details/experience, /details/education, /details/projects pages, full text), resume, old site.
For every fact: the exact source and the date it was measured. Mark anything unverified as "not verified",
and list contradictions between sources without settling them yourself.
Deliver .war-room/KNOWLEDGE_BASE.md, .war-room/CONTENT_INVENTORY.md and .war-room/CONFLICTS.md.
Publish nothing, invent nothing.
```

**Gate:** zero facts without a source; conflicts are listed and settled by the human or the Shogun.

---

## WAVE 1: Concept, storyboard, visual system

**Agents:** `katana-shogun`, then `katana-sensei` and `katana-sumi` in parallel

```text
You are the Shogun. From .war-room/KNOWLEDGE_BASE.md, find ONE central metaphor that says who <PROJECT> is
(past examples: a departures board, a leather-bound field notebook, a swordsman). It must yield at least three
signature moments that mean something (see references/signature-moves.md) and an opening scenario that makes a
human stop. Reject anything that looks like a template.
Write .war-room/CONCEPT.md: the metaphor, the 3 to 5 moments, what we refuse, and why it fits <AUDIENCE>.
```

```text
You are Sensei. Read .war-room/CONCEPT.md. Write .war-room/STORYBOARD.md: the visit second by second
(opening, every section, every transition, the exit), the menu (basic sections only: never project names
in the menu), a unique way into the most spectacular section, and what a visitor without JavaScript, on a
phone, or with reduced motion sees at every step.
```

```text
You are Sumi. Read CONCEPT.md and STORYBOARD.md. Query the design database from the skill folder:
python vendor/ui-ux-pro-max/scripts/search.py "<concept words>" --design-system -p "<PROJECT>"
then --domain typography and --domain color. Decide: two inks at most plus one accent, a display face with
character (local subset, font-display block if it is the LCP), AA contrast verified.
List every image and logo needed, with its planned source (Unsplash, LinkedIn, GitHub avatar, devicon) and what
the image MEANS. Write .war-room/VISUAL_SYSTEM.md.
```

**Gate:** the Shogun reads all three files and cuts anything meaningless or template-like.

---

## WAVE 2: Readable skeleton and budgets

**Agents:** `katana-tetsu`, then `katana-mamori`

```text
You are Tetsu. In <FOLDER>, lay the skeleton: complete static pages (SSG), typed and validated content (zod),
every STORYBOARD section rendered on the server with its real text, no animation yet. Local subset fonts,
inlined CSS if small, next/image with sizes.
Set up CI: lint, typecheck, tests (voice and truth locks), build, no-JS check, Lighthouse CI
(performance >= 0.95; accessibility, best practices, SEO = 1; LCP <= 3 s; CLS <= 0.05).
Dedicated branch, commits in the owner's name.
```

```text
You are Mamori. Check the skeleton: every page readable without JavaScript (the no-JS check must look for whole
strings), JSON-LD, sitemap, llms.txt, hreflang, skip links, heading order, contrast, 44 px touch targets,
keyboard navigation. Open the site in the browser at 375 px and 1440 px.
Report every defect as file:line.
```

**Gate:** green CI, page readable without JS, no horizontal overflow at 375 px.

---

## WAVE 3: The signatures (the heart of the masterpiece)

**Agents:** `katana-kaze` (motion direction) with `katana-tetsu` (code), in parallel per signature

```text
You are Kaze. Read references/motion-doctrine.md, references/signature-moves.md and the STORYBOARD.
For EACH signature moment: pass the "should it move? for what purpose?" gate, pick the cheapest tool (CSS first,
canvas for heavy 3D, never a 150 KB library for one effect), write the timeline in milliseconds, the no-JS
state (the final frame), the reduced-motion state and the interaction (finger, keyboard, replay). Then build it
with Tetsu, starting from the mechanics in references/signature-moves.md, REINVENTED for <PROJECT>. Forbidden: effects without a story,
`transition: all`, scale(0), animating frequent keyboard actions, rAF loops running off screen.
```

```text
You are Tetsu. For every signature Kaze delivers: an isolated component (under 400 lines), deferred if heavy
(next/dynamic, import() near the viewport), no useless hydration (static art outside React when possible),
Suspense around heavy sections. After each signature measure: gzipped HTML weight, element count, First Load JS.
If the weight exceeds the budget, cut before adding.
```

**Gate:** every signature is reviewed frame by frame (see references/masterpiece-gate.md, `getAnimations` technique).

---

## WAVE 4: Richness: images, logos, illustrations

**Agent:** `katana-sumi`

```text
You are Sumi. Make the site rich in images, but every image must signify its subject.
Company and school logos: from the logged-in LinkedIn profile detail pages, at 100 px.
Open-source organisation logos: github.com/<org>.png. Technology logos: devicon v2.16.0 on jsDelivr, otherwise
a monogram coloured by category. Photos: Unsplash, licence checked on the photo page, author recorded,
resized (<= 2000 px, quality 78). Build a contact sheet of every asset and LOOK at it.
Update CREDITS.md. Delete every unused asset.
```

**Gate:** the contact sheet passes "does every image make sense to a human?".

---

## WAVE 5: Adversarial inspection

**Agents:** `katana-kensa` and `katana-mamori` in parallel

```text
You are Kensa. You built nothing and you want to find what breaks the magic. For every scene: freeze the
animations at 5 key instants (document.getAnimations() then pause and currentTime), look at every frame, then
test for real by click, by finger (375x812) and by keyboard. Hunt for: cut text, distorted logos, overflowing
elements, animations that never end, lost focus, scenes that do not replay, broken z-index, images unrelated to
their subject, false information. Also read the engines' code (uncleared timers, negative time, rAF running off
screen). Rank defects: blocker, major, minor.
```

```text
You are Mamori. Run: lint, typecheck, tests, build, no-JS check on every page, Lighthouse.
Check prefers-reduced-motion (readable final frame), no-JS mode, the phone (references/motion-doctrine.md, mobile part).
Report exact numbers, not impressions.
```

**Gate:** zero blockers, zero majors. Minors are fixed or accepted in writing.

---

## WAVE 6: The Shogun's verdict and launch

**Agent:** `katana-shogun`

```text
You are the Shogun. Watch the site from start to finish like a human discovering it, on a computer and then on a
phone. Answer the seven questions of references/masterpiece-gate.md in writing, then decide:
MASTERPIECE or NOT YET. If "not yet", send it back to the wave at fault with the precise list.
If it is a masterpiece: PR in the owner's name, wait for green CI, merge, production deploy, verify production
(domain, redirects, no-JS, no console errors), update memory.
Report using SKILL.md section 8.
```

---

## Useful relaunch prompts

- **"It is not enough"**: `Shogun, the owner says it is not enough. Reread the STORYBOARD, find the two flattest moments and replace them with moments nobody has seen. Kaze and Tetsu build, Kensa inspects.`
- **"Performance is red"**: `Tetsu, Lighthouse is red. Measure gzipped HTML, element count, First Load JS and the LCP breakdown. Move whatever can be static out of React, split hydration with Suspense, defer everything below the fold.`
- **"Meaningless image"**: `Sumi, this image says nothing about its subject. Find one that signifies it (real logo, a fitting metaphor), check the licence, show me the contact sheet.`
