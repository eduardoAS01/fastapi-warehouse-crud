
"""
from sqlalchemy import Column,Integer,String,DateTime,Float,ForeignKey
from sqlalchemy import func
from core.base import Base

class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer,primary_key=True,nullable=False,autoincrement=True)
    name = Column(String(60),nullable=False,unique=True,index=True)
    description = Column(String(200),nullable=True)
    price = Column(Float,nullable=False)
    supplier_id = Column(ForeignKey)

    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    
"""
