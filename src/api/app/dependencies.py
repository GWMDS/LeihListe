from datetime import date, timedelta
from sqlmodel import Session, func, select
from models import Item, Customer, Borrowing
from database import engine
from sqlalchemy import text

def get_session():
    """Returns a new database session as a dependency."""
    with Session(engine) as session:
        yield session

def write_starting_data(session: Session):
    """Writes dummy data to the database, if there is no data yet."""
    item_list = [
        ("The Scrum Guide","Bücher"),
        ("Das Kapital","Bücher"),
        ("1984","Bücher"),
        ("Edding","Schreibwaren"),
        ("1000000000V Laserpointer","Kinderspielzeug"),
        ("Mikroskop","Laborequipment"),
        ("Multimeter","Laboreuqipment"),
        ("Biertischgarnitur","Veranstaltungszubehör"),
        ("Hunderoboter","Technik"),
        ("Plakataufsteller","Veranstaltungszubehör"),
        ("Lastenfahrrad","Fahrzeuge")
    ]
    state_list = [
        "neu",
        "beschädigt",
        "gut"
    ]

    with session:
        for i in range(1,11):
            if session.get(Item, i) is None:
                session.add(
                    Item(
                        id=i,
                        name=item_list[i-1][0],
                        category=item_list[i-1][1],
                        description = f"Toller Inventargegenstand mit einer sehr sehr sehr sehr sehr sehr sehr sehr sehr sehr sehr sehr sehr sehr sehr sehr sehr sehr sehr sehr sehr sehr langen Beschreibung {i}",
                        isBorrowed= bool(i%2),
                        state = state_list[i%3]
                    )
                    )

                borrowing = Borrowing(
                    item_id = i,
                    borrowing_date = date.today()-timedelta(days=2),
                    due_date = date.today() + timedelta(days=7)
                )
                if bool(i%2) is True:
                    borrowing.return_date=None
                else:
                    if bool(i%3) is True:
                        borrowing.return_date = date.today()
                        borrowing.due_date = date.today() - timedelta(days=1)
                    else:
                        borrowing.return_date = date.today()
                session.add(borrowing)

        session.flush()

        #This is necessary so POST-Requests work, since we set the ids manually
        session.execute(text("""
            SELECT setval(
            pg_get_serial_sequence('item', 'id'),
            (SELECT MAX(id) FROM item)
                )
            """))
        session.commit()
