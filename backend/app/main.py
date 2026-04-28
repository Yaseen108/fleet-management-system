from fastapi import FastAPI
from app.db.session import engine, Base
from app.models import user
from app.api.routes import auth, protected


Base.metadata.create_all(bind=engine)
app = FastAPI()
app.include_router(auth.router, prefix="/auth", tags=["Auth"])
app.include_router(protected.router, prefix="/user", tags=["User"])
@app.get("/")
def root():
    return {"message": "Fleet Management API running"}