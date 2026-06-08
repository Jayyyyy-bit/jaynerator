from generator.ui import clear, header, error, info, success, prompt
from generator.engine import generate


def run() -> None:
    clear()
    header("Command-line Mode")
    info("Format  : <type> <name>")
    info("Example : component Navbar\n")

    raw = prompt("Enter command").strip().split()

    if len(raw) != 2:
        error("Wrong format. Example: component Navbar")
        run()
        return

    type, name = raw[0].lower(), raw[1]
    info(f"\n  Generating {type}: {name}...\n")
    generate(type, name)
    success(f"{name} generated!")
