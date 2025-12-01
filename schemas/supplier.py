from pydantic import BaseModel, ConfigDict
from datetime import datetime

class SupplierCreate(BaseModel):
    name: str
    address: str |None = None
    phone: str |None = None

class SupplierRead(SupplierCreate):
    id: int
    created_at: datetime
    updated_at: datetime |None = None

    model_config = ConfigDict(from_attributes=True)

class SupplierUpdate(BaseModel):
    name: str |None = None
    address: str |None = None
    phone: str |None = None

    model_config = ConfigDict(from_attributes=True)
