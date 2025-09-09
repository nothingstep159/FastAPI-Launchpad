# app/auth.py
from datetime import datetime, timedelta, timezone
from passlib.context import CryptContext
import jwt

SECRET_KEY = "CHANGE_ME_IN_ENV"
ALGORITHM = "HS256"
ACCESS_MINUTES = 30

pwd = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(p: str) -> str:
    return pwd.hash(p)

def verify_password(p: str, hashed: str) -> bool:
    return pwd.verify(p, hashed)

def create_access_token(sub: str, minutes: int = ACCESS_MINUTES) -> str:
    now = datetime.now(timezone.utc)              # tz-aware
    exp = now + timedelta(minutes=minutes)
    payload = {
        "sub": sub,
        "iat": int(now.timestamp()),              # numeric date per JWT spec
        "exp": int(exp.timestamp()),
    }
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)

def decode_token(token: str) -> dict:
    # By default PyJWT verifies 'exp'; require 'iat' too for discipline
    return jwt.decode(
        token,
        SECRET_KEY,
        algorithms=[ALGORITHM],
        options={"require": ["exp", "iat"]},
    )
