import os
import pytest
import tempfile
from unittest.mock import patch
from generator.engine import generate
from generator.config import CONFIG


@pytest.fixture
def temp_output(tmp_path):
    """Provide a temp directory for generated output."""
    return tmp_path


def test_generate_component(temp_output):
    """Test that component generates correct files."""
    paths = {
        "component": str(temp_output / "components"),
        "page":      str(temp_output / "apps"),
        "form":      str(temp_output / "forms"),
        "layout":    str(temp_output / "layouts"),
        "modal":     str(temp_output / "modals"),
        "hook":      str(temp_output / "hooks"),
    }

    with patch("generator.engine.load_paths", return_value=paths):
        generate("component", "Navbar")

    component_file = temp_output / "components" / "Navbar" / "Navbar.tsx"
    index_file = temp_output / "components" / "Navbar" / "index.ts"

    assert component_file.exists()
    assert index_file.exists()


def test_generate_hook_creates_ts_file(temp_output):
    """Hook should generate .ts not .tsx."""
    paths = {
        "hook": str(temp_output / "hooks"),
        "component": str(temp_output / "components"),
        "page":      str(temp_output / "apps"),
        "form":      str(temp_output / "forms"),
        "layout":    str(temp_output / "layouts"),
        "modal":     str(temp_output / "modals"),
    }

    with patch("generator.engine.load_paths", return_value=paths):
        generate("hook", "useAuth")

    hook_file = temp_output / "hooks" / "useAuth" / "useAuth.ts"
    assert hook_file.exists()


def test_generate_no_overwrite(temp_output):
    """Existing files should not be overwritten."""
    paths = {
        "component": str(temp_output / "components"),
        "page":      str(temp_output / "apps"),
        "form":      str(temp_output / "forms"),
        "layout":    str(temp_output / "layouts"),
        "modal":     str(temp_output / "modals"),
        "hook":      str(temp_output / "hooks"),
    }

    with patch("generator.engine.load_paths", return_value=paths):
        generate("component", "Navbar")

    component_file = temp_output / "components" / "Navbar" / "Navbar.tsx"
    original_content = component_file.read_text()

    with patch("generator.engine.load_paths", return_value=paths):
        generate("component", "Navbar")

    assert component_file.read_text() == original_content


def test_generate_dry_run(temp_output):
    """Dry run should not create any files."""
    paths = {
        "component": str(temp_output / "components"),
        "page":      str(temp_output / "apps"),
        "form":      str(temp_output / "forms"),
        "layout":    str(temp_output / "layouts"),
        "modal":     str(temp_output / "modals"),
        "hook":      str(temp_output / "hooks"),
    }

    CONFIG["dry_run"] = True

    with patch("generator.engine.load_paths", return_value=paths):
        generate("component", "Navbar")

    CONFIG["dry_run"] = False

    component_file = temp_output / "components" / "Navbar" / "Navbar.tsx"
    assert not component_file.exists()
