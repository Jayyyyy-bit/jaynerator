from generator.plugins.registry import registry


def test_registry_loads_plugins():
    plugins = registry.all()
    assert len(plugins) > 0


def test_react_plugin_exists():
    plugin = registry.get("react")
    assert plugin is not None
    assert plugin.name == "react"
    assert plugin.stack == "frontend"


def test_python_plugin_exists():
    plugin = registry.get("python")
    assert plugin is not None
    assert plugin.stack == "backend"


def test_node_plugin_exists():
    plugin = registry.get("node")
    assert plugin is not None
    assert plugin.stack == "backend"


def test_rust_plugin_exists():
    plugin = registry.get("rust")
    assert plugin is not None
    assert plugin.stack == "backend"


def test_plugin_has_types():
    plugin = registry.get("react")
    types = plugin.get_types()
    assert len(types) > 0


def test_plugin_has_template_dir():
    plugin = registry.get("react")
    assert plugin.get_template_dir() == "frontend"
