import os
import datetime
from generator.config import load_paths, CONFIG
from generator.plugins.registry import registry
from generator.hooks import fire
from generator.ast_tools.index_updater import update_index
from generator.ast_tools.python_builder import build_fastapi_route, build_fastapi_model
from generator.ast_tools.ts_builder import build as ts_build

def get_template(template_name: str, stack: str = "frontend", plugin_name: str = "react") -> str:
    template_dir = os.path.join(os.path.dirname(__file__), "templates", stack)

    extension = "ts" if template_name in ["hook", "nestjs_controller"] else \
        "py" if plugin_name == "python" else \
        "js" if plugin_name == "node" else \
        "rs" if plugin_name == "rust" else \
        "tsx"

    template_path = os.path.join(
        template_dir, f"{template_name}.{extension}.template")

    if not os.path.exists(template_path):
        raise FileNotFoundError(f"Template '{template_name}' not found.")

    with open(template_path, "r") as f:
        return f.read()


def write_file(file_path: str, content: str) -> None:
    """Write content to a file safely."""
    # Safety: never overwrite
    if os.path.exists(file_path) and not CONFIG["overwrite"]:
        print(f"    Skipped — file already exists: {file_path}")
        return

    # Dry run: preview only
    if CONFIG["dry_run"]:
        print(f"   [DRY RUN] Would create: {file_path}")
        return

    #  Create folders if they don't exist
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, "w") as f:
        f.write(content)

    print(f"  Created: {file_path}")
    log_generated(file_path)

    fire("after_write", file_path=file_path)


# ── AST builders — used instead of templates ──────────────────────
# ── AST builders dict — this stays OUTSIDE, module level ─────────
AST_BUILDERS = {
    "fastapi_route": build_fastapi_route,
    "fastapi_model": build_fastapi_model,
}


def generate(type: str, name: str, plugin_name: str = "react") -> None:
    PATHS = load_paths()

    if not PATHS or type not in PATHS:
        print(f"  Unknown type '{type}'.")
        return

    plugin    = registry.get(plugin_name)
    stack_dir = plugin.get_template_dir()

    fire("before_generate", type=type, name=name)

    extension = "ts" if type in ["hook", "nestjs_controller"] else \
                "py" if plugin_name == "python"               else \
                "js" if plugin_name == "node"                 else \
                "rs" if plugin_name == "rust"                 else \
                "tsx"

    # ── these 3 lines must be INSIDE generate() ──────────────────
    content = ts_build(type, name)

    if content is None and type in AST_BUILDERS:
        content = AST_BUILDERS[type](name)

    if content is None:
        template = get_template(type, stack_dir, plugin_name)
        content  = template.replace("{{ComponentName}}", name)

    base_path      = os.path.join(PATHS[type], name)
    component_file = os.path.join(base_path, f"{name}.{extension}")
    index_file     = os.path.join(base_path, "index.ts")

    write_file(component_file, content)
    write_file(index_file, f'export {{ default }} from "./{name}";\n')

    parent_index = os.path.join(PATHS[type], "index.ts")
    update_index(parent_index, name)

    fire("after_generate", type=type, name=name, path=base_path)

def log_generated(file_path: str) -> None:
    """Append generated file to the log."""
    if not CONFIG["log"]:
        return

    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(CONFIG["log_file"], "a") as log:
        log.write(f"[{timestamp}] {file_path}\n")
