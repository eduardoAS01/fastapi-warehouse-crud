from sqlalchemy import Column,Integer,String,DateTime
from sqlalchemy import func
from core.base import Base

class Client(Base):
    __tablename__ = "clients"

    id = Column(Integer,primary_key=True,index=True,autoincrement=True)
    username = Column(String(50),nullable=False,unique=True,index=True)
    email = Column(String(150),nullable=False,unique=True,index=True)
    phone = Column(String(16),nullable=True)
    password_hash = Column(String(255),nullable=False)

    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    def __repr__(self):
        return f"<Client id={self.id} username={self.username} email={self.email} >"