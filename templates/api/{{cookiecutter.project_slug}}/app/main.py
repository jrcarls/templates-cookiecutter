from fastapi import FastAPI
from app.core.config import settings
from app.health.router import router as health_router

app = FastAPI(
    title=settings.app_name,
    openapi_url=f"{settings.api_v1_prefix}/openapi.json",
    docs_url=f"{settings.api_v1_prefix}/docs",
)

app.include_router(health_router, prefix=f"{settings.api_v1_prefix}/health", tags=["health"])
