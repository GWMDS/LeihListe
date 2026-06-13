from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from models import Item
from dependencies import get_session

router = APIRouter(
    prefix="/api/items",
    tags=["items"]
)

@router.get("/borrowed")#, response_model=Item)
def get_items_borrowed(session: Session = Depends(get_session))-> list[Item]:
    """Returns borrowed items from database."""
    items = session.exec(select(Item).where(Item.status == False)).all()
    return items
