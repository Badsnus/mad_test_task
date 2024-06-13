from fastapi import Depends, FastAPI

from config.config import s3_api
from models import create_all_tables
from repo.db import DB, get_db

app = FastAPI()


@app.on_event("startup")
async def on_startup():
    # Можно переделать на alembic
    await create_all_tables()


@app.get("/memes")
async def get_mems(db: DB = Depends(get_db)):
    return []


@app.get("/memes/{id}")
async def get_mem(id: int):
    return {'id': id}


@app.post("/memes")
async def create_mem(id: int, db: DB = Depends(get_db)):
    return {}


@app.put("/memes/{id}")
async def update_mem(id: int):
    return {'id': id}


@app.delete("/memes/{id}")
async def delete_mem(id: int):
    return {'id': id}
