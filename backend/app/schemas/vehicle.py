from pydantic import BaseModel


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

    class Config:
        from_attributes = True