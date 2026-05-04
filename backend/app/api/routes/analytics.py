from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func
from datetime import date
from fastapi import Query

from app.db.session import SessionLocal
from app.models.fuel import Fuel
from app.models.vehicle import Vehicle
from app.core.dependencies import require_role

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# 📊 Total fuel cost per vehicle
@router.get("/fuel-cost-per-vehicle")
def fuel_cost_per_vehicle(
    start_date: date | None = Query(default=None),
    end_date: date | None = Query(default=None),
    db: Session = Depends(get_db),
    current_user = Depends(require_role(["admin", "manager"]))
):
    query = (
        db.query(
            Vehicle.registration_number.label("vehicle"),
            func.sum(Fuel.cost).label("total_cost")
        )
        .join(Fuel, Fuel.vehicle_id == Vehicle.id)
    )

    # ✅ Apply filters if provided
    if start_date:
        query = query.filter(Fuel.created_at >= start_date)

    if end_date:
        query = query.filter(Fuel.created_at <= end_date)

    result = query.group_by(Vehicle.registration_number).all()

    return [
        {
            "vehicle": row.vehicle,
            "total_cost": row.total_cost
        }
        for row in result
    ]


# ⛽ Total litres per vehicle
@router.get("/fuel-litres-per-vehicle")
def fuel_litres_per_vehicle(
    start_date: date | None = Query(default=None),
    end_date: date | None = Query(default=None),
    db: Session = Depends(get_db),
    current_user = Depends(require_role(["admin", "manager"]))
):
    query = (
        db.query(
            Vehicle.registration_number.label("vehicle"),
            func.sum(Fuel.litres).label("total_litres")
        )
        .join(Fuel, Fuel.vehicle_id == Vehicle.id)
    )

    if start_date:
        query = query.filter(Fuel.created_at >= start_date)

    if end_date:
        query = query.filter(Fuel.created_at <= end_date)

    result = query.group_by(Vehicle.registration_number).all()

    return [
        {
            "vehicle": row.vehicle,
            "total_litres": row.total_litres
        }
        for row in result
    ]


# 📈 Average price per litre per vehicle
@router.get("/average-price-per-litre")
def avg_price_per_litre(
    start_date: date | None = Query(default=None),
    end_date: date | None = Query(default=None),
    db: Session = Depends(get_db),
    current_user = Depends(require_role(["admin", "manager"]))
):
    query = (
        db.query(
            Vehicle.registration_number.label("vehicle"),
            func.avg(Fuel.price_per_litre).label("avg_price")
        )
        .join(Fuel, Fuel.vehicle_id == Vehicle.id)
    )

    if start_date:
        query = query.filter(Fuel.created_at >= start_date)

    if end_date:
        query = query.filter(Fuel.created_at <= end_date)

    result = query.group_by(Vehicle.registration_number).all()

    return [
        {
            "vehicle": row.vehicle,
            "avg_price": row.avg_price
        }
        for row in result
    ]