from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from models import Item, ItemBase, Borrowing
from dependencies import get_session
from datetime import date, timedelta

router = APIRouter(
    prefix="/api/items",
    tags=["items"]
)


@router.get("/")#, response_model=Item)
def get_items(session: Session = Depends(get_session))-> list[Item]:
    """
    Returns all items in the database.
    
    Args: session (Session): Database session, provided as a dependency.

    Returns: items (list[Item]): A list of all items in the database.
    """
    items = session.exec(select(Item)).all()
    return items


@router.get("/{item_id}")#, response_model=Item)
def get_item(item_id: int, session: Session = Depends(get_session)) -> Item:
    """
    Returns one item by id.
    
    Args: item_id (int): The id of the item to retrieve, as a path parameter.
        session (Session): Database session, provided as a dependency.


    Returns: item (Item): The item with the specified id.

    Raises: HTTPException (404): If the item with the specified id is not found in the database.
    """
    item = session.get(Item, item_id)

    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item


@router.post("/")#, response_model=Item)
def create_item(item: ItemBase, session: Session = Depends(get_session)) -> Item:
    """
    Creates a new item in the database.
    
    Args: item (ItemBase): The item to create.
        session (Session): Database session, provided as a dependency.

    Returns: db_item (Item): The created item.
    """
    db_item = Item.model_validate(item)
    session.add(db_item)
    session.commit()
    session.refresh(db_item)
    return db_item


@router.put("/{item_id}")#, response_model=Item)
def update_item(item_id: int, item: ItemBase, session: Session = Depends(get_session)) -> Item:
    """
    Updates an item in the database.
    
    Args: item_id (int): The id of the item to update, as a path parameter.
        item (ItemBase): The updated item data.
        session (Session): Database session, provided as a dependency.

    Returns: db_item (Item): The updated item.

    Raises: HTTPException (404): If the item with the specified id is not found in the database.
    """
    db_item = session.get(Item, item_id)

    if not db_item:
        raise HTTPException(status_code=404, detail="Item not found")

    db_item.sqlmodel_update(item.model_dump())
    session.add(db_item)
    session.commit()
    session.refresh(db_item)
    return db_item


@router.delete("/{item_id}")#, response_model=Item)
def delete_item(item_id: int, session: Session = Depends(get_session)) -> dict:
    """
    Deletes an item from the database.
    
    Args: item_id (int): The id of the item to delete, as a path parameter.
        session (Session): Database session, provided as a dependency.
    
    Returns: message (dict): A message indicating that the item was deleted successfully.

    Raises: HTTPException (404): If the item with the specified id is not found in the database.
    """
    item = session.get(Item, item_id)

    if not item:
        raise HTTPException(status_code=404, detail="Item not found")

    session.delete(item)
    session.commit()
    return {"message": "Item deleted successfully"}


@router.put("/borrow/{item_id}")#, response_model=Item)
def borrow_item(item_id: int, session: Session = Depends(get_session)) -> Item:
    """
    Marks an item as borrowed.
    
    Args: item_id (int): The id of the item to borrow, as a path parameter.
        session (Session): Database session, provided as a dependency.

    Returns: item (Item): The borrowed item.

    Raises: HTTPException (404): If the item with the specified id is not found in the database.
        HTTPException (400): If the item is already borrowed.
    """
    item = session.get(Item, item_id)

    if not item:
        raise HTTPException(status_code=404, detail="Item not found")

    if item.isBorrowed:
        raise HTTPException(status_code=400, detail="Item is already borrowed")

    item.isBorrowed = True
    new_borrowing = Borrowing(
        item_id = item.id,
        borrowing_date = date.today(),
        due_date = date.today() + timedelta(days=7),
        return_date = None
    )
    session.add(new_borrowing)

    session.commit()
    session.refresh(item)
    return item


# issue 63 - return single item
@router.put("/return/{item_id}")#, response_model=Item)
def return_item(item_id: int, session: Session = Depends(get_session)) -> Item:
    """Marks an item as returned."""
    item = session.get(Item, item_id)

    if not item:
        raise HTTPException(status_code=404, detail="Item not found")

    if (item.isBorrowed) is False:
        raise HTTPException(status_code=400, detail="Item is already returned")

    item.isBorrowed = False
    session.commit()
    session.refresh(item)
    return item