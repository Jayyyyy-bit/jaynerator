from generator.engine import generate
from generator.plugins.registry import registry


def compose(
    frontend_plugin: str,
    backend_plugin:  str,
    frontend_type:   str,
    backend_type:    str,
    name:            str,
) -> None:
    """Generate frontend + backend files together."""

    print(f"\n  Generating frontend: {frontend_type} ({frontend_plugin})...")
    generate(frontend_type, name, plugin_name=frontend_plugin)

    print(f"\n  Generating backend: {backend_type} ({backend_plugin})...")
    generate(backend_type, name, plugin_name=backend_plugin)
