from generator.ui import clear, prompt, error, info, success, header
from generator.engine import generate
from generator.plugins.registry import registry
from colorama import Fore, Style


def _pick_type():
    plugin = registry.get("python")
    TYPES = plugin.get_types()

    clear()
    print("\n" * 2)
    header("\n  What do you want to generate?\n")
    print()

    for number, item in TYPES.items():
        print(Fore.CYAN + Style.BRIGHT + f"  [{number}] {item['label']}")
        print(Fore.WHITE + f"       {item['description']}")
        print(Fore.WHITE + Style.DIM + f"       e.g. {item['examples']}\n")

    print(Fore.RED + "  [7] Back to main menu\n")

    choice = prompt(" Choose a number: ").strip()

    if choice == "7":
        return None, None

    if choice not in TYPES:
        print(" Invalid choice. Please try again.")
        return _pick_type()

    selected = TYPES[choice]
    name = prompt(
        f"Enter {selected['label']} name "
        f"(e.g. {selected['examples'].split(',')[0].strip()})"
    )

    if not name:
        error(" Name cannot be empty. Please try again.")
        return _pick_type()

    return selected["key"], name


def run() -> None:
    type, name = _pick_type()

    if type is None:
        return

    info(f"\n  Generating {type}: {name}...\n")
    generate(type, name, plugin_name="python")
    success(f"{name} generated!")
