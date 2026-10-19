# Security policy

Katana Forge is created and maintained by **Ayoub Hammoudi** ([@Ayoubhm07](https://github.com/Ayoubhm07)).

## Reporting a vulnerability

Please do not open a public issue. Use GitHub's private vulnerability reporting on this repository
(Security tab, "Report a vulnerability"). You will get an acknowledgement within 72 hours and a fix or
mitigation plan within 14 days for confirmed issues.

## What is in scope

- The plugin manifests, agents, skill and command files (prompt injection paths, unsafe instructions).
- The installers (`install.sh`, `install.ps1`).
- The reference implementation and SVG assets (script injection, unsafe DOM usage).
- The CI and release workflows (supply chain, token permissions).

## How this repository protects itself

- `main` only moves through reviewed pull requests with every required check green.
- Every GitHub Action is pinned to a full commit SHA and updated by Dependabot.
- Workflows run with read-only tokens by default, hardened runners and no persisted credentials.
- Secret scanning (Gitleaks) on the full history, CodeQL, OpenSSF Scorecard, zizmor workflow audit,
  dependency review, an SVG gate that rejects scripts and external references, and a SHA-256 lock on vendored files.
- Releases ship with SHA-256 checksums and signed build provenance attestations.
