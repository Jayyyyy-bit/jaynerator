
import os
import json
import sys
from generator.ui import clear, header, success, error, warning, info, dim, label, prompt
from generator.schemas import PathsSchema
from pydantic import ValidationError
from generator.config import CONFIG_FILE


GENERATOR_TYPES = ["component", "page", "form", "hook", "modal", "layout"]

DESCRIPTIONS = {
    "component": "small reusable UI pieces  (e.g. Navbar, Button, Card)",
    "page":      "full screens or views      (e.g. Dashboard, Login)",
    "form":      "form components            (e.g. LoginForm, SignupForm)",
    "layout":    "page wrapper shells        (e.g. MainLayout, AuthLayout)",
    "modal":     "popup dialogs              (e.g. ConfirmModal, AlertModal)",
    "hook":      "reusable React logic       (e.g. useAuth, useFetch)",
}


def scan_folders(base_dir: str, max_depth: int = 3) -> list:
    """i-scan nya yung buong project folder up to max depth for existing components, pages, etc."""
    found = []

    for root, dirs, _ in os.walk(base_dir):

        dirs[:] = [
            d for d in dirs
            if d not in ["node_modules", "__pycache__", ".git", "dist", "build", ".next"] and not d.startswith(".")
        ]

        depth = root.replace(base_dir, "").count(os.sep)

        if depth >= max_depth:
            continue

        for d in dirs:
            folder_path = os.path.join(root, d)
            relative = os.path.relpath(folder_path, base_dir)
            found.append(relative)

    return sorted(found)


def show_folders(folders: list) -> None:
    """ found folders with numbers."""
    print("\n  Found these folders in your project:\n")
    for i, folder in enumerate(folders, 1):
        print(f"  [{i}] {folder}")
    print()


def pick_folder(type: str, folders: list, index: int, total: int) -> str:
    clear()
    header(f"Setup ({index}/{total}) — {type.upper()}")
    info(f"  {DESCRIPTIONS.get(type, type)}\n")

    show_folders(folders)

    dim(" Enter the number of the folder to use, or type a custom path.")
    dim(" Example: src/components or just components\n")

    choice = prompt(f"Where should {type.upper()} files go?")

    if choice.isdigit() and 1 <= int(choice) <= len(folders):
        selected = folders[int(choice) - 1]
        success(f"{type.upper()} → {selected}/Name/Name.tsx\n")
        return selected

    if choice:
        success(f"{type.upper()} → {choice}/Name/Name.tsx\n")
        return choice

    default = f"src/{type}s"
    warning(f"No input — defaulting to: {default}\n")
    return default


def run_setup(base_dir: str) -> dict:
    """Run the initial setup to configure paths."""
    clear()
    print("\n  Setup mode — configure your project paths.")
    print("  " + "─" * 40)
    print("\n  We'll scan your project and help you map each type to a folder.\n")
    print(f"   Current directory: {base_dir}")
    print("\n  Press ENTER to use current directory, or type the full path.")

    custom = prompt("Project path ")
    target = custom if custom else base_dir

    if not os.path.exists(target):
        print(f"  Path does not exist: {target}")
        sys.exit(1)

    clear()
    header("Scanning Project...")
    folders = scan_folders(target)

    if not folders:
        warning("No folders found. Using default paths.")
        return {t: f"src/{t}s" for t in GENERATOR_TYPES}

    config = {}
    total = len(GENERATOR_TYPES)

    for index, type in enumerate(GENERATOR_TYPES, 1):
        config[type] = pick_folder(type, folders, index, total)

    return config


def save_config(config: dict) -> None:
    try:
        PathsSchema(**config)
    except ValidationError as e:
        error("Invalid config — hindi ma-save:")
        for err in e.errors():
            print(f"  - {err['loc'][0]}: {err['msg']}")
        return

    with open(CONFIG_FILE, "w") as f:
        json.dump(config, f, indent=2)

    success("Config saved to generator.config.json")
    dim("Delete that file anytime to re-run setup.\n")


def load_config() -> dict | None:
    """Load configuration from JSON file if it exists."""
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, "r") as f:
            return json.load(f)
    return None
