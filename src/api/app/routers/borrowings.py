from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from models import Borrowing, BorrowingDetails, Item
from dependencies import get_session

router = APIRouter(
    prefix="/api/borrowings",
    tags=["borrowings"]
)

# issue 63 - get all borrowings with details
@router.get("/all/details")#, response_model=Borrowing)
def get_borrowings_with_details(session: Session = Depends(get_session))-> list[Borrowing]:
    """Returns all borrowings in the database."""
    borrowings = session.exec(select(Borrowing)).all()

    return borrowings


# issue 63 - get all borrowings with details
@router.get("/all/details")#, response_model=Borrowing)
def get_borrowings_with_details_for_customer(session: Session = Depends(get_session))-> list[Borrowing]:
    """Returns all borrowings for a specific customer."""
    borrowings = session.exec(select(Borrowing)).all()

    if not borrowings:
        raise HTTPException(status_code=404, detail="no borrowings found")

    return borrowings

# issue 63 - get all borrowings with details and with item_name
@router.get("/all/details/item")#, response_model=Borrowing)
def get_borrowings_with_details_and_itemdetails_for_customer(session: Session = Depends(get_session))-> list[BorrowingDetails]:
    """Returns all borrowings for a specific customer."""
    borrowings = session.exec(select(Borrowing)).all()

    if not borrowings:
        raise HTTPException(status_code=404, detail="no borrowings found")

    for borrowing in borrowings:
        # get the item name for each borrowing
        item = session.get(Item, borrowing.item_id)

        borrowingDetails = BorrowingDetails(
            borrowing_id=borrowing.borrowing_id,
            item_id=borrowing.item_id,
            customer_id=0,
            borrowing_date=borrowing.borrowing_date,
            return_date=borrowing.return_date,
            item_name=item.name
        )

        yield borrowingDetails

