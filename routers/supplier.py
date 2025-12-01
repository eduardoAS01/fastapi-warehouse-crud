from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from core.db import get_db
from crud.supplier import create_supplier,get_all_suppliers,get_supplier,update_supplier,delete_supplier
from schemas.supplier import SupplierCreate,SupplierRead,SupplierUpdate

router = APIRouter(prefix="/suppliers", tags=["suppliers"])

@router.get("/",response_model=list[SupplierRead])
def list_suppliers(db: Session = Depends(get_db)):
    suppliers = get_all_suppliers(db)
    return suppliers

@router.get("/{supplier_id}", response_model=SupplierRead)
def read_supplier(supplier_id: int, db: Session = Depends(get_db)):
    supplier = get_supplier(db,supplier_id)
    if supplier is None:
        raise HTTPException(status_code=404,detail="Supplier not found")

    return supplier

@router.post("/", response_model=SupplierRead)
def make_supplier(data: SupplierCreate, db: Session = Depends(get_db)):
    return create_supplier(db,data)

@router.put("/{supplier_id}",response_model=SupplierRead)
def change_supplier(supplier_id: int, data: SupplierUpdate, db: Session = Depends(get_db)):
    supplier = update_supplier(db,supplier_id,data)

    if supplier is None:
        raise HTTPException(status_code=404,detail="Supplier not found")

    return supplier

@router.delete("/{supplier_id}",status_code=200)
def remove_supplier(supplier_id: int,db: Session = Depends(get_db)):
    supplier = delete_supplier(db,supplier_id)
    
    if supplier is not True:
        raise HTTPException(status_code=404,detail="Client not found")
    
    return {"detail":"Supplier deleted"}