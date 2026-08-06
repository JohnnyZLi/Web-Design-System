#!/usr/bin/env python3
"""Generate, validate, serve, and package the Johnny Li Web Design System."""
from __future__ import annotations

from html.parser import HTMLParser
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from pathlib import Path
import argparse
import json
import os
import re
import sys
import zipfile

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "tokens" / "tokens.tokens.json"
OUTPUT = ROOT / "tokens" / "tokens.css"
CSS_EXTENSION = "com.johnnyli.css"
GENERIC_FONTS = {
    "serif", "sans-serif", "monospace", "cursive", "fantasy",
    "system-ui", "ui-serif", "ui-sans-serif", "ui-monospace",
}

SAFE_CSS_OVERRIDE = re.compile(
    r"^(?:-?(?:\d+(?:\.\d+)?|\.\d+)(?:px|rem|em|vw|vh|svh|dvh|lvh|%|ch)"
    r"|(?:clamp|min|max|calc)\([0-9A-Za-z%+*/.,()\s-]+\))$"
)
BLOCKED_CSS_OVERRIDE_FRAGMENTS = (";", "{", "}", "/*", "*/", "url(", "@import", "\n", "\r")

RELEASE_PATHS = (
    ".browserslistrc",
    ".gitignore",
    ".github/CODEOWNERS",
    ".github/dependabot.yml",
    ".github/workflows/validate.yml",
    "CHANGELOG.md",
    "LICENSE",
    "Makefile",
    "README.md",
    "SECURITY.md",
    "ci/performance-baselines.json",
    "docs/DESIGN-SYSTEM.md",
    "docs/MIGRATION.md",
    "scripts/design_system.py",
    "scripts/theme-bootstrap.js",
    "styles/theme-control.css",
    "specimen/index.html",
    "specimen/specimen.css",
    "specimen/specimen.js",
    "tokens/tokens.css",
    "tokens/tokens.tokens.json",
)

SENSITIVE_FILE_PATTERNS = (
    re.compile(r"(^|/)\.env(?:\..+)?$", re.IGNORECASE),
    re.compile(r"(^|/)(?:id_rsa|id_ed25519|credentials\.json|service-account\.json)$", re.IGNORECASE),
    re.compile(r"\.(?:pem|p12|pfx|key)$", re.IGNORECASE),
)

SENSITIVE_CONTENT_PATTERNS = {
    "private key": re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
    "GitHub token": re.compile(r"\bgh[pousr]_[A-Za-z0-9_]{30,}\b"),
    "AWS access key": re.compile(r"\bAKIA[0-9A-Z]{16}\b"),
    "generic secret assignment": re.compile(
        r"(?i)\b(?:api[_-]?key|client[_-]?secret|access[_-]?token|password)\s*[:=]\s*['\"][^'\"]{12,}['\"]"
    ),
    "private IPv4 address": re.compile(
        r"\b(?:10(?:\.\d{1,3}){3}|192\.168(?:\.\d{1,3}){2}|172\.(?:1[6-9]|2\d|3[01])(?:\.\d{1,3}){2})\b"
    ),
    "absolute home path": re.compile(r"(?:/Users/[^/\s]+/|/home/[^/\s]+/|[A-Za-z]:\\Users\\[^\\\s]+\\)"),
    "Cloudflare identifier assignment": re.compile(
        r"(?i)\b(?:account|zone|tunnel)[_-]?id\s*[:=]\s*['\"]?[0-9a-f]{32,36}['\"]?"
    ),
}


def walk(node, path=(), inherited_type=None):
    if not isinstance(node, dict):
        return
    token_type = node.get("$type", inherited_type)
    if "$value" in node:
        yield path, node, token_type
        return
    for key, value in node.items():
        if key.startswith("$"):
            continue
        yield from walk(value, path + (key,), token_type)


def kebab(value):
    return re.sub(r"(?<!^)(?=[A-Z])", "-", value).replace("_", "-").lower()


