from schemas.client import ClientLogin
from core.security import verify_password
from sqlalchemy.orm import Session
from models.client import Client

def authenticate_client(db: Session, data: ClientLogin):
    client = db.query(Client).filter(Client.email == data.email).first()

    if client is None:
        return None
    
    if not verify_password(data.password, client.password_hash):
        return None
    
    return client