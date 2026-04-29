from sqlalchemy import Column, Integer, String, Float
from app.db.session import Base


class Vehicle(Base):
    __tablename__ = "vehicles"

    id = Column(Integer, primary_key=True, index=True)
    registration_number = Column(String, unique=True, index=True, nullable=False)
    model = Column(String, nullable=False)
    fuel_type = Column(String, nullable=False)
    tank_capacity = Column(Float, nullable=False)
    status = Column(String, default="active")  # active / inactive