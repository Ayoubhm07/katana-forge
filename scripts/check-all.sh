#!/usr/bin/env bash
# Runs the same gates as CI, locally, before you push. Usage: bash scripts/check-all.sh
set -euo pipefail
cd "$(dirname "$0")/.."
PY="${PYTHON:-python3}"
command -v "$PY" >/dev/null 2>&1 || PY=python
step() { printf '\n== %s\n' "$1"; }
step "Plugin manifests, agents, skill, plan, ownership"; "$PY" scripts/validate_plugin.py
step "Voice lock"; "$PY" scripts/voice_lock.py
step "SVG gate"; "$PY" scripts/check_svg.py
step "Vendor integrity"; "$PY" scripts/vendor_integrity.py
step "Design database smoke test"; "$PY" scripts/smoke_search.py
if command -v markdownlint-cli2 >/dev/null 2>&1; then step "Markdown lint"; markdownlint-cli2; fi
if command -v typos >/dev/null 2>&1; then step "Spelling"; typos; fi
if command -v shellcheck >/dev/null 2>&1; then step "ShellCheck"; shellcheck install.sh scripts/check-all.sh; fi
if command -v gitleaks >/dev/null 2>&1; then step "Secret scan"; gitleaks detect --no-banner --redact; fi
printf '\nAll local gates passed.\n'
