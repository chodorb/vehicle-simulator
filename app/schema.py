from pydantic import BaseModel

class UserBase(BaseModel):
    id: int
    login: str
    password: str

    class Config:
        orm_mode = True