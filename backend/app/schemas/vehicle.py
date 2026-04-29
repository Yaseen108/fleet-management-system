from pydantic import BaseModel
from typing import Optional
from app.schemas.driver import DriverResponse


class VehicleCreate(BaseModel):
    registration_number: str
    model: str
    fuel_type: str
    tank_capacity: float


class VehicleResponse(BaseModel):
    id: int
    registration_number: str
    model: str
    fuel_type: str
    tank_capacity: float
    status: str

    driver: Optional[DriverResponse] = None  # NEW

    class Config:
        from_attributes = True