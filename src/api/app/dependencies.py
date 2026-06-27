from datetime import date
from sqlmodel import Session
from models import Item, Customer, Borrowing
from database import engine

def get_session():
    """Returns a new database session as a dependency."""
    with Session(engine) as session:
        yield session

def write_starting_data(session: Session):
    """Writes dummy data to the database, if there is no data yet."""
    with session:
        for i in range(10):
            if session.get(Item, i) is None:
                db_item = Item(id=i,
                            name=f"Customer {i}",
                            description=f"Description for item {i}",
                            state="new",
                            isBorrowed= i % 2 == 0,
                            category="general")
                session.add(db_item)
        
            if session.get(Customer, i) is None:
                db_customer = Customer(customer_id=i,
                            customer_name=f"Customer {i}")
                session.add(db_customer)
                
        session.commit()

        for j in range(5):
            if session.get(Borrowing, j) is None:
                db_borrowing = Borrowing(borrowing_id=j,
                            item_id=((j+1)%2),
                            customer_id=((j+5)%2),
                            borrowing_date=date.today(),
                            return_date=date.today())
                session.add(db_borrowing)

        session.commit()
