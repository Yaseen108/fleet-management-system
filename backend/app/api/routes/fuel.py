from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.session import SessionLocal
from app.models.fuel import Fuel
from app.models.vehicle import Vehicle
from app.schemas.fuel import FuelCreate, FuelResponse
from app.core.dependencies import require_role

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# 🚛 Create fuel entry (Driver/Admin)
@router.post("/", response_model=FuelResponse)
def create_fuel(
    fuel: FuelCreate,
    db: Session = Depends(get_db),
    current_user = Depends(require_role(["admin", "driver"]))
):
    vehicle = db.query(Vehicle).filter(Vehicle.id == fuel.vehicle_id).first()

    if not vehicle:
        raise HTTPException(status_code=404, detail="Vehicle not found")

    price_per_litre = fuel.cost / fuel.litres

    new_fuel = Fuel(
        vehicle_id=fuel.vehicle_id,
        litres=fuel.litres,
        cost=fuel.cost,
        price_per_litre=price_per_litre
    )

    db.add(new_fuel)
    db.commit()
    db.refresh(new_fuel)

    return new_fuel


# 📋 List fuel entries (Admin/Manager)
@router.get("/", response_model=list[FuelResponse])
def list_fuel(
    db: Session = Depends(get_db),
    current_user = Depends(require_role(["admin", "manager"]))
):
    return db.query(Fuel).all()


# ✅ Approve fuel (Manager/Admin)
@router.post("/{fuel_id}/approve")
def approve_fuel(
    fuel_id: int,
    db: Session = Depends(get_db),
    current_user = Depends(require_role(["admin", "manager"]))
):
    fuel = db.query(Fuel).filter(Fuel.id == fuel_id).first()

    if not fuel:
        raise HTTPException(status_code=404, detail="Fuel entry not found")

    fuel.status = "approved"
    fuel.approved_by = current_user.id

    db.commit()

    return {"message": "Fuel entry approved"}