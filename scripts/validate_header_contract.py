#!/usr/bin/env python3
from pathlib import Path

css = (Path(__file__).resolve().parents[1] / "styles" / "site-identity.css").read_text(encoding="utf-8")
required = (
    "width: 88px;",
    "min-width: 88px;",
    "@media (max-width: 360px)",
    "width: calc(100% - 16px);",
    ".jl-global-header__actions {\n    gap: var(--jl-space-1);",
    ".jl-header-menu-toggle {\n    min-width: 44px;",
    "font-size: 11px;",
    "right: var(--jl-space-2);",
    "left: var(--jl-space-2);",
)
for fragment in required:
    if fragment not in css:
        raise SystemExit(f"Extreme-compact header contract is incomplete: {fragment}")

compact_block = css.split("@media (max-width: 360px)", 1)[1].split("@media (forced-colors: active)", 1)[0]
if ".jl-site-identity__product" in compact_block and "display: none" in compact_block:
    raise SystemExit("Extreme-compact header must preserve the full product identity.")
if ".jl-site-switcher__button" in compact_block and "display: none" in compact_block:
    raise SystemExit("Extreme-compact header must preserve the Sites control.")

print("Extreme-compact header contract passed.")
