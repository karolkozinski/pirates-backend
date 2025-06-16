from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from models.ship import Ship
from schemas.ship import ShipRead

router = APIRouter()

@router.get("/ships", response_model=list[ShipRead])
def read_ships(db: Session = Depends(get_db)):
    return db.query(Ship).all()