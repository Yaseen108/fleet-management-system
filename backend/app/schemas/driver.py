from pydantic import BaseModel
from datetime import date


class DriverCreate(BaseModel):
    name: str
    license_number: str
    license_expiry: date


class DriverResponse(BaseModel):
    id: int
    name: str
    license_number: str
    license_expiry: date
    status: str

    class Config:
        from_attributes = True