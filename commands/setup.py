import os
from generator.ui import info
from generator.scanner import run_setup, save_config


def run() -> None:
    base_dir = os.path.abspath(".")
    config = run_setup(base_dir)
    save_config(config)
    info("Configured successfully! You can now use the generator.")
