from pydantic import BaseModel, EmailStr
from datetime import datetime

class ClientBase(BaseModel):
    username: str
    email: EmailStr
    phone: str | None = None

class ClientCreate(ClientBase):
    password: str

class ClientRead(ClientBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True     