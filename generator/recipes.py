RECIPES = {
    "1": {
        "name":        "React + FastAPI",
        "description": "Full stack web app — React frontend, FastAPI backend",
        "stack":       "fullstack",
        "generates": [
            {"plugin": "react",  "type": "component", "name": "App"},
            {"plugin": "react",  "type": "page",      "name": "Home"},
            {"plugin": "react",  "type": "layout",    "name": "MainLayout"},
            {"plugin": "python", "type": "fastapi_route", "name": "Main"},
            {"plugin": "python", "type": "fastapi_model", "name": "Main"},
        ],
    },
    "2": {
        "name":        "React + Express",
        "description": "Full stack web app — React frontend, Express backend",
        "stack":       "fullstack",
        "generates": [
            {"plugin": "react", "type": "component", "name": "App"},
            {"plugin": "react", "type": "page",      "name": "Home"},
            {"plugin": "react", "type": "layout",    "name": "MainLayout"},
            {"plugin": "node",  "type": "express_route", "name": "Main"},
        ],
    },
    "3": {
        "name":        "Python CLI Tool",
        "description": "Standalone Python CLI tool using Typer",
        "stack":       "backend",
        "generates": [
            {"plugin": "python", "type": "cli", "name": "Main"},
        ],
    },
    "4": {
        "name":        "Neural Net API",
        "description": "PyTorch model exposed via FastAPI",
        "stack":       "backend",
        "generates": [
            {"plugin": "python", "type": "neural_net",    "name": "Model"},
            {"plugin": "python", "type": "fastapi_route", "name": "Predict"},
            {"plugin": "python", "type": "fastapi_model", "name": "InputData"},
        ],
    },
    "5": {
        "name":        "Recon Tool",
        "description": "Cyber recon tool — Python scanner + Rust systems module",
        "stack":       "backend",
        "generates": [
            {"plugin": "python", "type": "cyber",   "name": "Scanner"},
            {"plugin": "rust",   "type": "systems", "name": "CoreTool"},
        ],
    },
    "6": {
        "name":        "Rust CLI Tool",
        "description": "Fast standalone CLI tool using Clap",
        "stack":       "backend",
        "generates": [
            {"plugin": "rust", "type": "cli", "name": "Main"},
        ],
    },
}
