# app/schemas.py
from pydantic import BaseModel, EmailStr, Field, ConfigDict

class UserCreate(BaseModel):
    email: EmailStr
    password: str = Field(min_length=8)

class UserOut(BaseModel):
    id: int
    email: EmailStr
    model_config = ConfigDict(from_attributes=True)  # <-- replaces class Config
