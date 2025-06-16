from pydantic import BaseModel

class ShipRead(BaseModel):
    id: int
    name: str
    type: str

    class Config:
        orm_mode = True