def css_name(path):
    return "--jl-" + "-".join(kebab(part) for part in path)


def color_css(value):
    if value.get("alpha", 1) == 1 and value.get("hex"):
        return value["hex"].lower()
    r, g, b = [round(component * 255) for component in value["components"]]
    return f"rgba({r}, {g}, {b}, {value.get('alpha', 1):g})"


def measurement_css(value):
    return f"{value['value']:g}{value['unit']}"


def font_css(value):
    families = [value] if isinstance(value, str) else value
    result = []
    for family in families:
        if family in GENERIC_FONTS or re.fullmatch(r"-?[A-Za-z][A-Za-z-]*", family):
            result.append(family)
        else:
            result.append('"' + family.replace('"', '\\"') + '"')
    return ", ".join(result)


def shadow_css(value):
    return " ".join([
        measurement_css(value["offsetX"]),
        measurement_css(value["offsetY"]),
        measurement_css(value["blur"]),
        measurement_css(value["spread"]),
        color_css(value["color"]),
    ])


def validate_css_override(value):
    if not isinstance(value, str) or not value:
        raise ValueError("CSS override must be a non-empty string")
    lowered = value.lower()
    if any(fragment in lowered for fragment in BLOCKED_CSS_OVERRIDE_FRAGMENTS):
        raise ValueError(f"unsafe CSS override: {value!r}")
    if not SAFE_CSS_OVERRIDE.fullmatch(value):
        raise ValueError(f"unsupported CSS override syntax: {value!r}")
    return value


def to_css(token, token_type):
    override = token.get("$extensions", {}).get(CSS_EXTENSION, {}).get("value")
    if override is not None:
        return validate_css_override(override)
    value = token["$value"]
    if token_type == "color":
        return color_css(value)
    if token_type in {"dimension", "duration"}:
        return measurement_css(value)
    if token_type == "number":
        return f"{value:g}"
    if token_type == "fontFamily":
        return font_css(value)
    if token_type == "cubicBezier":
        return "cubic-bezier(" + ", ".join(f"{part:g}" for part in value) + ")"
    if token_type == "shadow":
        values = value if isinstance(value, list) else [value]
        return ", ".join(shadow_css(item) for item in values)
    raise ValueError(f"Unsupported token type: {token_type}")


def render_tokens():
    data = json.loads(SOURCE.read_text(encoding="utf-8"))
    version = data["$extensions"]["com.johnnyli.meta"]["version"]
    lines = [
        "/* GENERATED FILE — DO NOT EDIT.",
        "   Source: tokens/tokens.tokens.json",
        f"   Design-system version: {version} */",
        ":root {",
    ]
    for path, token, token_type in walk(data):
        if not token_type:
            raise ValueError(f"Token {'.'.join(path)} has no $type")
        lines.append(f"  {css_name(path)}: {to_css(token, token_type)};")
    lines.extend(["}", ""])
    return "\n".join(lines)


def generate():
    OUTPUT.write_text(render_tokens(), encoding="utf-8")
    print(f"Generated {OUTPUT.relative_to(ROOT)}")


def fail(message):
    raise AssertionError(message)


