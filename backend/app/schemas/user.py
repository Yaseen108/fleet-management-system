from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    email: EmailStr
    password: str
    role: str = "driver"  # NEW (default)

class UserLogin(BaseModel):
    email: EmailStr
    password: str
