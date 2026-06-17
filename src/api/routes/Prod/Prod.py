from fastapi import APIRouter, HTTPException
from .Prod_model import Prod

router = APIRouter(prefix="/prod", tags=["Prod"])

@router.get("/")
async def get_all():
    # TODO: return all Prod
    return []

@router.get("/{id}")
async def get_one(id: int):
    # TODO: return single Prod
    return {}

@router.post("/")
async def create(data: Prod):
    # TODO: create Prod
    return data

@router.put("/{id}")
async def update(id: int, data: Prod):
    # TODO: update Prod
    return data

@router.delete("/{id}")
async def delete(id: int):
    # TODO: delete Prod
    return {"deleted": id}
