import os
import re


def parse_exports(content: str) -> list[str]:
    """Extract all existing export names from index.ts content."""
    pattern = r"export\s*\{\s*default\s+as\s+(\w+)\s*\}"
    return re.findall(pattern, content)


def build_export(name: str) -> str:
    """Build a single export line."""
    return f'export {{ default as {name} }} from "./{name}";\n'


def update_index(index_path: str, name: str) -> None:
    """
    Safely add a new export to an index.ts barrel file.
    Creates the file if it doesn't exist.
    Skips if export already exists.
    """
    # ── Read existing content ─────────────────────────────────────
    if os.path.exists(index_path):
        with open(index_path, "r") as f:
            content = f.read()
    else:
        content = ""

    # ── Check for duplicate ───────────────────────────────────────
    existing = parse_exports(content)
    if name in existing:
        print(f"  [INDEX] Skipped — {name} already exported")
        return

    # ── Append new export ─────────────────────────────────────────
    new_export = build_export(name)

    with open(index_path, "a") as f:
        f.write(new_export)

    print(f"  [INDEX] Added export → {name}")