from sqlmodel import SQLModel, Field

class item(SQLModel, table=True):
    """
    This is an item that is stored in the database.
    The items can be borrowed.
    """
    id: int = Field(default=None, primary_key=True)
    name: str = Field()
    description: str = Field()
    state: str = Field()    #zu enum aendern
    status: bool = Field()  
    category: str = Field() #zu enum aendern
