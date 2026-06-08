from generator.ui import clear, header, error, info, success, prompt
from generator.engine import generate
from colorama import Fore, Style
from generator.plugins.registry import registry


def _pick_type(plugin_name: str = "react"):
    plugin = registry.get(plugin_name)
    TYPES = plugin.get_types()
    clear()
    print("\n" * 2)
    print("\n  What do you want to generate?\n")
    for number, item in TYPES.items():
        print(Fore.CYAN + Style.BRIGHT + f"  [{number}] {item['label']}")
        print(Fore.WHITE + f"       {item['description']}")
        print(Fore.WHITE + Style.DIM + f"       e.g. {item['examples']}\n")
    print(Fore.RED + "  [7] Back to main menu\n")

    choice = input(" Choose a number: ").strip()

    if choice == "7":
        return None, None

    if choice not in TYPES:
        print(" Invalid choice. Please try again.")
        return _pick_type()

    selected = TYPES[choice]
    name = prompt(f"Enter {selected['label']} name").strip()

    if not name:
        print(" Name cannot be empty. Please try again.")
        return _pick_type()

    return selected["key"], name


def run() -> None:
    type, name = _pick_type()

    if type is None:
        return

    info(f"\n  Generating {type}: {name}...\n")
    generate(type, name)
    success(f"{name} generated!")