def validate_token(path, token, token_type):
    name = ".".join(path)
    override = token.get("$extensions", {}).get(CSS_EXTENSION, {}).get("value")
    if override is not None:
        try:
            validate_css_override(override)
        except ValueError as error:
            fail(f"{name}: {error}")
    if not token_type:
        fail(f"{name}: missing $type")
    if "value" in token:
        fail(f"{name}: use $value, not value")
    value = token["$value"]
    if token_type == "color":
        if not isinstance(value, dict) or value.get("colorSpace") != "srgb":
            fail(f"{name}: invalid sRGB color")
        if len(value.get("components", [])) != 3:
            fail(f"{name}: color needs three components")
        if not all(isinstance(item, (int, float)) and 0 <= item <= 1 for item in value["components"]):
            fail(f"{name}: color components must be 0–1")
        if not 0 <= value.get("alpha", 1) <= 1:
            fail(f"{name}: invalid alpha")
    elif token_type in {"dimension", "duration"}:
        if not isinstance(value, dict) or set(value) != {"value", "unit"}:
            fail(f"{name}: invalid {token_type}")
        units = {"px", "rem"} if token_type == "dimension" else {"ms", "s"}
        if value["unit"] not in units:
            fail(f"{name}: invalid unit")
    elif token_type == "number" and not isinstance(value, (int, float)):
        fail(f"{name}: invalid number")
    elif token_type == "fontFamily" and not isinstance(value, (str, list)):
        fail(f"{name}: invalid font family")
    elif token_type == "cubicBezier" and (
        not isinstance(value, list) or len(value) != 4
        or not all(isinstance(item, (int, float)) for item in value)
    ):
        fail(f"{name}: invalid cubic Bézier")
    elif token_type == "shadow":
        values = value if isinstance(value, list) else [value]
        for item in values:
            if not isinstance(item, dict):
                fail(f"{name}: invalid shadow")
            for key in ("color", "offsetX", "offsetY", "blur", "spread"):
                if key not in item:
                    fail(f"{name}: shadow missing {key}")
    elif token_type not in {"color", "dimension", "duration", "number", "fontFamily", "cubicBezier", "shadow"}:
        fail(f"{name}: unsupported type {token_type}")


def rgba(value):
    return (*value["components"], value.get("alpha", 1))


def composite(foreground, background):
    fr, fg, fb, fa = rgba(foreground)
    br, bg, bb, _ = rgba(background)
    return (
        fr * fa + br * (1 - fa),
        fg * fa + bg * (1 - fa),
        fb * fa + bb * (1 - fa),
    )


def luminance(rgb):
    values = [
        value / 12.92 if value <= 0.04045 else ((value + 0.055) / 1.055) ** 2.4
        for value in rgb
    ]
    return 0.2126 * values[0] + 0.7152 * values[1] + 0.0722 * values[2]


def contrast(first, second):
    a, b = luminance(first), luminance(second)
    return (max(a, b) + 0.05) / (min(a, b) + 0.05)


def token_at(data, dotted):
    node = data
    for part in dotted.split("."):
        node = node[part]
    return node["$value"]


class SpecimenParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.stylesheets = []
        self.scripts = []
        self.ids = set()
        self.references = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if attrs.get("id"):
            if attrs["id"] in self.ids:
                fail(f"duplicate specimen id: {attrs['id']}")
            self.ids.add(attrs["id"])
        if tag == "link" and attrs.get("rel") == "stylesheet":
            self.stylesheets.append(attrs.get("href"))
        if tag == "script" and attrs.get("src"):
            self.scripts.append(attrs["src"])
        for key in ("aria-controls", "aria-labelledby", "aria-describedby"):
            if attrs.get(key):
                self.references.extend(attrs[key].split())


def validate_markdown():
    paths = [ROOT / "README.md", ROOT / "CHANGELOG.md", *sorted((ROOT / "docs").glob("*.md"))]
    links = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
    for path in paths:
        text = path.read_text(encoding="utf-8")
        if re.search(r"^#{1,6}(?!#)(?=\S)", text, re.MULTILINE):
            fail(f"{path.relative_to(ROOT)}: malformed heading")
        for target in links.findall(text):
            if target.startswith(("http://", "https://", "mailto:", "#")):
                continue
            file_target = target.split("#", 1)[0]
            if file_target and not (path.parent / file_target).resolve().exists():
                fail(f"{path.relative_to(ROOT)}: missing link {target}")


