import shutil

REQUIREMENTS = {
    "react": [
        {
            "tool":    "node",
            "label":   "Node.js",
            "install": "https://nodejs.org",
        },
        {
            "tool":    "npm",
            "label":   "npm",
            "install": "Comes with Node.js",
        },
    ],
    "python": [
        {
            "tool":    "python",
            "label":   "Python 3",
            "install": "https://python.org",
        },
        {
            "tool":    "pip",
            "label":   "pip",
            "install": "Comes with Python",
        },
    ],
    "node": [
        {
            "tool":    "node",
            "label":   "Node.js",
            "install": "https://nodejs.org",
        },
    ],
    "rust": [
        {
            "tool":    "rustc",
            "label":   "Rust",
            "install": "https://rustup.rs",
        },
        {
            "tool":    "cargo",
            "label":   "Cargo",
            "install": "Comes with Rust via rustup",
        },
    ],
}


def check_tool(tool: str) -> bool:
    return shutil.which(tool) is not None


def run_doctor(plugin_name: str = None) -> dict:
    results = {}

    targets = (
        {plugin_name: REQUIREMENTS[plugin_name]}
        if plugin_name and plugin_name in REQUIREMENTS
        else REQUIREMENTS
    )

    for stack, tools in targets.items():
        results[stack] = []
        for item in tools:
            installed = check_tool(item["tool"])
            results[stack].append({
                "tool":      item["tool"],
                "label":     item["label"],
                "install":   item["install"],
                "installed": installed,
            })

    return results
