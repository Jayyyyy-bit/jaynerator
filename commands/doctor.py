from generator.validator import run_doctor
from generator.ui import clear, header, success, error, info, dim
from colorama import Fore, Style


def run() -> None:
    clear()
    header("Doctor — Checking your environment")
    print()

    results = run_doctor()
    all_good = True

    for stack, tools in results.items():
        print(Fore.CYAN + Style.BRIGHT + f"  {stack.upper()}\n")

        for item in tools:
            if item["installed"]:
                print(Fore.GREEN + f"  [OK]     {item['label']}")
            else:
                print(Fore.RED + f"  [MISSING] {item['label']}")
                print(Fore.WHITE + Style.DIM +
                      f"           Install: {item['install']}")
                all_good = False

        print()

    if all_good:
        success("All tools are installed. You're good to go!")
    else:
        error("Some tools are missing. Install them before generating.")
