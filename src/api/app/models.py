from sqlmodel import SQLModel, Field

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
    