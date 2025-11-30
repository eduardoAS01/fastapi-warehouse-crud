from models.client import Client
from schemas.client import ClientCreate,ClientUpdate
from sqlalchemy.orm import Session
from core.security import hash_password

def create_client(db: Session, data: ClientCreate):
    client_data = data.model_dump()
    hashed = hash_password(client_data["password"])
    client_data["password_hash"] = hashed

    del client_data["password"]
    new_client = Client(**client_data)

    db.add(new_client)
    db.commit()
    db.refresh(new_client)

    return new_client

def get_client(db: Session, client_id: int):
    client = db.query(Client).filter(Client.id == client_id).first()
    return client

def get_all_clients(db: Session):
    clients = db.query(Client).all()
    return clients

def update_client(db: Session, client_id: int, data:ClientUpdate):
    client = db.query(Client).filter(Client.id == client_id).first()
    
    if client is None:
        return None
    
    updated_data = data.model_dump(exclude_unset=True)

    if "password" in updated_data:
        hashed = hash_password(updated_data["password"])
        updated_data["password_hash"] = hashed
        del updated_data["password"]

    for key,value in updated_data.items():
        setattr(client,key,value)

    db.commit()
    db.refresh(client)

    return client

def delete_client(db: Session, client_id: int):
    client = db.query(Client).filter(Client.id == client_id).first()
    
    if client is None:
        return None
    
    db.delete(client)
    db.commit()

    return True