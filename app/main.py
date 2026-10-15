from fastapi import FastAPI

from app.api.routes import router
from app.config import settings

app = FastAPI(title=settings.app_name, debug=settings.app_debug)
app.include_router(router)


@app.get("/health")
def health() -> dict:
    return {
        "status": "ok",
        "service": settings.app_name,
        "environment": settings.app_env,
    }


@app.get("/")
def root() -> dict:
    return {
        "message": f"{settings.app_name} is running",
        "docs": "/docs",
    }
