# https://learnsql.de/blog/postgresql-datumsfunktionen/
from datetime import date
from sqlmodel import SQLModel, Field
# https://python4data.science/de/latest/data-processing/postgresql/sqlalchemy.html
from sqlalchemy import ForeignKey


class Item(SQLModel, table=True):
    """
    This is an item that is stored in the database.
    The items can be borrowed.
    """
    id: int = Field(default=None, primary_key=True)
    name: str = Field()
    description: str = Field()
    state: str = Field()    #zu enum aendern
    isBorrowed: bool = Field(default=False) #True if item is borrowed, False otherwise
    category: str = Field() #zu enum aendern

class Customer(SQLModel, table=True):
    """
    This is a customer who is stored in the database.
    Customers can borrow/return Items.
    """
    customer_id: int = Field(default=None, primary_key=True)
    customer_name: str = Field()

class Borrowing(SQLModel, table=True):
    """
    This is a borrowing.
    A borrowing shows who borrowed what when
    """
    borrowing_id: int = Field(default=None, primary_key=True)
    item_id: int = Field(ForeignKey(Item.id))
    customer_id: int = Field(ForeignKey(Customer.customer_id))
    borrowing_date: date = Field()
    return_date: date = Field()
