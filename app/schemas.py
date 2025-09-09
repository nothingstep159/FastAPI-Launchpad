# app/schemas.py
from pydantic import BaseModel, Field, ConfigDict

class UserCreate(BaseModel):
    email: str
    password: str = Field(min_length=8)

class UserOut(BaseModel):
    id: int
    email: str
    model_config = ConfigDict(from_attributes=True)  # <-- replaces class Config
