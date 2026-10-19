"""SVG gate: every SVG in the repository is well formed and inert.

An SVG is an executable document in a browser. Fails on any script element, event handler attribute,
javascript: URL, foreignObject or external reference (http, https, protocol-relative, data: other than images).
"""

from __future__ import annotations

import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKIP = {".git", "node_modules"}
EVENT_ATTR = re.compile(r"^on[a-z]+$", re.IGNORECASE)
EXTERNAL = re.compile(r"^\s*(https?:|//|javascript:)", re.IGNORECASE)
HREF_KEYS = {"href", "{http://www.w3.org/1999/xlink}href", "src"}


def local(tag: str) -> str:
    return tag.split("}", 1)[-1].lower()


def check(path: Path) -> list[str]:
    where = path.relative_to(ROOT)
    try:
        tree = ET.parse(path)
    except ET.ParseError as error:
        return [f"{where}: not well formed ({error})"]
    problems: list[str] = []
    for element in tree.iter():
        tag = local(element.tag)
        if tag in {"script", "foreignobject", "iframe", "embed", "object"}:
            problems.append(f"{where}: forbidden <{tag}> element")
        for key, value in element.attrib.items():
            name = local(key)
            if EVENT_ATTR.match(name):
                problems.append(f"{where}: event handler attribute {name}")
            if key in HREF_KEYS or name in {"href", "src"}:
                if EXTERNAL.match(value):
                    problems.append(f"{where}: external reference {value[:60]}")
                if value.strip().lower().startswith("data:") and not value.strip().lower().startswith("data:image/"):
                    problems.append(f"{where}: non-image data URL")
    return problems


def main() -> int:
    svgs = [p for p in ROOT.rglob("*.svg") if not SKIP.intersection(p.parts)]
    problems = [problem for svg in svgs for problem in check(svg)]
    if problems:
        print("SVG gate failed:")
        for problem in problems:
            print(f"  - {problem}")
        return 1
    print(f"SVG gate passed: {len(svgs)} SVG files, well formed, no scripts, no handlers, no external references.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
