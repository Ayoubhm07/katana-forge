"""Vendor integrity: the bundled third-party database is byte for byte what was reviewed.

`vendor.lock.json` stores the SHA-256 of every vendored file. Any change, addition or removal fails CI
until someone re-reviews it and runs `python scripts/vendor_integrity.py --update` in the same pull request.
"""

from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
VENDOR = ROOT / "skills" / "katana-forge" / "vendor"
LOCK = ROOT / "vendor.lock.json"


def digest(path: Path) -> str:
    data = path.read_bytes().replace(b"\r\n", b"\n")
    return hashlib.sha256(data).hexdigest()


def current() -> dict[str, str]:
    return {
        path.relative_to(ROOT).as_posix(): digest(path)
        for path in sorted(VENDOR.rglob("*"))
        if path.is_file() and "__pycache__" not in path.parts
    }


def main() -> int:
    state = current()
    if "--update" in sys.argv:
        LOCK.write_text(json.dumps(state, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        print(f"vendor.lock.json updated: {len(state)} files.")
        return 0
    locked = json.loads(LOCK.read_text(encoding="utf-8"))
    changed = sorted(k for k in state.keys() & locked.keys() if state[k] != locked[k])
    added = sorted(state.keys() - locked.keys())
    removed = sorted(locked.keys() - state.keys())
    if changed or added or removed:
        print("Vendor integrity failed:")
        for label, items in (("changed", changed), ("added", added), ("removed", removed)):
            for item in items:
                print(f"  - {label}: {item}")
        return 1
    print(f"Vendor integrity passed: {len(state)} files match vendor.lock.json.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
