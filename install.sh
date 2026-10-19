#!/usr/bin/env bash
# Manual install of Katana Forge into your user-level Claude Code folder.
# Prefer the plugin route:  /plugin marketplace add Ayoubhm07/katana-forge  then  /plugin install katana-forge@katana-forge
set -euo pipefail
HERE="$(cd "$(dirname "$0")" && pwd)"
TARGET="${CLAUDE_HOME:-$HOME/.claude}"
mkdir -p "$TARGET/skills" "$TARGET/agents" "$TARGET/commands"
rm -rf "$TARGET/skills/katana-forge"
cp -R "$HERE/skills/katana-forge" "$TARGET/skills/katana-forge"
cp "$HERE"/agents/katana-*.md "$TARGET/agents/"
cp "$HERE/commands/forge.md" "$TARGET/commands/forge.md"
echo "Katana Forge installed in $TARGET. Open Claude Code and type /forge or /katana-forge."
