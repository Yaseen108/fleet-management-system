from app.models.driver import Driver
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.session import SessionLocal
from app.models.vehicle import Vehicle
from app.schemas.vehicle import VehicleCreate, VehicleResponse
from app.core.dependencies import require_role

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=VehicleResponse)
def create_vehicle(
    vehicle: VehicleCreate,
    db: Session = Depends(get_db),
    current_user = Depends(require_role(["admin"]))
):
    existing = db.query(Vehicle).filter(
        Vehicle.registration_number == vehicle.registration_number
    ).first()

    if existing:
        raise HTTPException(status_code=400, detail="Vehicle already exists")

    new_vehicle = Vehicle(**vehicle.model_dump())

    db.add(new_vehicle)
    db.commit()
    db.refresh(new_vehicle)

    return new_vehicle


@router.get("/", response_model=list[VehicleResponse])
def list_vehicles(
    db: Session = Depends(get_db),
    current_user = Depends(require_role(["admin", "manager"]))
):
    return db.query(Vehicle).all()

@router.post("/{vehicle_id}/assign-driver/{driver_id}")
def assign_driver(
    vehicle_id: int,
    driver_id: int,
    db: Session = Depends(get_db),
    current_user = Depends(require_role(["admin"]))
):
    vehicle = db.query(Vehicle).filter(Vehicle.id == vehicle_id).first()
    driver = db.query(Driver).filter(Driver.id == driver_id).first()

    if not vehicle:
        raise HTTPException(status_code=404, detail="Vehicle not found")

    if not driver:
        raise HTTPException(status_code=404, detail="Driver not found")

    vehicle.driver_id = driver.id

    db.commit()
    db.refresh(vehicle)

    return {"message": "Driver assigned successfully"}