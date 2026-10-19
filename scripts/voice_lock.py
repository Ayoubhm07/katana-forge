"""Voice lock: the English edition reads like a careful human wrote it.

Fails on em dashes, en dashes and emoji in English docs and agents, and on French prose leaking into the
English edition. `docs/fr/`, `README.fr.md` and the vendored database are out of scope by design.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SCOPE = [
    "README.md",
    "CONTRIBUTING.md",
    "CHANGELOG.md",
    "SECURITY.md",
    "NOTICE.md",
    "skills/katana-forge/SKILL.md",
    "skills/katana-forge/PLAN.md",
    "skills/katana-forge/references",
    "agents",
    "commands",
    "examples",
    ".github",
]
DASHES = re.compile("[–—]")
EMOJI = re.compile("[\U0001F300-\U0001FAFF\U00002600-\U000026FF\U00002700-\U000027BF]")
FRENCH = re.compile(r"\b(le|la|les|des|une|est|pour|avec|dans|qui|sur|pas)\b [a-zàâçéèêëîïôûùü]", re.IGNORECASE)
FRENCH_ACCENTS = re.compile("[àâçèêëîïôûùüœ]")
ALLOWED_LINES = ("Version française",)


def files() -> list[Path]:
    found: list[Path] = []
    for entry in SCOPE:
        path = ROOT / entry
        if path.is_file():
            found.append(path)
        elif path.is_dir():
            found.extend(p for p in path.rglob("*") if p.suffix in {".md", ".yml", ".yaml"})
    return found


def main() -> int:
    problems: list[str] = []
    for path in files():
        in_code = False
        for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            if line.strip().startswith("```"):
                in_code = not in_code
            where = f"{path.relative_to(ROOT)}:{number}"
            if DASHES.search(line):
                problems.append(f"{where}: em or en dash")
            if EMOJI.search(line):
                problems.append(f"{where}: emoji")
            if in_code or any(allowed in line for allowed in ALLOWED_LINES):
                continue
            if FRENCH_ACCENTS.search(line) and FRENCH.search(line):
                problems.append(f"{where}: French prose in the English edition")
    if problems:
        print("Voice lock failed:")
        for problem in problems:
            print(f"  - {problem}")
        return 1
    print("Voice lock passed: no dashes, no emoji, no French in the English edition.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
