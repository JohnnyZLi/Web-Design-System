#!/usr/bin/env python3
from pathlib import Path

p = Path("styles/site-identity.css")
s = p.read_text()
old = """.jl-site-menu {
  width: 144px;
  min-width: 144px;
  box-sizing: border-box;
  grid-column: 1;
  grid-row: 2;
  justify-self: start;
  padding: var(--jl-space-1);
  border-radius: 0 0 var(--jl-radius-md) var(--jl-radius-md);
  list-style: none;
}

.jl-site-menu::before {
  content: "";
  position: absolute;
  top: 0;
  right: -1px;
  left: 87px;
  border-top: 1px solid var(--jl-color-rule-strong);
}
"""
new = """.jl-site-menu {
  --_jl-site-menu-trigger-offset: calc(144px - 88px - var(--jl-space-2) - var(--jl-control-height-md));
  width: 144px;
  min-width: 144px;
  box-sizing: border-box;
  grid-column: 1 / 3;
  grid-row: 2;
  justify-self: end;
  padding: var(--jl-space-1);
  border-radius: 0 0 var(--jl-radius-md) var(--jl-radius-md);
  list-style: none;
}

.jl-site-menu::before,
.jl-site-menu::after {
  content: "";
  position: absolute;
  top: 0;
  border-top: 1px solid var(--jl-color-rule-strong);
}

.jl-site-menu::before {
  left: -1px;
  width: calc(var(--_jl-site-menu-trigger-offset) + 1px);
}

.jl-site-menu::after {
  right: -1px;
  left: calc(var(--_jl-site-menu-trigger-offset) + 88px);
}
"""
if old not in s:
    raise SystemExit("expected Sites menu block not found")
s = s.replace(old, new, 1)
s = s.replace(
    """  .jl-site-menu a {
    min-height: 36px;
    padding: 6px;
  }
""",
    """  .jl-site-menu {
    --_jl-site-menu-trigger-offset: calc(144px - 88px - var(--jl-space-2) - 40px);
  }

  .jl-site-menu a {
    min-height: 36px;
    padding: 6px;
  }
""",
    1,
)
s = s.replace(
    """  .jl-site-switcher__button {
    width: 88px;
    min-width: 88px;
  }

  .jl-site-menu a {
""",
    """  .jl-site-switcher__button {
    width: 88px;
    min-width: 88px;
  }

  .jl-site-menu {
    --_jl-site-menu-trigger-offset: calc(144px - 88px - (var(--jl-space-1) / 2) - 40px);
  }

  .jl-site-menu a {
""",
    1,
)
s = s.replace(
    """  .jl-site-switcher {
    column-gap: 0;
  }
}
""",
    """  .jl-site-switcher {
    column-gap: 0;
  }

  .jl-site-menu {
    --_jl-site-menu-trigger-offset: 16px;
  }
}
""",
    1,
)
p.write_text(s)
