from generator.ui import clear, header, error, info, success, dim, prompt
from generator.engine import generate
from generator.recipes import RECIPES
from colorama import Fore, Style


def show_menu() -> None:
    clear()
    header("Recipes — One-command project presets")
    print()

    for number, recipe in RECIPES.items():
        print(Fore.CYAN + Style.BRIGHT + f"  [{number}] {recipe['name']}")
        print(Fore.WHITE + f"       {recipe['description']}")

        print(Fore.WHITE + Style.DIM + "       Generates: " + ", ".join(
            f"{g['plugin']}/{g['type']}"
            for g in recipe["generates"]
        ) + "\n")

    print(Fore.RED + "  [9] Back to main menu\n")


def run() -> None:
    show_menu()

    choice = prompt("Pumili ng number").strip()

    if choice == "9":
        return

    if choice not in RECIPES:
        error("Invalid choice.")
        run()
        return

    recipe = RECIPES[choice]

    # ── Confirm ───────────────────────────────────────────────────
    clear()
    header(f"Recipe: {recipe['name']}")
    info(f"  {recipe['description']}\n")
    print(Fore.WHITE + "  This will generate:\n")

    for item in recipe["generates"]:
        print(Fore.CYAN +
              f"  → {item['plugin']}/{item['type']}/{item['name']}")

    print()
    confirm = prompt("Proceed? (y/n)").strip().lower()

    if confirm != "y":
        info("Cancelled.")
        return

    # ── Generate all ──────────────────────────────────────────────
    print()
    for item in recipe["generates"]:
        info(f"  Generating {item['type']}: {item['name']}...")
        generate(item["type"], item["name"], plugin_name=item["plugin"])

    success(f"\n  Recipe '{recipe['name']}' complete!")
