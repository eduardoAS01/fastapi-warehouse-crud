from pydantic import BaseModel, EmailStr, ConfigDict
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
    updated_at: datetime | None = None

    model_config = ConfigDict(from_attributes=True)

class ClientUpdate(BaseModel):
    username: str | None = None
    email: EmailStr | None = None
    phone: str | None = None
    password: str | None = None

    model_config = ConfigDict(from_attributes=True)

class ClientLogin(BaseModel):
    email: EmailStr
    password: str