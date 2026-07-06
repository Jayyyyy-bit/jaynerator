# JAYNERATOR

> Para hindi ka na palaging mag-umpisa from scratch.

A stack-aware, plugin-driven CLI scaffolding tool that generates boilerplate for any project — React, FastAPI, Express, NestJS, and Rust. AST-powered, extensible, and built for real developers.

---

## Why JAYNERATOR?

Most generators are either too generic or too opinionated. JAYNERATOR is different:

- **Stack-agnostic** — React, Python, Node.js, Rust — all first-class citizens
- **Plugin-extensible** — add a new stack by dropping one file
- **AST-powered** — uses ts-morph and libcst for syntax-safe generation
- **Convention-aware** — generates files that match YOUR project structure
- **Developer-friendly** — interactive CLI, dry run mode, environment doctor

---

## Install

```bash
git clone https://github.com/Jayyyyy-bit/jaynerator.git
cd jaynerator

python -m venv venv
venv\Scripts\Activate        # Windows
source venv/bin/activate     # Mac/Linux

pip install -r requirements.txt
pip install -e .

# Install Node.js dependencies for TypeScript AST
cd generator/ast_tools/ts_builder && npm install && cd ../../..
```

---

## Usage

```bash
jaynerator
```

Pick a mode from the menu:

```
[1] Interactive mode   — step-by-step prompts
[2] Command-line mode  — type the command directly
[3] Dry run mode       — preview files without creating them
[4] Setup mode         — configure folder paths for your project
[5] Python mode        — FastAPI, Scraper, Neural Net, CLI, Cyber
[6] Node.js mode       — Express, Fastify, NestJS
[7] Rust mode          — CLI, Axum Web API, Systems
[8] Doctor             — check your environment
[9] Full Stack mode    — generate frontend + backend together
[0] Recipes            — one-command project presets
[X] Exit
```

---

## Supported Stacks

### Frontend
| Type | Output |
|---|---|
| Component | `src/components/Name/Name.tsx` |
| Page | `src/apps/Name/Name.tsx` |
| Form | `src/forms/Name/Name.tsx` |
| Layout | `src/layouts/Name/Name.tsx` |
| Modal | `src/modals/Name/Name.tsx` |
| Hook | `src/hooks/Name/Name.ts` |

### Python Backend
| Type | Output |
|---|---|
| FastAPI Route | REST API endpoints |
| FastAPI Model | Pydantic request/response model |
| Web Scraper | BeautifulSoup scraper class |
| Neural Network | PyTorch model |
| CLI Tool | Typer CLI app |
| Cyber/Recon Tool | Network scanner |

### Node.js Backend
| Type | Output |
|---|---|
| Express Route | REST API with Express |
| Fastify Route | REST API with Fastify |
| NestJS Controller | Controller with decorators |

### Rust
| Type | Output |
|---|---|
| CLI Tool | Clap-based CLI |
| Axum Route | REST API with Axum |
| Systems Tool | Low-level systems module |

---

## Recipes

One command generates an entire project skeleton:

```
[1] React + FastAPI       — full stack web app
[2] React + Express       — full stack web app
[3] Python CLI Tool       — standalone CLI
[4] Neural Net API        — PyTorch + FastAPI
[5] Recon Tool            — Python + Rust
[6] Rust CLI Tool         — Clap-based CLI
```

---

## Setup Mode

First time in a new project? Run setup:

```bash
jaynerator → [4] Setup mode
```

JAYNERATOR scans your project folders and asks where each type should go. Saves to `generator.config.json` — delete it anytime to reconfigure.

---

## Plugin System

Adding a new stack = dropping one file:

```python
# generator/plugins/stacks/go.py
from generator.plugins.base import StackPlugin

class GoPlugin(StackPlugin):
    name      = "go"
    label     = "Go Backend"
    stack     = "backend"
    templates = "go"
    types     = { ... }
```

Zero changes needed anywhere else. Registry auto-discovers it.

---

## Architecture

```
jaynerator/
├── generate.py               ← CLI entry point
├── commands/                 ← one file per mode
├── generator/
│   ├── engine.py             ← core generation pipeline
│   ├── context.py            ← GenerationContext dataclass
│   ├── plugins/              ← plugin system
│   │   └── stacks/           ← one file per stack
│   ├── ast_tools/            ← AST generation
│   │   ├── python_builder.py ← libcst (Python AST)
│   │   ├── ts_builder.py     ← ts-morph bridge
│   │   └── index_updater.py  ← barrel file auto-export
│   └── templates/            ← fallback templates
└── tests/                    ← pytest test suite
```

### Generation Pipeline

```
CLI Input
   ↓
Command Router (generate.py)
   ↓
GenerationContext (context.py)
   ↓
Content Resolution:
  1. TypeScript AST (ts-morph)
  2. Python AST    (libcst)
  3. Template      (fallback)
   ↓
File Writer + Index Updater
   ↓
Lifecycle Hooks
```

---

## Safety Features

- **No overwrite** — never destroys existing files
- **Dry run** — preview before creating anything
- **Config validation** — Pydantic schema validation
- **Generation log** — tracks everything in `generated.log`
- **Doctor command** — checks Node.js, Python, Rust are installed

---

## Development

```bash
# Run tests
pytest tests/ -v

# Debug mode
jaynerator --debug

# Add a new stack
# 1. Create generator/plugins/stacks/yourstack.py
# 2. Create generator/templates/yourstack/
# 3. Add templates — done
```

---

## Requirements

- Python 3.11+
- Node.js (for TypeScript AST generation)
- Rust (optional — only for Rust templates)

```bash
pip install -r requirements.txt
```

---

## Roadmap

- [ ] Project Analyzer — reads existing project, adapts generation
- [ ] `.jaynerator` project memory file
- [ ] Dependency resolution graph
- [ ] Deployment presets (Docker, GitHub Actions, Vercel)
- [ ] AI-assisted stack recommendations (via Ollama, free)
- [ ] Blueprint Marketplace — community-shared recipes

---

## Built By

Jay — *para hindi na palaging from scratch.*

---

*JAYNERATOR is a living tool — built to grow with your stack.*
