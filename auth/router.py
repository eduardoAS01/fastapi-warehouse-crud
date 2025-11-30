from fastapi import APIRouter,Depends,HTTPException
from .login_client import authenticate_client
from sqlalchemy.orm import Session
from core.db import get_db
from schemas.client import ClientLogin,ClientRead

router = APIRouter(
    prefix="/login",
    tags=["login"]
)

router.post("/",response_model=ClientRead)
def login_client(data: ClientLogin,db: Session = Depends(get_db)):
    client = authenticate_client(db,data)
    return client