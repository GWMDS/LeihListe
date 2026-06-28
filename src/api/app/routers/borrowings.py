from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from sqlalchemy.sql.operators import is_
from models import BorrowingBase, Borrowing, BorrowingDetails, Item, BorrowingNew
from dependencies import get_session
from datetime import date


router = APIRouter(
    prefix="/api/borrowings",
    tags=["borrowings"]
)


## create a borrowing for an item
#@router.post("/create")#, response_model=Borrowing)
#def create_borrowing(borrowing_new: BorrowingNew, session: Session = Depends(get_session))-> Borrowing:
#    """Creates a new borrowing in the database."""
#    # no customer_id in use, thats why cust_id = 0
#    cust_id = 0
#
#    item = session.get(Item, borrowing_new.item_id)
#
#    if not item:
#        raise HTTPException(status_code=404, detail=f"Item {borrowing_new.item_id} not found")
#
#    borrowing = Borrowing(
#        item_id=borrowing_new.item_id,
#        customer_id=cust_id,
#        borrowing_date=borrowing_new.borrowing_date,
#        return_date=None,
#        due_date=(borrowing_new.due_date)
#    )
#    session.add(borrowing)
#    session.commit()
#    session.refresh(borrowing)
#    return borrowing



# return an item
#@router.put("/return/{item_id}")#, response_model=Borrowing)
#def return_item(item_id: int, session: Session = Depends(get_session))-> None:
#    """Removes a borrowing from the database.
#    Method is without return value."""
#    borrowings = session.exec(select(Borrowing).where(Borrowing.item_id == item_id, is_(Borrowing.return_date, None)))
#
#    if not borrowings:
#        raise HTTPException(status_code=404, detail=f"No borrowings for Item {Borrowing.item_id} found")
#
#    for borrowing in borrowings:
#        db_borrowing = session.get(Borrowing, borrowing.borrowing_id)
#        if not db_borrowing:
#            raise HTTPException(status_code=404, detail="Item not found")
#        borrowing.return_date = date.today()
#        db_borrowing.sqlmodel_update(borrowing.model_dump(exclude_unset=True))
#        session.add(db_borrowing)
#        session.commit()
#        session.refresh(db_borrowing)
#        print(f"Borrowing {db_borrowing.borrowing_id} for Item {db_borrowing.item_id} returned on {db_borrowing.return_date}")
    

# issue 63 - get all borrowings with details
@router.get("/all/details")#, response_model=Borrowing)
def get_borrowings_with_details(session: Session = Depends(get_session))-> list[BorrowingDetails]:
    """Returns all borrowings with details from the database."""
    borrowings = session.exec(select(Borrowing)).all()
    if not borrowings:
        raise HTTPException(status_code=404, detail="no borrowings found")

    borrowingresponse:list[BorrowingDetails] = []

    for borrowing in borrowings:
        borrowed_item_name = session.get(Item,borrowing.item_id).name

        borrow_response = BorrowingDetails(
            item_id=borrowing.item_id,
            borrowing_date=borrowing.borrowing_date,
            return_date=borrowing.return_date,
            due_date=borrowing.due_date,
            item_name=borrowed_item_name
        )

        if borrow_response.return_date is None:
            borrowingresponse.append(borrow_response)

    return borrowingresponse


## issue 63 - get all borrowings with details and with item_name
#@router.get("/all/details/item_name")#, response_model=Borrowing)
#def get_borrowings_with_details_and_itemname(session: Session = Depends(get_session))-> list[BorrowingDetails]:
#    """Returns all borrowings with details and item names from the database."""
#    borrowings = session.exec(select(Borrowing)).all()
#
#    if not borrowings:
#        raise HTTPException(status_code=404, detail="no borrowings found")
#
#    for borrowing in borrowings:
#        # get the item name for each borrowing
#        item = session.get(Item, borrowing.item_id)
#
#        borrowing_details = BorrowingDetails(
#            borrowing_id=borrowing.borrowing_id,
#            item_id=borrowing.item_id,
#            customer_id=0,
#            borrowing_date=borrowing.borrowing_date,
#            return_date=borrowing.return_date,
#            due_date=borrowing.due_date,
#            item_name=item.name
#        )
#
#        yield borrowing_details
#
#
## issue 63 - get all active borrowings with details and with item_name
#@router.get("/all/details/item_name/<active>")#, response_model=Borrowing)
#def get_active_borrowings_with_details_and_itemname(session: Session = Depends(get_session))-> list[BorrowingBase]:
#    """Returns all borrowings with details and item names from the database."""
#    borrowings = session.exec(select(Borrowing).where(is_(Borrowing.return_date, None)))
#
#    if not borrowings:
#        raise HTTPException(status_code=404, detail="no borrowings found")
#
#    for borrowing in borrowings:
#        # get the item name for each borrowing
#        item = session.get(Item, borrowing.item_id)
#
#        borrowing_details = BorrowingDetails(
#            borrowing_id=borrowing.borrowing_id,
#            item_id=borrowing.item_id,
#            customer_id=0,
#            borrowing_date=borrowing.borrowing_date,
#            return_date=borrowing.return_date,
#            due_date=borrowing.due_date,
#            item_name=item.name
#        )
#
#        yield borrowing_details
#