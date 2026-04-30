from sqlalchemy import Column, Integer, Float, ForeignKey, DateTime, String
from sqlalchemy.orm import relationship
from datetime import datetime

from app.db.session import Base


class Fuel(Base):
    __tablename__ = "fuel_logs"

    id = Column(Integer, primary_key=True, index=True)

    vehicle_id = Column(Integer, ForeignKey("vehicles.id"), nullable=False)
    litres = Column(Float, nullable=False)
    cost = Column(Float, nullable=False)
    price_per_litre = Column(Float, nullable=False)

    created_at = Column(DateTime, default=datetime.utcnow)

    status = Column(String, default="pending")  # pending / approved
    approved_by = Column(Integer, ForeignKey("users.id"), nullable=True)

    vehicle = relationship("Vehicle")