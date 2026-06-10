from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from models import Item
from dependencies import get_session

router = APIRouter(
    prefix="/api/items",
    tags=["items"]
)

@router.get("/")#, response_model=Item)
def get_items(session: Session = Depends(get_session))-> list[Item]:
    """Returns all items in the database."""
    items = session.exec(select(Item)).all()
    return items
