from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.session import SessionLocal
from app.models.driver import Driver
from app.schemas.driver import DriverCreate, DriverResponse
from app.core.dependencies import require_role

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=DriverResponse)
def create_driver(
    driver: DriverCreate,
    db: Session = Depends(get_db),
    current_user = Depends(require_role(["admin"]))
):
    existing = db.query(Driver).filter(
        Driver.license_number == driver.license_number
    ).first()

    if existing:
        raise HTTPException(status_code=400, detail="Driver already exists")

    new_driver = Driver(**driver.model_dump())

    db.add(new_driver)
    db.commit()
    db.refresh(new_driver)

    return new_driver


@router.get("/", response_model=list[DriverResponse])
def list_drivers(
    db: Session = Depends(get_db),
    current_user = Depends(require_role(["admin", "manager"]))
):
    return db.query(Driver).all()