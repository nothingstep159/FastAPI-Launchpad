from fastapi import FastAPI
from .routers import auth


app = FastAPI(title="FastAPI Launchpad")


@app.get("/health")
def health():
    return {"status": "ok"}


app.include_router(auth.router)
