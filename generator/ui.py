import os
import sys
from colorama import init, Fore, Back, Style

init(autoreset=True)

def clear():
    """Clear the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')


def header(text: str):
    """Print a section header."""
    print(Fore.CYAN + Style.BRIGHT + f"\n  {text}")
    print(Fore.CYAN + "  " + "─" * 40)


def success(text: str):
    print(Fore.GREEN + Style.BRIGHT + f"  {text}")


def error(text: str):
    print(Fore.RED + Style.BRIGHT + f"  {text}")


def warning(text: str):
    print(Fore.YELLOW + f"  {text}")


def info(text: str):
    print(Fore.WHITE + f"  {text}")


def dim(text: str):
    print(Fore.WHITE + Style.DIM + f"  {text}")


def label(text: str):
    print(Fore.MAGENTA + Style.BRIGHT + f"  {text}")


def prompt(text: str) -> str:
    return input(Fore.YELLOW + Style.BRIGHT + f"  → {text}: " + Style.RESET_ALL).strip()