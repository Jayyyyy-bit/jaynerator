from generator.context import GenerationContext


def test_context_creation():
    ctx = GenerationContext(
        gen_type="component",
        name="Navbar",
        plugin_name="react",
    )
    assert ctx.gen_type == "component"
    assert ctx.name == "Navbar"
    assert ctx.plugin_name == "react"
    assert ctx.content == ""
    assert ctx.dry_run == False


def test_context_is_valid():
    ctx = GenerationContext(
        gen_type="component",
        name="Navbar",
        plugin_name="react",
    )
    assert ctx.is_valid() == True


def test_context_invalid_when_empty():
    ctx = GenerationContext(
        gen_type="",
        name="Navbar",
        plugin_name="react",
    )
    assert ctx.is_valid() == False


def test_context_str():
    ctx = GenerationContext(
        gen_type="component",
        name="Navbar",
        plugin_name="react",
    )
    assert str(ctx) == "GenerationContext(react/component/Navbar)"
