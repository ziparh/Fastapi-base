import uvicorn
from fastapi import FastAPI
from contextlib import asynccontextmanager
from core import settings
from api import router as api_router
from core import db_helper


@asynccontextmanager
def lifespan(api: FastAPI):
    # start
    print("Starting app")
    yield
    # shutdown
    db_helper.dispose()
    print("Shutting down app")


app = FastAPI(lifespan=lifespan)
app.include_router(api_router)

if __name__ == '__main__':
    uvicorn.run('main:app', host=settings.run.host, port=settings.run.port, reload=True)