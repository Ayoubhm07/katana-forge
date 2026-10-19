# Connectors and asset sources

| Connector | Use | How |
|---|---|---|
| **21st.dev MCP** | premium components (decoding text, marquees, timelines, 3D cards) | `mcp__21st__search` (free) then `mcp__21st__get_component` (paid plan = unlimited). Adapt to the design and credit the author in CREDITS.md. `search_logo` can come back empty: use the sources below. |
| **Devicon** | full-color technology logos | `https://cdn.jsdelivr.net/gh/devicons/devicon@v2.16.0/icons/<name>/<name>-original.svg` (variants `plain`, `original-wordmark`). Black logos go on a light badge. |
| **svgl** | brand logos | `curl "https://api.svgl.app?search=<brand>"` (rejects Python urllib, go through curl). |
| **LinkedIn** (signed-in browser) | company and school logos, full project text | `/in/<profile>/details/experience/`, `/details/education/`, `/details/projects/`; grab `img[alt^="Logo"]`. Never open profiles in bulk. |
| **GitHub** | organization logos, verifiable data | `https://github.com/<org>.png?size=160`, `gh api`, `gh pr diff`. |
| **Unsplash** (browser) | free photos | page `/s/photos/<query>?license=free`, record the author and "Unsplash License" from the photo page, download `/photos/<id>/download?w=2000`. |
| **Built-in browser** | visual review, frame-by-frame inspection | `mcp__Claude_Browser__*`; `resize_window` for 375x812 and 1440x900. |
| **gh CLI** | branches, PRs, merge, CI | commits in the owner's name, never any mention of Claude. |
| **Vercel CLI** | deployment, domains | `vercel deploy --prod --yes`; `vercel domains add <domain> <project>`; a `*.vercel.app` alias must be set again after every deployment. Domain purchases are made by the human. |
| **Lighthouse CI** | budgets | `lighthouserc.json` in the repository, run in CI. |
| **Context7 / official docs** | exact APIs | View Transitions, scroll-driven animations, Next.js App Router. |

## 21st.dev MCP configuration (if missing)

Add the 21st.dev server to the Claude Code MCP configuration with the user's personal key,
stored in an environment variable (never written into a repository or into this skill).
