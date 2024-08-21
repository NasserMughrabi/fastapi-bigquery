from fastapi import APIRouter, HTTPException
from app.api.models.item import Item
from app.api.services.item_service import get_items, create_item

router = APIRouter()

@router.post("/")
def add_item(item: Item):
    return create_item(item)

@router.get("/")
def read_items():
    return get_items()

# Code -> Comment -> Test -> Refactor -> Document
