from generator.ui import clear, header, info, success, warning, prompt
from generator.engine import generate
from generator.config import CONFIG
from commands.interactive import _pick_type


def run() -> None:
    clear()
    header("Dry Run Mode — preview lang, walang files na i-gegenerate")

    CONFIG["dry_run"] = True
    type, name = _pick_type()

    if type is None:
        return

    info(f"\n  Previewing {type}: {name}...\n")
    generate(type, name)

    confirm = prompt("Generate? (y/n)").strip().lower()

    if confirm == "y":
        CONFIG["dry_run"] = False
        info(f"\n  Generating {type}: {name}...\n")
        generate(type, name)
        success(f"{name} generated!")
    else:
        warning("Cancelled. No files were generated.")
