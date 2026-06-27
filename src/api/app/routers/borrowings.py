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

