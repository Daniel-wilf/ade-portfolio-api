from pydantic import BaseModel, Field

class ItemIn(BaseModel):
    name: str = Field(min_length=1)
    qty: int = 0

class ItemOut(ItemIn):
    id: int
