from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from core.db import get_db
from crud.client import create_client,get_client,get_all_clients,delete_client,update_client
from schemas.client import ClientCreate,ClientUpdate,ClientRead

router = APIRouter(prefix="/clients",tags=["clients"])

@router.get("/",response_model=list[ClientRead])
def list_clients(db: Session = Depends(get_db)):
    clients = get_all_clients(db)
    return clients

@router.get("/{client_id}", response_model=ClientRead)
def read_client(client_id: int, db: Session = Depends(get_db)):
    client = get_client(db,client_id)
    if client is None:
        raise HTTPException(status_code=404,detail="Client not found")

    return client

@router.post("/", response_model=ClientRead)
def make_client(data: ClientCreate, db: Session = Depends(get_db)):
    return create_client(db,data)

@router.put("/{client_id}",response_model=ClientRead)
def change_client(client_id: int, data: ClientUpdate, db: Session = Depends(get_db)):
    client = update_client(db,client_id,data)

    if client is None:
        raise HTTPException(status_code=404,detail="Client not found")

    return client

@router.delete("/{client_id}",status_code=204)
def remove_client(client_id: int,db: Session = Depends(get_db)):
    client = delete_client(db,client_id)

    if client is None:
        raise HTTPException(status_code=404,detail="Client not found")
 