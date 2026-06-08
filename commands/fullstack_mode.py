from generator.ui import clear, header, error, info, success, prompt
from generator.composer import compose
from generator.plugins.registry import registry
from colorama import Fore, Style


FRONTEND_PLUGINS = {
    "1": "react",
}

BACKEND_PLUGINS = {
    "1": "python",
    "2": "node",
    "3": "rust",
}


def pick_frontend() -> str | None:
    clear()
    header("Full Stack — Pick Frontend Stack")
    print()

    for number, plugin_name in FRONTEND_PLUGINS.items():
        plugin = registry.get(plugin_name)
        print(Fore.CYAN + Style.BRIGHT + f"  [{number}] {plugin.label}")

    print(Fore.RED + "\n  [9] Back to main menu\n")

    choice = prompt("Pick a number").strip()

    if choice == "9":
        return None
    if choice not in FRONTEND_PLUGINS:
        error("Invalid choice.")
        return pick_frontend()

    return FRONTEND_PLUGINS[choice]


def pick_backend() -> str | None:
    clear()
    header("Full Stack — Pick Backend Stack")
    print()

    for number, plugin_name in BACKEND_PLUGINS.items():
        plugin = registry.get(plugin_name)
        print(Fore.CYAN + Style.BRIGHT + f"  [{number}] {plugin.label}")

    print(Fore.RED + "\n  [9] Back to main menu\n")

    choice = prompt("Pick a number").strip()

    if choice == "9":
        return None
    if choice not in BACKEND_PLUGINS:
        error("Invalid choice.")
        return pick_backend()

    return BACKEND_PLUGINS[choice]


def pick_type(plugin_name: str) -> str | None:
    plugin = registry.get(plugin_name)
    TYPES = plugin.get_types()

    clear()
    header(f"{plugin.label} — Pick Type")
    print()

    for number, item in TYPES.items():
        print(Fore.CYAN + Style.BRIGHT + f"  [{number}] {item['label']}")
        print(Fore.WHITE + f"       {item['description']}")
        print(Fore.WHITE + Style.DIM + f"       e.g. {item['examples']}\n")

    print(Fore.RED + "  [9] Back\n")

    choice = prompt("Pick a number").strip()

    if choice == "9":
        return None
    if choice not in TYPES:
        error("Invalid choice.")
        return pick_type(plugin_name)

    return TYPES[choice]["key"]


def run() -> None:
    # ── Pick stacks ───────────────────────────────────────────────
    frontend_plugin = pick_frontend()
    if frontend_plugin is None:
        return

    backend_plugin = pick_backend()
    if backend_plugin is None:
        return

    # ── Pick types ────────────────────────────────────────────────
    clear()
    header("Full Stack — Pick Frontend Type")
    frontend_type = pick_type(frontend_plugin)
    if frontend_type is None:
        return

    clear()
    header("Full Stack — Pick Backend Type")
    backend_type = pick_type(backend_plugin)
    if backend_type is None:
        return

    # ── Pick name ─────────────────────────────────────────────────
    clear()
    header("Full Stack — Enter Name")
    info("This name will be used for both frontend and backend files.\n")
    name = prompt("Enter name (e.g. User, Product, Auth)").strip()

    if not name:
        error("Name is required.")
        return

    # ── Compose ───────────────────────────────────────────────────
    print()
    compose(frontend_plugin, backend_plugin, frontend_type, backend_type, name)
    success(f"\n  Full stack '{name}' generated!")
