#!/usr/bin/env python3
from pathlib import Path

css_path = Path('styles/site-identity.css')
css = css_path.read_text()
replacements = [
    ('grid-template-columns: 88px var(--jl-control-height-md);', 'grid-template-columns: 104px var(--jl-control-height-md);'),
    ('  width: 88px;\n  height: var(--jl-control-height-md);\n  min-width: 88px;', '  width: 104px;\n  height: var(--jl-control-height-md);\n  min-width: 104px;'),
    ('  gap: var(--jl-space-1);\n  margin: 0;', '  gap: calc(var(--jl-space-1) / 2);\n  margin: 0;'),
    ('  width: 88px;\n  min-width: 88px;\n  box-sizing: border-box;\n  grid-column: 1;', '  width: 104px;\n  min-width: 104px;\n  box-sizing: border-box;\n  grid-column: 1;'),
    ('  min-height: calc(var(--jl-control-height-md) - var(--jl-space-1));', '  min-height: calc(var(--jl-control-height-md) - 6px);'),
    ('  padding: var(--jl-space-1);\n  border-radius: var(--jl-radius-sm);\n  text-decoration: none;\n  line-height: 1.2;', '  padding: 5px 6px;\n  border-radius: var(--jl-radius-sm);\n  text-decoration: none;\n  line-height: 1.15;'),
    ('    grid-template-columns: 88px 40px;\n    grid-template-rows: 40px auto;', '    grid-template-columns: 104px 40px;\n    grid-template-rows: 40px auto;'),
    ('  .jl-site-menu a {\n    min-height: 36px;\n    padding: 6px;\n  }', '  .jl-site-menu a {\n    min-height: 34px;\n    padding: 5px 6px;\n  }'),
    ('    grid-template-columns: 88px 40px;\n    column-gap: calc(var(--jl-space-1) / 2);', '    grid-template-columns: 104px 40px;\n    column-gap: calc(var(--jl-space-1) / 2);'),
    ('  .jl-site-switcher__button {\n    width: 88px;\n    min-width: 88px;\n  }', '  .jl-site-switcher__button {\n    width: 104px;\n    min-width: 104px;\n  }'),
    ('  .jl-site-menu a {\n    padding: 4px;\n  }', '  .jl-site-menu a {\n    padding: 4px 6px;\n  }'),
    ('  .jl-site-switcher {\n    column-gap: 0;\n  }\n\n}', '  .jl-site-switcher {\n    grid-template-columns: 96px 40px;\n    column-gap: 0;\n  }\n\n  .jl-site-switcher__button,\n  .jl-site-menu {\n    width: 96px;\n    min-width: 96px;\n  }\n\n}'),
]
for old, new in replacements:
    if old not in css:
        raise SystemExit(f'Expected CSS fragment not found:\n{old}')
    css = css.replace(old, new, 1)
css_path.write_text(css)

validator_path = Path('scripts/validate_header_contract.py')
v = validator_path.read_text()
v = v.replace('"grid-template-columns: 88px var(--jl-control-height-md);",', '"grid-template-columns: 104px var(--jl-control-height-md);",')
v = v.replace('".jl-site-switcher__button {\\n  width: 88px;",', '".jl-site-switcher__button {\\n  width: 104px;",')
v = v.replace('"min-width: 88px;",', '"min-width: 104px;",', 1)
v = v.replace('".jl-site-menu {\\n  width: 88px;",', '".jl-site-menu {\\n  width: 104px;",')
v = v.replace('"grid-template-columns: 88px 40px;",', '"grid-template-columns: 104px 40px;",')
v = v.replace('    ".jl-header-menu-toggle {\\n    min-width: 40px;",\n)', '    ".jl-header-menu-toggle {\\n    min-width: 40px;",\n    "grid-template-columns: 96px 40px;",\n    "width: 96px;",\n)')
validator_path.write_text(v)
