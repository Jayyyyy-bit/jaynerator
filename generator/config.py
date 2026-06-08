import os
import json
from generator.schemas import PathsSchema
from pydantic import ValidationError
import sys


CONFIG_FILE = "generator.config.json"
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))


def load_paths() -> dict:
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, "r") as f:
            saved = json.load(f)

        try:
            validated = PathsSchema(**saved)
        except ValidationError as e:
            print("\n  [ERROR] generator.config.json is invalid:")
            for err in e.errors():
                print(f"  - {err['loc'][0]}: {err['msg']}")
            print("\n  Run setup mode to fix it.\n")
            sys.exit(1)

        return {
            type: os.path.join(BASE_DIR, path)
            for type, path in validated.model_dump().items()
        }

    return {
        # ── Frontend ──────────────────────────────────────────────────
        "component":    os.path.join(BASE_DIR, "src", "components"),
        "page":         os.path.join(BASE_DIR, "src", "apps"),
        "form":         os.path.join(BASE_DIR, "src", "forms"),
        "layout":       os.path.join(BASE_DIR, "src", "layouts"),
        "modal":        os.path.join(BASE_DIR, "src", "modals"),
        "hook":         os.path.join(BASE_DIR, "src", "hooks"),
        # ── Python backend ────────────────────────────────────────────
        "fastapi_route": os.path.join(BASE_DIR, "src", "api", "routes"),
        "fastapi_model": os.path.join(BASE_DIR, "src", "api", "models"),
        "scraper":       os.path.join(BASE_DIR, "src", "scrapers"),
        "neural_net":    os.path.join(BASE_DIR, "src", "models"),
        "cli":           os.path.join(BASE_DIR, "src", "cli"),
        "cyber":         os.path.join(BASE_DIR, "src", "tools"),
        # ── Node.js backend ───────────────────────────────────────────
        "express_route":     os.path.join(BASE_DIR, "src", "routes"),
        "fastify_route":     os.path.join(BASE_DIR, "src", "routes"),
        "nestjs_controller": os.path.join(BASE_DIR, "src", "controllers"),
        # ── Rust backend ────────────────────────────────────────────
        "axum_route": os.path.join(BASE_DIR, "src", "routes"),
        "systems":    os.path.join(BASE_DIR, "src", "systems"),

    }


PATHS = load_paths()

CONFIG = {
    "overwrite": False,
    "dry_run":   False,
    "log":       True,
    "log_file": "generated.log",

}
