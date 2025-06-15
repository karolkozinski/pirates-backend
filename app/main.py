from fastapi import FastAPI
from app.routes import game

app = FastAPI(
    title="Pirates MMO API",
    version="0.1.0"
)

app.include_router(game.router)