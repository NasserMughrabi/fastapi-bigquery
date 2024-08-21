from pydantic import BaseModel

# Define the Pydantic model for an item
class Item(BaseModel):
    id: str
    name: str