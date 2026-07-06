import logging
import os

LOG_FILE = "jaynerator.log"

def setup_logger(debug: bool = False) -> logging.Logger:
    logger = logging.getLogger("jaynerator")
    logger.setLevel(logging.DEBUG if debug else logging.INFO)

    # ── Terminal handler ──────────────────────────────────────────
    console = logging.StreamHandler()
    console.setLevel(logging.DEBUG if debug else logging.INFO)
    console.setFormatter(logging.Formatter("%(message)s"))

    # ── File handler ──────────────────────────────────────────────
    file_handler = logging.FileHandler(LOG_FILE)
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(
        logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")
    )

    logger.addHandler(console)
    logger.addHandler(file_handler)

    return logger


# ── Global logger instance ────────────────────────────────────────
logger = setup_logger()