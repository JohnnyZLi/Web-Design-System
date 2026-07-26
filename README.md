# Johnny Li Web Design System

[![Validate](https://github.com/JohnnyZLi/Web-Design-System/actions/workflows/validate.yml/badge.svg)](https://github.com/JohnnyZLi/Web-Design-System/actions/workflows/validate.yml)

A shared UI and UX system for `johnnyli.dev`, `network.johnnyli.dev`, and `rolepacket.johnnyli.dev`.

**Version:** 1.3.2  
**Status:** Implementation candidate  
**License:** All rights reserved

The system is derived from all three websites:

- The portfolio supplies the palette, editorial typography, exact dot texture, open layout, and restrained terracotta treatment.
- Network Diagnostics supplies analytical controls, measurements, charts, and data-density patterns.
- RolePacket supplies workflow panels, application rows, review states, and comparison patterns.
- Shared accessibility, focus, semantic borders, token generation, and validation complete the system.

## Use

```bash
make generate   # regenerate tokens/tokens.css
make validate   # validate tokens, contrast, links, specimen, and public safety
make serve      # preview http://localhost:8000/specimen/
make release    # generate a consolidated Markdown release and ZIP in dist/
```

Start with:

- [`specimen/index.html`](specimen/index.html) — visual reference
- [`docs/DESIGN-SYSTEM.md`](docs/DESIGN-SYSTEM.md) — permanent rules
- [`docs/MIGRATION.md`](docs/MIGRATION.md) — high-level rollout plan
- [`tokens/tokens.tokens.json`](tokens/tokens.tokens.json) — sole editable token source

## Structure

```text
.
├── README.md
├── LICENSE
├── CHANGELOG.md
├── Makefile
├── tokens/
├── specimen/
├── scripts/
├── docs/
├── ci/
└── .github/
```

The repository is public, but public visibility does not grant permission to reuse the work. See `LICENSE`.

## Security

The repository validates release contents, CSS override syntax, common secret patterns, private network addresses, local home-directory paths, and sensitive filenames. Report vulnerabilities privately as described in [`SECURITY.md`](SECURITY.md).
