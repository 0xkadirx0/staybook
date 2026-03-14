from pydantic import BaseModel

class Room(BaseModel):
    id: int
    name: str
    price: int

    class Config:
        orm_mode = True
