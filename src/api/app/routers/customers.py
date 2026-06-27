from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from models import Customer
from dependencies import get_session

router = APIRouter(
    prefix="/api/customers",
    tags=["customers"]
)

# issue 63 - get all customers with details
@router.get("/all")#, response_model=Customers)
def get_customers(session: Session = Depends(get_session))-> list[Customer]:
    """Returns all customers in the database."""
    customers = session.exec(select(Customer)).all()
    return customers