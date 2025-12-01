from sqlalchemy.orm import Session
from models.supplier import Supplier
from schemas.supplier import SupplierCreate,SupplierRead,SupplierUpdate

def create_supplier(db: Session , data: SupplierCreate):
    supplier_data = data.model_dump()

    new_supplier = Supplier(**supplier_data)

    db.add(new_supplier)
    db.commit()
    db.refresh(new_supplier)

    return new_supplier

def get_supplier(db: Session, supplier_id: int):
    supplier = db.query(Supplier).filter(Supplier.id == supplier_id).first()
    
    if supplier is None:
        return None
    
    return supplier

def get_all_suppliers(db: Session):
    suppliers = db.query(Supplier).all()

    return suppliers

def update_supplier(db: Session,supplier_id: int, data: SupplierUpdate):
    supplier = db.query(Supplier).filter(Supplier.id == supplier_id).first()

    if supplier is None:
        return None
    
    updated_data = data.model_dump(exclude_unset=True)
    
    for key,value in updated_data.items():
        setattr(supplier,key,value)
    
    db.commit()
    db.refresh(supplier)

    return supplier

def delete_supplier(db: Session,supplier_id: int):
    supplier = db.query(Supplier).filter(Supplier.id == supplier_id).first()
    
    if supplier is None:
        return None
    
    db.delete(supplier)
    db.commit()

    return True
