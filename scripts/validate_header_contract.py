#!/usr/bin/env python3
from pathlib import Path

css = (Path(__file__).resolve().parents[1] / "styles" / "site-identity.css").read_text(encoding="utf-8")
required = (
    "grid-template-columns: 136px var(--jl-control-height-md);",
    "width: 136px;",
    "min-width: 136px;",
    "@media (max-width: 420px)",
    "width: calc(100% - 8px);",
    "grid-template-columns: 116px 40px;",
    "width: 116px;",
    "min-width: 116px;",
    ".jl-global-header__actions {\n    gap: calc(var(--jl-space-1) / 2);",
    ".jl-header-menu-toggle {\n    min-width: 40px;",
    "font-size: 11.5px;",
    "white-space: nowrap;",
)
for fragment in required:
    if fragment not in css:
        raise SystemExit(f"Extreme-compact header contract is incomplete: {fragment}")

compact_block = css.split("@media (max-width: 420px)", 1)[1].split("@media (forced-colors: active)", 1)[0]
if ".jl-site-identity__product" in compact_block and "display: none" in compact_block:
    raise SystemExit("Extreme-compact header must preserve the full product identity.")
if ".jl-site-switcher__button" in compact_block and "display: none" in compact_block:
    raise SystemExit("Extreme-compact header must preserve the Sites control.")

print("Extreme-compact header contract passed.")
