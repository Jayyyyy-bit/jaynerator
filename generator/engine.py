import os
import datetime
from generator.config import load_paths, CONFIG
from generator.plugins.registry import registry
from generator.hooks import fire
from generator.ast_tools.index_updater import update_index
from generator.ast_tools.python_builder import build_fastapi_route, build_fastapi_model
from generator.ast_tools.ts_builder import build as ts_build
from generator.context import GenerationContext

# ── AST builders ──────────────────────────────────────────────────
AST_BUILDERS = {
    "fastapi_route": build_fastapi_route,
    "fastapi_model": build_fastapi_model,
}


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
    if os.path.exists(file_path) and not CONFIG["overwrite"]:
        print(f"    Skipped — file already exists: {file_path}")
        return

    if CONFIG["dry_run"]:
        print(f"   [DRY RUN] Would create: {file_path}")
        return

    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, "w") as f:
        f.write(content)

    print(f"  Created: {file_path}")
    log_generated(file_path)
    fire("after_write", file_path=file_path)


def _resolve_content(ctx: GenerationContext) -> str:
    content = ts_build(ctx.gen_type, ctx.name)
    if content:
        return content

    if ctx.gen_type in AST_BUILDERS:
        return AST_BUILDERS[ctx.gen_type](ctx.name)

    template = get_template(ctx.gen_type, ctx.stack_dir, ctx.plugin_name)
    return template.replace("{{ComponentName}}", ctx.name)


def _write_files(ctx: GenerationContext) -> None:
    """Write component file + index file + update parent index."""
    write_file(ctx.component_file, ctx.content)
    write_file(ctx.index_file, f'export {{ default }} from "./{ctx.name}";\n')

    parent_index = os.path.join(os.path.dirname(ctx.base_path), "index.ts")
    update_index(parent_index, ctx.name)


def generate(type: str, name: str, plugin_name: str = "react") -> None:
    PATHS = load_paths()
    plugin = registry.get(plugin_name)

    if not PATHS or type not in PATHS:
        print(f"  Unknown type '{type}'.")
        return

    # Build context
    ctx = GenerationContext(
        gen_type=type,
        name=name,
        plugin_name=plugin_name,
        stack_dir=plugin.get_template_dir(),
        dry_run=CONFIG["dry_run"],
        overwrite=CONFIG["overwrite"],
    )

    # Resolve extension
    ctx.extension = (
        "ts" if type in ["hook", "nestjs_controller"] else
        "py" if plugin_name == "python" else
        "js" if plugin_name == "node" else
        "rs" if plugin_name == "rust" else
        "tsx"
    )

    # Resolve paths
    ctx.base_path = os.path.join(PATHS[type], name)
    ctx.component_file = os.path.join(ctx.base_path, f"{name}.{ctx.extension}")
    ctx.index_file = os.path.join(ctx.base_path, "index.ts")

    #  Fire before hook
    fire("before_generate", ctx=ctx)

    # Resolve content
    ctx.content = _resolve_content(ctx)

    #  Write files
    _write_files(ctx)

    # Fire after hook
    fire("after_generate", ctx=ctx)


def log_generated(file_path: str) -> None:
    if not CONFIG["log"]:
        return

    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(CONFIG["log_file"], "a") as log:
        log.write(f"[{timestamp}] {file_path}\n")
