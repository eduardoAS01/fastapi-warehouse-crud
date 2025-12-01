from sqlalchemy import Column,Integer,String,DateTime,Float,ForeignKey
from sqlalchemy import func
from core.base import Base

class Supplier(Base):
    __tablename__ ="suppliers"

    id = Column(Integer,primary_key=True,nullable=False,autoincrement=True,index=True)
    name = Column(String(60),nullable=False,index=True)
    address = Column(String(200),index=True)
    phone = Column(String(20),unique=True,index=True)

    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    def __repr__(self):
        return f"<Supplier id={self.id} name={self.name} phone={self.phone}>"