def validate_raw_colors():
    pattern = re.compile(r"#[0-9a-fA-F]{3,8}\b|\b(?:rgb|rgba|hsl|hsla)\(")
    failures = []
    for path in (ROOT / "specimen").rglob("*"):
        if path.suffix not in {".css", ".html", ".js"}:
            continue
        for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            if pattern.search(line):
                failures.append(f"{path.relative_to(ROOT)}:{line_number}: {line.strip()}")
    if failures:
        fail("raw colors outside token files:\n" + "\n".join(failures))


def iter_repository_files():
    for path in sorted(ROOT.rglob("*")):
        if not path.is_file():
            continue
        relative = path.relative_to(ROOT)
        if relative.parts[0] in {".git", "dist", "__pycache__"}:
            continue
        yield path, relative


def validate_repository_safety():
    failures = []
    for path, relative in iter_repository_files():
        normalized = relative.as_posix()
        if any(pattern.search(normalized) for pattern in SENSITIVE_FILE_PATTERNS):
            failures.append(f"sensitive filename: {normalized}")
            continue
        if path.suffix.lower() not in {".md", ".py", ".json", ".yml", ".yaml", ".html", ".css", ".js", ""}:
            continue
        try:
            content = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            failures.append(f"unexpected binary file: {normalized}")
            continue
        if normalized == "scripts/design_system.py":
            content = re.sub(
                r"SENSITIVE_CONTENT_PATTERNS = \{.*?\n\}\n",
                "SENSITIVE_CONTENT_PATTERNS = {}\n",
                content,
                count=1,
                flags=re.DOTALL,
            )
        for label, pattern in SENSITIVE_CONTENT_PATTERNS.items():
            if pattern.search(content):
                failures.append(f"{label}: {normalized}")
    if failures:
        fail("repository safety check failed:\n" + "\n".join(failures))


def validate_release_allowlist():
    missing = [relative for relative in RELEASE_PATHS if not (ROOT / relative).is_file()]
    if missing:
        fail("release allowlist references missing files: " + ", ".join(missing))
    unsafe = [relative for relative in RELEASE_PATHS if any(pattern.search(relative) for pattern in SENSITIVE_FILE_PATTERNS)]
    if unsafe:
        fail("release allowlist contains sensitive paths: " + ", ".join(unsafe))


