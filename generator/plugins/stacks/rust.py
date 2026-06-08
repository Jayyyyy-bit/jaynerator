from generator.plugins.base import StackPlugin

TYPES = {
    "1": {
        "key":         "cli",
        "label":       "CLI Tool",
        "description": "Command-line tool using Clap — para sa fast, reliable na CLI apps sa Rust",
        "examples":    "FileTool, NetworkTool, DeployTool",
    },
    "2": {
        "key":         "axum_route",
        "label":       "Axum Web Route",
        "description": "REST API endpoints using Axum — pinaka-popular na Rust web framework",
        "examples":    "UserRoute, ProductRoute, AuthRoute",
    },
    "3": {
        "key":         "systems",
        "label":       "Systems Tool",
        "description": "Low-level systems tool — file I/O, memory, OS interaction",
        "examples":    "FileProcessor, MemoryTool, NetworkScanner",
    },
}


class RustPlugin(StackPlugin):
    name = "rust"
    label = "Rust"
    stack = "backend"
    templates = "rust"
    types = TYPES
