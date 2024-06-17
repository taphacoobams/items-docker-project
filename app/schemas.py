from pydantic import BaseModel

class ItemBase(BaseModel):
    name: str
    description: str = None
    price: float

class ItemCreate(ItemBase):
    pass

class ItemInDB(ItemBase):
    id: int

class ItemOut(BaseModel):
    id: int
    name: str
    description: str = None
    price: float