from sqlmodel import Session
from models import Item
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
