from fastapi import FastAPI
from .database import Base, engine
from .routers import auth

app = FastAPI(title="FastAPI Launchpad")
Base.metadata.create_all(bind=engine)

@app.get("/health")
def health():
    return {"status": "ok"}

app.include_router(auth.router)
