"""Validate the Katana Forge plugin: manifests, front matter, cross references and versions.

Standard library only, so it runs anywhere Python 3.10+ runs. Exit code 1 on any error.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILL_DIR = ROOT / "skills" / "katana-forge"
AGENTS_DIR = ROOT / "agents"
COMMANDS_DIR = ROOT / "commands"
EXPECTED_AGENTS = {"shogun", "kage", "sensei", "sumi", "kaze", "tetsu", "mamori", "kensa"}
NAME_PATTERN = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
SEMVER = re.compile(r"^\d+\.\d+\.\d+$")
ALLOWED_TOOLS = {"Read", "Grep", "Glob", "Bash", "Write", "Edit", "Agent", "WebFetch", "WebSearch"}
OWNER = "Ayoub Hammoudi"

errors: list[str] = []


def fail(message: str) -> None:
    errors.append(message)


def front_matter(path: Path) -> dict[str, str]:
    """Parse the simple `key: value` front matter used by skills, agents and commands."""
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        fail(f"{path.relative_to(ROOT)}: missing front matter")
        return {}
    end = text.find("\n---\n", 4)
    if end == -1:
        fail(f"{path.relative_to(ROOT)}: unterminated front matter")
        return {}
    data: dict[str, str] = {}
    for line in text[4:end].splitlines():
        if not line.strip():
            continue
        key, sep, value = line.partition(":")
        if not sep:
            fail(f"{path.relative_to(ROOT)}: bad front matter line {line!r}")
            continue
        value = value.strip()
        if value.startswith('"'):
            try:
                value = json.loads(value)
            except json.JSONDecodeError:
                fail(f"{path.relative_to(ROOT)}: description is not a valid quoted string")
        elif ": " in value:
            fail(f"{path.relative_to(ROOT)}: unquoted value for {key!r} contains ': ' (breaks YAML)")
        data[key.strip()] = value
    return data


def check_manifests() -> str:
    plugin = json.loads((ROOT / ".claude-plugin" / "plugin.json").read_text(encoding="utf-8"))
    market = json.loads((ROOT / ".claude-plugin" / "marketplace.json").read_text(encoding="utf-8"))
    for key in ("name", "version", "description", "author", "license", "repository"):
        if key not in plugin:
            fail(f"plugin.json: missing {key}")
    if plugin.get("name") != "katana-forge":
        fail("plugin.json: name must be katana-forge")
    if not SEMVER.match(plugin.get("version", "")):
        fail("plugin.json: version must be semver")
    if plugin.get("author", {}).get("name") != OWNER:
        fail(f"plugin.json: author must be {OWNER}")
    if market.get("owner", {}).get("name") != OWNER:
        fail(f"marketplace.json: owner must be {OWNER}")
    entries = market.get("plugins", [])
    if len(entries) != 1 or entries[0].get("name") != "katana-forge":
        fail("marketplace.json: must list exactly the katana-forge plugin")
    elif entries[0].get("version") != plugin.get("version"):
        fail("marketplace.json: plugin version differs from plugin.json")
    if market.get("metadata", {}).get("version") != plugin.get("version"):
        fail("marketplace.json: metadata.version differs from plugin.json")
    return plugin.get("version", "")


def check_skill() -> None:
    meta = front_matter(SKILL_DIR / "SKILL.md")
    if meta.get("name") != "katana-forge":
        fail("SKILL.md: name must be katana-forge")
    description = meta.get("description", "")
    if not 100 <= len(description) <= 1024:
        fail(f"SKILL.md: description length {len(description)} outside 100..1024")
    body = (SKILL_DIR / "SKILL.md").read_text(encoding="utf-8")
    for agent in EXPECTED_AGENTS:
        if f"katana-{agent}" not in body:
            fail(f"SKILL.md: team table does not mention katana-{agent}")
    for ref in re.findall(r"`(references/[\w./-]+\.md)`", body):
        if not (SKILL_DIR / ref).exists():
            fail(f"SKILL.md: referenced file {ref} does not exist")
    plan = (SKILL_DIR / "PLAN.md").read_text(encoding="utf-8")
    for agent in EXPECTED_AGENTS:
        if f"katana-{agent}" not in plan:
            fail(f"PLAN.md: no wave assigns katana-{agent}")
    for ref in set(re.findall(r"(references/[\w-]+\.md)", plan)):
        if not (SKILL_DIR / ref).exists():
            fail(f"PLAN.md: referenced file {ref} does not exist")


def check_agents() -> None:
    found = set()
    for path in sorted(AGENTS_DIR.glob("*.md")):
        meta = front_matter(path)
        name = meta.get("name", "")
        if path.stem != name:
            fail(f"{path.name}: name {name!r} does not match file name")
        if not NAME_PATTERN.match(name) or not name.startswith("katana-"):
            fail(f"{path.name}: invalid agent name {name!r}")
        found.add(name.removeprefix("katana-"))
        if len(meta.get("description", "")) < 80:
            fail(f"{path.name}: description too short to route the agent")
        tools = json.loads(meta.get("tools", "[]"))
        unknown = set(tools) - ALLOWED_TOOLS
        if unknown:
            fail(f"{path.name}: unknown tools {sorted(unknown)}")
        if meta.get("model") not in {"inherit", "sonnet", "opus", "haiku"}:
            fail(f"{path.name}: unexpected model {meta.get('model')!r}")
    if found != EXPECTED_AGENTS:
        fail(f"agents: expected {sorted(EXPECTED_AGENTS)}, found {sorted(found)}")


def check_commands() -> None:
    for path in COMMANDS_DIR.glob("*.md"):
        meta = front_matter(path)
        if not meta.get("description"):
            fail(f"{path.name}: missing description")
        if "$ARGUMENTS" not in path.read_text(encoding="utf-8"):
            fail(f"{path.name}: does not pass $ARGUMENTS")


def check_changelog(version: str) -> None:
    changelog = (ROOT / "CHANGELOG.md").read_text(encoding="utf-8")
    if f"## {version}" not in changelog:
        fail(f"CHANGELOG.md: no entry for version {version}")


def check_ownership() -> None:
    license_text = (ROOT / "LICENSE").read_text(encoding="utf-8")
    if f"Copyright (c)" not in license_text or OWNER not in license_text:
        fail(f"LICENSE: copyright must name {OWNER}")
    codeowners = (ROOT / ".github" / "CODEOWNERS").read_text(encoding="utf-8")
    if "@Ayoubhm07" not in codeowners:
        fail("CODEOWNERS: @Ayoubhm07 must own the repository")
    if OWNER not in (ROOT / "README.md").read_text(encoding="utf-8"):
        fail(f"README.md: must credit {OWNER}")


def main() -> int:
    version = check_manifests()
    check_skill()
    check_agents()
    check_commands()
    check_changelog(version)
    check_ownership()
    if errors:
        print("Plugin validation failed:")
        for message in errors:
            print(f"  - {message}")
        return 1
    print(f"Plugin valid: katana-forge {version}, {len(EXPECTED_AGENTS)} agents, manifests, skill, plan, commands, ownership.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
