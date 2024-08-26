from typing import Annotated

from fastapi import Path, APIRouter

router = APIRouter(prefix="/items", tags=["Items"])

items = [
    {"id": 1, "item": "item1"},
    {"id": 2, "item": "item2"},
    {"id": 3, "item": "item3"},   
]

@router.get('/')
def list_items():
    return items

@router.get("/latest/")
def get_latest_item():
    return items[-1]

@router.get("/{item_id}")
def get_item(item_id: int = Annotated[int, Path(ge=1, lt=1_000_000)]):
    for item in items:
        if item_id == item.get("id"):
            return item
    return {
        "message": "Нет предмета с таким номером"
    }




