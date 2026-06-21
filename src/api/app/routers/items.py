from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from models import Item, ItemBase
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


@router.get("/{item_id}")#, response_model=Item)
def get_item(item_id: int, session: Session = Depends(get_session)) -> Item:
    """Returns one item by id."""
    item = session.get(Item, item_id)

    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item


@router.post("/")#, response_model=Item)
def create_item(item: ItemBase, session: Session = Depends(get_session)) -> Item:
    """Creates a new item in the database."""
    db_item = Item.model_validate(item)
    session.add(db_item)
    session.commit()
    session.refresh(db_item)
    return db_item


@router.put("/{item_id}/{item_name}/{item_description}/{item_state}/{item_isborrowed}/{item_category}")#, response_model=Item)
def update_item(item_id: int, item_name: str, item_description: str, item_state: str, item_isborrowed: bool, item_category: str, session: Session = Depends(get_session)) -> Item:
    """Updates an item in the database."""
    db_item = session.get(Item, item_id)

    if not db_item:
        raise HTTPException(status_code=404, detail="Item not found")

    db_item.name = item_name
    db_item.description = item_description
    db_item.state = item_state
    db_item.isBorrowed = item_isborrowed
    db_item.category = item_category
    session.commit()
    session.refresh(db_item)
    return db_item


@router.post("/update")#, response_model=Item)
def update_item_with_post(item: Item, session: Session = Depends(get_session)) -> Item:
    """Updates an item in the database."""
    db_item = session.get(Item, item.id)

    if not db_item:
        raise HTTPException(status_code=404, detail="Item not found")

    db_item.name = item.name
    if (item.description is not None):
        db_item.description = item.description
    db_item.state = item.state
    db_item.isBorrowed = item.isBorrowed
    db_item.category = item.category
    session.commit()
    session.refresh(db_item)
    return db_item


@router.delete("/{item_id}")#, response_model=Item)
def delete_item(item_id: int, session: Session = Depends(get_session)) -> dict:
    """Deletes an item from the database."""
    item = session.get(Item, item_id)

    if not item:
        raise HTTPException(status_code=404, detail="Item not found")

    session.delete(item)
    session.commit()
    return {"message": "Item deleted successfully"}


@router.put("/{item_id}/borrow")#, response_model=Item)
def borrow_item(item_id: int, session: Session = Depends(get_session)) -> Item:
    """Marks an item as borrowed."""
    item = session.get(Item, item_id)

    if not item:
        raise HTTPException(status_code=404, detail="Item not found")

    if item.isBorrowed:
        raise HTTPException(status_code=400, detail="Item is already borrowed")

    item.isBorrowed = True
    session.commit()
    session.refresh(item)
    return item
