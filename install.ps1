# Manual install of Katana Forge into your user-level Claude Code folder (Windows PowerShell).
# Prefer the plugin route:  /plugin marketplace add Ayoubhm07/katana-forge  then  /plugin install katana-forge@katana-forge
$ErrorActionPreference = "Stop"
$here = Split-Path -Parent $MyInvocation.MyCommand.Path
$target = if ($env:CLAUDE_HOME) { $env:CLAUDE_HOME } else { Join-Path $HOME ".claude" }
foreach ($dir in @("skills", "agents", "commands")) { New-Item -ItemType Directory -Force -Path (Join-Path $target $dir) | Out-Null }
$skill = Join-Path $target "skills\katana-forge"
if (Test-Path $skill) { Remove-Item -Recurse -Force $skill }
Copy-Item -Recurse (Join-Path $here "skills\katana-forge") $skill
Copy-Item (Join-Path $here "agents\katana-*.md") (Join-Path $target "agents")
Copy-Item (Join-Path $here "commands\forge.md") (Join-Path $target "commands\forge.md")
Write-Output "Katana Forge installed in $target. Open Claude Code and type /forge or /katana-forge."
