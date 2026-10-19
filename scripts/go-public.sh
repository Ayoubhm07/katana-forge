#!/usr/bin/env bash
# Run once, by the owner, the day Katana Forge goes public. Turns on every protection GitHub offers
# to public repositories. Requires an authenticated gh CLI with admin rights on the repository.
set -euo pipefail
REPO="${REPO:-Ayoubhm07/katana-forge}"
cd "$(dirname "$0")/.."
gh repo edit "$REPO" --visibility public --accept-visibility-change-consequences
gh api -X POST "repos/$REPO/rulesets" --input .github/rulesets/protect-main.json >/dev/null
gh api -X PUT "repos/$REPO/private-vulnerability-reporting" >/dev/null
gh api -X PUT "repos/$REPO/vulnerability-alerts" >/dev/null
gh api -X PUT "repos/$REPO/automated-security-fixes" >/dev/null
gh api -X PATCH "repos/$REPO" --input - >/dev/null <<'JSON'
{ "security_and_analysis": { "secret_scanning": { "status": "enabled" }, "secret_scanning_push_protection": { "status": "enabled" } },
  "delete_branch_on_merge": true, "allow_merge_commit": false, "allow_rebase_merge": false, "allow_squash_merge": true }
JSON
echo "$REPO is public and protected: ruleset on main, secret scanning with push protection, private vulnerability reporting, Dependabot."
