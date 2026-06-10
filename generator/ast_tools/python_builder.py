import libcst as cst


def build_fastapi_route(name: str) -> str:
    """Build a FastAPI route file using AST."""

    # ── Imports ───────────────────────────────────────────────────
    imports = [
        cst.parse_statement("from fastapi import APIRouter, HTTPException\n"),
        cst.parse_statement(f"from .{name}_model import {name}\n"),
    ]

    # ── Router instance ───────────────────────────────────────────
    router_var = cst.parse_statement(
        f'router = APIRouter(prefix="/{name.lower()}", tags=["{name}"])\n'
    )

    # ── Route functions ───────────────────────────────────────────
    get_all = cst.parse_statement(f"""
@router.get("/")
async def get_all():
    # TODO: return all {name}
    return []
""")

    get_one = cst.parse_statement(f"""
@router.get("/{{id}}")
async def get_one(id: int):
    # TODO: return single {name}
    return {{}}
""")

    create = cst.parse_statement(f"""
@router.post("/")
async def create(data: {name}):
    # TODO: create {name}
    return data
""")

    update = cst.parse_statement(f"""
@router.put("/{{id}}")
async def update(id: int, data: {name}):
    # TODO: update {name}
    return data
""")

    delete = cst.parse_statement(f"""
@router.delete("/{{id}}")
async def delete(id: int):
    # TODO: delete {name}
    return {{"deleted": id}}
""")

    # ── Assemble module ───────────────────────────────────────────
    module = cst.Module(
        body=[
            *imports,
            cst.EmptyLine(),
            router_var,
            get_all,
            get_one,
            create,
            update,
            delete,
        ]
    )

    return module.code


def build_fastapi_model(name: str) -> str:
    """Build a Pydantic model file using AST."""

    imports = [
        cst.parse_statement("from pydantic import BaseModel\n"),
        cst.parse_statement("from typing import Optional\n"),
    ]

    model_class = cst.parse_statement(f"""
class {name}(BaseModel):
    id:   Optional[int] = None
    name: str
    # TODO: add your fields here
""")

    update_class = cst.parse_statement(f"""
class {name}Update(BaseModel):
    name: Optional[str] = None
    # TODO: add your update fields here
""")

    module = cst.Module(
        body=[
            *imports,
            model_class,
            update_class,
        ]
    )

    return module.code