from fastapi import APIRouter
from app.core import settings

api_router = APIRouter(prefix=settings.prefix.api)
routers = []
for router in routers:
    api_router.include_router(router)
