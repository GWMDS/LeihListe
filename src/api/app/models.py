from datetime import date, timedelta
from sqlmodel import SQLModel, Field
from sqlalchemy import ForeignKey

class ItemBase(SQLModel):
    """
    This is the base class for an item that is stored in the database.
    The items can be borrowed.
    """
    name: str = Field()
    description: str = Field()
    state: str = Field()    #zu enum aendern
    isBorrowed: bool = Field(default=False) #True if item is borrowed, False otherwise
    category: str = Field() #zu enum aendern

class Item(ItemBase, table=True):
    """
    This is an item that is stored in the database.
    The items can be borrowed.
    """
    id: int = Field(default=None, primary_key=True)

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
    borrowing_id: int | None = Field(default=None, primary_key=True)
    item_id: int = Field(ForeignKey(Item.id))
    customer_id: int = Field(ForeignKey(Customer.customer_id))
    borrowing_date: date = Field()
    return_date: date = Field(nullable=True)
    due_date: date = Field()

class BorrowingDetails(Borrowing, table=False):
    """
    This is the base class for a borrowing that is stored in the database.
    """
    item_name: str = Field()

class BorrowingNew(SQLModel, table=False):
    """
    TODO: This is the base class for a borrowing that is created in the database.
    """
    item_id: int = Field()
    # noch nicht: customer_id: int = Field()
    borrowing_date: date = Field(default=date.today())
    due_date: date = Field(default=date.today() + timedelta(days=7))
