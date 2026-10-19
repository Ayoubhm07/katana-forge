# Case study: forging ayoubhammoudi.com

This is the real project the Forge was built on: a personal site that is live at <https://ayoubhammoudi.com>. Its source code is private and is not part of this repository. Every move, budget and rule in this skill was first paid for here, over two days (2026-10-18 and 2026-10-19).

What the Forge actually did, in order, with what the owner said at each step.
It is the proof that the method works, and the list of human reactions to anticipate.

| Step | Shipped | Owner's reaction | Lesson |
|---|---|---|---|
| Harvest | LinkedIn, GitHub, FR/EN resume, old site (73 characters of readable HTML) in `.war-room/harvest/` | "put everything in memory" | the harvest comes before everything; conflicts listed and settled by him |
| S0 to S5 | locked content (zod, sources, truth tests), pages readable without JS, 3 demos on real data, Lighthouse CI, resume with phone number | "but what is this design? beginner level" | rigor is invisible: you need visible spectacle |
| S6 | fonts: CLS 0.33 in production fixed (block + optional) | | measure production |
| S7 | Unsplash photos everywhere, portrait, 3D boarding pass, orbit, coverflow, WebGL globe, page-turn transitions | "great but not enough", menu without project names, split-flap tiles "ugly", Phantera image "meaningless" | every image must signify its subject; remove the basic stuff |
| S8 | colorful splash that dives into the screen, 3D book that opens, portal transition, real logos (LinkedIn, GitHub), tabbed lab, blog (4 articles verified against the diffs), white tiger + logo for Phantera | "merged!" | the book and the splash won him over |
| S8 perf | perf 0.92: splash moved out of React into a static SVG, Suspense per section | | weight creeps back fast, cut before adding |
| S9 | avatar dancing under the book | "an avatar with aura, not a little boy", "a man with a katana who slices the screen" | a character needs aura; one strong gesture beats a dance |
| S9 bis | swordsman who splits the screen of the 12 other projects, galaxy of 43 skills drawn from the 15 LinkedIn projects (vortex, hyperspace), related-article images fixed | "merged!" | a single entry point to the flagship section sticks in people's minds |
| Content | hackathon then award removed, FirstDown Tech corrected (not Spar-X) | | the owner corrects the facts: record his corrections |
| Domain | ayoubhammoudi.com bought by him on Vercel, connected, www and old alias on 301 | "okay cool!!" | the human pays, the Forge connects and verifies |

## What impressed (reproduce it)

- A real object that opens (the book) rather than a carousel.
- An opening that tells a story (you enter the creator's screen).
- A character with aura making a gesture loaded with meaning (slicing the screen to reveal what comes next).
- A visualization where every element is tied to evidence (skill to project).
- Real logos and real photos, wherever they carry meaning.

## What was rejected (never do it again)

- A sober, "correct" design without images or 3D.
- Split-flap tiles for headings.
- Project names in the menu.
- A decorative image unrelated to the subject.
- A cute dancing character.
