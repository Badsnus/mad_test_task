import asyncio
from typing import Annotated

from fastapi import Depends, FastAPI, File, Form, UploadFile

from config.config import S3_API_URL
from models import create_all_tables
from repo.db import DB, get_db
from schemas import MemSchema
from services import get_file_extension, S3Api

app = FastAPI()

s3_api = S3Api(S3_API_URL)


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
async def create_mem(file: Annotated[UploadFile, File()],
                     text: Annotated[str, Form()] = '',
                     db: DB = Depends(get_db)) -> MemSchema:
    mem = await db.mem.create(
        text=text,
        file_extension=get_file_extension(file.filename)
    )
    asyncio.create_task(s3_api.create(db, mem, file))  # специально без await
    return mem


@app.put("/memes/{id}")
async def update_mem(id: int):
    return {'id': id}


@app.delete("/memes/{id}")
async def delete_mem(id: int):
    return {'id': id}
