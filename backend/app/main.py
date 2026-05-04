from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.db.session import engine, Base
from app.models import user, vehicle, driver, fuel
from app.api.routes import auth, protected, vehicle, driver, fuel, analytics


Base.metadata.create_all(bind=engine)
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(auth.router, prefix="/auth", tags=["Auth"])
app.include_router(vehicle.router, prefix="/vehicles", tags=["Vehicles"])
app.include_router(driver.router, prefix="/drivers", tags=["Drivers"])
app.include_router(fuel.router, prefix="/fuel", tags=["Fuel"])
app.include_router(protected.router, prefix="/user", tags=["User"])
app.include_router(analytics.router, prefix="/analytics", tags=["Analytics"])
@app.get("/")
def root():
    return {"message": "Fleet Management API running"}