def validate():
    data = json.loads(SOURCE.read_text(encoding="utf-8"))
    if data.get("$schema") != "https://www.designtokens.org/schemas/2025.10/format.json":
        fail("unexpected DTCG schema")
    for path, token, token_type in walk(data):
        validate_token(path, token, token_type)

    if OUTPUT.read_text(encoding="utf-8") != render_tokens():
        fail("tokens.css drifted; run make generate")

    pairs = [
        ("color.ink", "color.canvas", 4.5),
        ("color.text", "color.canvas", 4.5),
        ("color.muted", "color.canvas", 4.5),
        ("color.accent", "color.canvas", 4.5),
        ("color.onAccent", "color.accent", 4.5),
        ("color.textInverse", "color.surfaceInverse", 4.5),
    ]
    for foreground, background, minimum in pairs:
        fg, bg = token_at(data, foreground), token_at(data, background)
        result = contrast(composite(fg, bg), composite(bg, bg))
        if result < minimum:
            fail(f"{foreground} on {background}: {result:.2f}:1")

    for role in ("success", "warning", "danger", "info", "violet"):
        surface = token_at(data, f"semantic.{role}.surface")
        text = token_at(data, f"semantic.{role}.text")
        border = token_at(data, f"semantic.{role}.border")
        if contrast(composite(text, surface), composite(surface, surface)) < 4.5:
            fail(f"{role} semantic text contrast")
        if contrast(composite(border, surface), composite(surface, surface)) < 3:
            fail(f"{role} semantic border contrast")

    validate_markdown()
    validate_raw_colors()
    validate_repository_safety()
    validate_release_allowlist()

    for unsafe_override in ("1rem; color:red", "url(https://example.com)", "clamp(1rem, 2vw, 3rem)\n@import x"):
        try:
            validate_css_override(unsafe_override)
        except ValueError:
            pass
        else:
            fail(f"CSS override guard accepted unsafe input: {unsafe_override!r}")

    public_text = "\n".join(
        path.read_text(encoding="utf-8")
        for path in [ROOT / "README.md", ROOT / "CHANGELOG.md", *sorted((ROOT / "docs").glob("*.md"))]
    )
    if re.search(r"\b[0-9a-f]{40}\b", public_text):
        fail("public docs expose a commit snapshot")
    if re.search(r"\bsrc/client/", public_text):
        fail("public docs expose a private source path")

    defined = set(re.findall(r"(--jl-[a-z0-9-]+)\s*:", OUTPUT.read_text(encoding="utf-8")))
    css = (ROOT / "specimen" / "specimen.css").read_text(encoding="utf-8")
    used = set(re.findall(r"var\((--jl-[a-z0-9-]+)", css))
    missing = sorted(used - defined)
    if missing:
        fail("undefined CSS variables: " + ", ".join(missing))
    if css.count("{") != css.count("}"):
        fail("unbalanced specimen CSS braces")

    specimen = ROOT / "specimen" / "index.html"
    parser = SpecimenParser()
    parser.feed(specimen.read_text(encoding="utf-8"))
    for relative in parser.stylesheets + parser.scripts:
        if not (specimen.parent / relative).resolve().exists():
            fail(f"missing specimen asset: {relative}")
    for reference in parser.references:
        if reference not in parser.ids:
            fail(f"missing specimen id: {reference}")

    if (ROOT / "FULL-SPECIFICATION.md").exists():
        fail("combined specification must be generated into dist/")

    print(f"Validation passed. Validated {sum(1 for _ in walk(data))} DTCG tokens.")


def serve():
    os.chdir(ROOT)
    print("Serving http://127.0.0.1:8000/specimen/")
    ThreadingHTTPServer(("127.0.0.1", 8000), SimpleHTTPRequestHandler).serve_forever()


def release():
    validate_release_allowlist()
    validate_repository_safety()
    data = json.loads(SOURCE.read_text(encoding="utf-8"))
    version = data["$extensions"]["com.johnnyli.meta"]["version"]
    dist = ROOT / "dist"
    dist.mkdir(exist_ok=True)

    markdown = dist / f"Johnny_Li_Web_Design_System_v{version}.md"
    sources = [
        ROOT / "README.md",
        ROOT / "docs" / "DESIGN-SYSTEM.md",
        ROOT / "docs" / "MIGRATION.md",
        ROOT / "CHANGELOG.md",
    ]
    parts = [
        f"# Johnny Li Web Design System v{version} — Consolidated Release\n\n",
        "> Generated from authoritative repository files. Do not edit directly.\n",
    ]
    for source in sources:
        parts.append(f"\n---\n\n<!-- Source: {source.relative_to(ROOT)} -->\n\n")
        parts.append(source.read_text(encoding="utf-8"))
    markdown.write_text("".join(parts), encoding="utf-8")

    archive = dist / f"Johnny_Li_Web_Design_System_v{version}.zip"
    with zipfile.ZipFile(archive, "w", zipfile.ZIP_DEFLATED) as output:
        for relative_text in RELEASE_PATHS:
            relative = Path(relative_text)
            output.write(ROOT / relative, Path(f"Web-Design-System-v{version}") / relative)
    print(f"Built {markdown.relative_to(ROOT)}")
    print(f"Built {archive.relative_to(ROOT)}")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("command", choices=["generate", "validate", "serve", "release"])
    args = parser.parse_args()
    {"generate": generate, "validate": validate, "serve": serve, "release": release}[args.command]()


if __name__ == "__main__":
    try:
        main()
    except (AssertionError, ValueError) as error:
        print(f"Error: {error}", file=sys.stderr)
        sys.exit(1)
