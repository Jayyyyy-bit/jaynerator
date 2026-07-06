import sys
from colorama import Fore, Style
from generator.ui import clear, prompt, error
from generator.hooks import register
from generator.plugins import registry
from commands import interactive, cli, dry_run, setup, \
    python_mode, node_mode, rust_mode, \
    doctor, fullstack_mode, recipe_mode
from generator.logger import setup_logger, logger


def on_after_generate(ctx, **kwargs):
    print(f"\n  [HOOK] after_generate → {ctx}")


register("after_generate", on_after_generate)


COMMANDS = {
    "1": interactive.run,
    "2": cli.run,
    "3": dry_run.run,
    "4": setup.run,
    "5": python_mode.run,
    "6": node_mode.run,
    "7": rust_mode.run,
    "8": doctor.run,
    "9": fullstack_mode.run,
    "0": recipe_mode.run
}


def show_welcome():
    clear()
    print(Fore.CYAN + Style.BRIGHT + """
     ██╗ █████╗ ██╗   ██╗███╗   ██╗███████╗██████╗  █████╗ ████████╗ ██████╗ ██████╗ 
     ██║██╔══██╗╚██╗ ██╔╝████╗  ██║██╔════╝██╔══██╗██╔══██╗╚══██╔══╝██╔═══██╗██╔══██╗
     ██║███████║ ╚████╔╝ ██╔██╗ ██║█████╗  ██████╔╝███████║   ██║   ██║   ██║██████╔╝
██   ██║██╔══██║  ╚██╔╝  ██║╚██╗██║██╔══╝  ██╔══██╗██╔══██║   ██║   ██║   ██║██╔══██╗
╚█████╔╝██║  ██║   ██║   ██║ ╚████║███████╗██║  ██║██║  ██║   ██║   ╚██████╔╝██║  ██║
 ╚════╝ ╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝
    """)
    print(Fore.YELLOW + Style.BRIGHT +
          "  A boilerplate generator para hindi ka na palaging from scratch. " + Style.RESET_ALL)
    print("\n  by Jay  ")
    print("  " + "─" * 70 + "\n")
    print(Fore.WHITE + "\n  Choose how you want to run the generator:\n")
    print(Fore.WHITE +
          "  [1] Interactive mode  — follow the prompts step by step")
    print(Fore.WHITE + "  [2] Command-line mode — type the command directly")
    print(Fore.WHITE +
          "  [3] Dry run mode      — preview files without creating them")
    print(Fore.WHITE +
          "  [4] Setup mode        — configure the generator for your project")
    print(Fore.WHITE +
          "  [5] Python mode       — FastAPI, Scraper, Neural Net, CLI, Cyber")
    print(Fore.WHITE +
          "  [6] Node.js mode      — Express, Fastify")
    print(Fore.WHITE +
          "  [7] Rust mode         — CLI, Axum Web API, Systems")
    print(Fore.WHITE +
          "  [8] Doctor            — Check your environment")
    print(Fore.WHITE +
          "  [9] Full Stack Mode   — Generate both frontend and backend")
    print(Fore.WHITE +
          "  [0] Recipes           — Run a predefined recipe")
    print(Fore.WHITE +
          "  [X] Exit\n")


def main():
    running = True
    while running:
        show_welcome()
        choice = prompt("Pick a number").strip()

        if choice.lower() == "x":
            clear()
            print(Fore.CYAN + Style.BRIGHT + "\n  Bye — JAYNERATOR\n")
            sys.exit(0)

        if choice not in COMMANDS:
            error("Invalid. Enter 1-8.")
            continue

        COMMANDS[choice]()

        # ── After action ──────────────────────────────────────────
        print(Fore.CYAN + "\n  " + "─" * 40)
        print(Fore.WHITE + "\n  Any more?\n")
        print(Fore.WHITE + "  [1] Back to main menu\n")
        print(Fore.RED + "  [2] Exit \n")

        action = prompt("Choose a number").strip()
        if action == "2":
            clear()
            print(Fore.CYAN + Style.BRIGHT + "\n  Bye — JAYNERATOR\n")
            sys.exit(0)


if __name__ == "__main__":
    main()

if "--debug" in sys.argv:
    sys.argv.remove("--debug")
    setup_logger(debug=True)
    logger.debug("Debug mode enabled")
