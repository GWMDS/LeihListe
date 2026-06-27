from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from models import Borrowing
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


# issue 63 - get all borrowings with details for one person
@router.get("/all/details/{customer_id}")#, response_model=Borrowing)
def get_borrowings_with_details_for_customer(customer_id: int, session: Session = Depends(get_session))-> list[Borrowing]:
    """Returns all borrowings for a specific customer."""
    borrowings = session.exec(select(Borrowing).where(Borrowing.customer_id == customer_id)).all()

    if  not customer_id in [borrowing.customer_id for borrowing in borrowings]:
        raise HTTPException(status_code=404, detail="no borrowings for customer found")

    return borrowings