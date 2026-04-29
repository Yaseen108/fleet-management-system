from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import relationship
from app.db.session import Base


class Driver(Base):
    __tablename__ = "drivers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    license_number = Column(String, unique=True, nullable=False)
    license_expiry = Column(Date, nullable=False)
    status = Column(String, default="active")  # active / inactive

    # inside class Driver
    vehicle = relationship("Vehicle", back_populates="driver", uselist=False)