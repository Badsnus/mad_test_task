from fastapi import Depends, FastAPI

from models import create_all_tables
from repo.db import DB, get_db

app = FastAPI()


@app.on_event("startup")
async def on_startup():
    # Можно переделать на alembic
    await create_all_tables()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/memes")
async def root(db: DB = Depends(get_db)):
    print(db.mem.session)
    return []


@app.get("/memes/{id}")
async def root(id: int):
    return {'id': id}


@app.post("/memes")
async def root(id: int):
    return {}


@app.put("/memes/{id}")
async def root(id: int):
    return {'id': id}


@app.delete("/memes/{id}")
async def root(id: int):
    return {'id': id}
