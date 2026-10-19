# Connecteurs et sources d'assets

| Connecteur | Usage | Comment |
|---|---|---|
| **21st.dev MCP** | composants premium (texte qui se décode, frises, timelines, cartes 3D) | `mcp__21st__search` (gratuit) puis `mcp__21st__get_component` (offre payante = illimité). Adapter au design, créditer l'auteur dans CREDITS.md. `search_logo` peut renvoyer vide : utiliser les sources ci-dessous. |
| **Devicon** | logos de technologies en couleur | `https://cdn.jsdelivr.net/gh/devicons/devicon@v2.16.0/icons/<nom>/<nom>-original.svg` (variantes `plain`, `original-wordmark`). Les logos noirs se posent sur un badge clair. |
| **svgl** | logos de marques | `curl "https://api.svgl.app?search=<marque>"` (refuse urllib Python, passer par curl). |
| **LinkedIn** (navigateur connecté) | logos d'entreprises et d'écoles, texte intégral des projets | `/in/<profil>/details/experience/`, `/details/education/`, `/details/projects/` ; récupérer `img[alt^="Logo"]`. Ne jamais ouvrir des profils en série. |
| **GitHub** | logos d'organisations, données vérifiables | `https://github.com/<org>.png?size=160`, `gh api`, `gh pr diff`. |
| **Unsplash** (navigateur) | photos libres | page `/s/photos/<requête>?license=free`, relever l'auteur et « Unsplash License » sur la page de la photo, télécharger `/photos/<id>/download?w=2000`. |
| **Navigateur intégré** | revue visuelle, inspection image par image | `mcp__Claude_Browser__*` ; `resize_window` pour 375x812 et 1440x900. |
| **gh CLI** | branches, PR, merge, CI | commits au nom du propriétaire, jamais de mention de Claude. |
| **Vercel CLI** | déploiement, domaines | `vercel deploy --prod --yes` ; `vercel domains add <domaine> <projet>` ; un alias `*.vercel.app` doit être reposé après chaque déploiement. L'achat de domaine se fait par l'humain. |
| **Lighthouse CI** | budgets | `lighthouserc.json` dans le dépôt, exécuté en CI. |
| **Context7 / docs officielles** | API exactes | View Transitions, scroll-driven animations, Next.js App Router. |

## Configuration MCP 21st.dev (si absente)

Ajouter le serveur 21st.dev dans la configuration MCP de Claude Code avec la clé personnelle de l'utilisateur,
stockée dans une variable d'environnement (jamais écrite dans un dépôt ni dans ce skill).
