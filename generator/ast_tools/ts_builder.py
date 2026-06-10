import subprocess
import os

BUILDER_DIR = os.path.join(os.path.dirname(__file__), "ts_builder")

TS_BUILDERS = {
    "component": "component.js",
    "hook":      "hook.js",
}


def build(type: str, name: str) -> str | None:
    if type not in TS_BUILDERS:
        return None

    script = os.path.join(BUILDER_DIR, TS_BUILDERS[type])

    try:
        result = subprocess.run(
            ["node", script, name],
            capture_output = True,
            text           = True,
            cwd            = BUILDER_DIR,
        )

        if result.returncode != 0:
            print(f"  [AST ERROR] {result.stderr}")
            return None

        return result.stdout

    except FileNotFoundError:
        print("  [AST ERROR] Node.js not found — falling back to template")
        return None