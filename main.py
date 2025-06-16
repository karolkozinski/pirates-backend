from fastapi import FastAPI
from app.api import game

app = FastAPI()

from routers import ships

app.include_router(ships.router, prefix="/api")