"""Smoke test: the bundled design database answers a real query in every domain the Forge uses."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SEARCH = ROOT / "skills" / "katana-forge" / "vendor" / "ui-ux-pro-max" / "scripts" / "search.py"
QUERIES = [
    ("cinematic dark portfolio", "style"),
    ("luxury editorial", "typography"),
    ("developer tool dark", "color"),
    ("animation reduced motion", "ux"),
]


def main() -> int:
    failures = 0
    for query, domain in QUERIES:
        result = subprocess.run(
            [sys.executable, str(SEARCH), query, "--domain", domain, "-n", "1"],
            capture_output=True,
            text=True,
            encoding="utf-8",
            cwd=SEARCH.parent.parent,
            timeout=60,
            check=False,
        )
        ok = result.returncode == 0 and "Result 1" in result.stdout
        failures += 0 if ok else 1
        print(f"{'PASS' if ok else 'FAIL'} {domain}: {query}")
        if not ok:
            print(result.stdout[-500:], result.stderr[-500:])
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
