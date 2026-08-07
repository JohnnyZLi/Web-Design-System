#!/usr/bin/env python3
from pathlib import Path

root = Path(__file__).resolve().parents[1]
css_path = root / "styles" / "site-identity.css"
validator_path = root / "scripts" / "validate_header_contract.py"

css = css_path.read_text(encoding="utf-8")

old_link = """.jl-site-menu a {\n  width: 100%;\n  min-width: 0;\n  min-height: calc(var(--jl-control-height-md) - 6px);\n  box-sizing: border-box;\n  display: flex;\n  align-items: center;\n  padding: 5px 6px;\n  border-radius: var(--jl-radius-sm);\n  text-decoration: none;\n  line-height: 1.15;\n  overflow-wrap: normal;\n  white-space: normal;\n}\n"""
new_link = """.jl-site-menu a {\n  width: 100%;\n  min-width: 0;\n  min-height: calc(var(--jl-control-height-md) - 6px);\n  box-sizing: border-box;\n  display: flex;\n  align-items: center;\n  justify-content: center;\n  padding: 5px 6px;\n  border-radius: var(--jl-radius-sm);\n  text-align: center;\n  text-decoration: none;\n  line-height: 1.15;\n  overflow-wrap: normal;\n  white-space: normal;\n}\n"""
if old_link not in css:
    raise SystemExit("Expected Sites link block was not found.")
css = css.replace(old_link, new_link, 1)

anchor = """.jl-site-menu a:focus-visible {\n  outline: none;\n  outline-offset: 0;\n  box-shadow: inset 0 0 0 2px var(--jl-color-focus-ring);\n}\n\n"""
motion = """@media (prefers-reduced-motion: no-preference) {\n  .jl-site-menu:not([hidden]),\n  .jl-settings-menu:not([hidden]) {\n    transform-origin: top center;\n    animation: jl-attached-menu-lower 190ms cubic-bezier(0.2, 0.8, 0.2, 1) both;\n  }\n}\n\n@keyframes jl-attached-menu-lower {\n  from {\n    opacity: 0;\n    transform: translateY(-7px) scaleY(0.97);\n  }\n\n  to {\n    opacity: 1;\n    transform: translateY(0) scaleY(1);\n  }\n}\n\n"""
if anchor not in css:
    raise SystemExit("Expected Sites focus block was not found.")
if "@keyframes jl-attached-menu-lower" not in css:
    css = css.replace(anchor, anchor + motion, 1)

css_path.write_text(css, encoding="utf-8")

validator = validator_path.read_text(encoding="utf-8")
needle = '    "white-space: normal;",\n'
addition = (
    '    "justify-content: center;",\n'
    '    "text-align: center;",\n'
    '    "@keyframes jl-attached-menu-lower",\n'
    '    "animation: jl-attached-menu-lower 190ms cubic-bezier(0.2, 0.8, 0.2, 1) both;",\n'
)
if needle not in validator:
    raise SystemExit("Expected validator anchor was not found.")
if '"@keyframes jl-attached-menu-lower"' not in validator:
    validator = validator.replace(needle, needle + addition, 1)
validator_path.write_text(validator, encoding="utf-8")
