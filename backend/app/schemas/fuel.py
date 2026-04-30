from pydantic import BaseModel
from datetime import datetime


class FuelCreate(BaseModel):
    vehicle_id: int
    litres: float
    cost: float


class FuelResponse(BaseModel):
    id: int
    vehicle_id: int
    litres: float
    cost: float
    price_per_litre: float
    status: str
    created_at: datetime

    class Config:
        from_attributes = True