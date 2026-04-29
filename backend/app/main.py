from fastapi import FastAPI
from app.db.session import engine, Base
from app.models import user, vehicle, driver
from app.api.routes import auth, protected, vehicle, driver


Base.metadata.create_all(bind=engine)
app = FastAPI()
app.include_router(auth.router, prefix="/auth", tags=["Auth"])
app.include_router(vehicle.router, prefix="/vehicles", tags=["Vehicles"])
app.include_router(driver.router, prefix="/drivers", tags=["Drivers"])
app.include_router(protected.router, prefix="/user", tags=["User"])
@app.get("/")
def root():
    return {"message": "Fleet Management API running"}