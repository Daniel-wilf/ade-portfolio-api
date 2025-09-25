from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db import SessionLocal, engine
from app.models import Base, Item
from app.schemas.item import ItemIn, ItemOut

router = APIRouter(prefix="/items", tags=["items"])

# dev-only: create tables at import; for prod use migrations
Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("", response_model=ItemOut, status_code=201)
def create_item(payload: ItemIn, db: Session = Depends(get_db)):
    obj = Item(name=payload.name, qty=payload.qty)
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return ItemOut(id=obj.id, name=obj.name, qty=obj.qty)

@router.get("", response_model=List[ItemOut])
def list_items(db: Session = Depends(get_db)):
    rows = db.query(Item).all()
    return [ItemOut(id=r.id, name=r.name, qty=r.qty) for r in rows]
