from datetime import date, timedelta
from sqlmodel import Session, func, select
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
                            name=f"Item {i}",
                            description=f"Description for item {i}",
                            state="new",
                            isBorrowed= i % 2 == 0,
                            category="general")
                session.add(db_item)
        session.commit()

        for j in range(1):
            if session.get(Customer, j) is None:
                    db_customer = Customer(customer_id=j,
                                customer_name=f"Customer {j}")
                    session.add(db_customer)

        cnt = session.exec(select(func.count(Borrowing.borrowing_id))).first()
        if cnt == 0:
            anzahl_demo = 3
            for k in range(anzahl_demo):
                db_borrowing = Borrowing(
                            item_id=((k+1)% anzahl_demo),
                            customer_id=0,
                            borrowing_date=date.today(),
                            return_date=(date.today() + timedelta(7)),
                            due_date=(date.today() + timedelta(7)))
                session.add(db_borrowing)

            for l in range(anzahl_demo):
                db_borrowing = Borrowing(
                            item_id=((l+1)% anzahl_demo),
                            customer_id=0,
                            borrowing_date=date.today(),
                            return_date=None,
                            due_date=(date.today() + timedelta(7)))
                session.add(db_borrowing)
        session.commit()
