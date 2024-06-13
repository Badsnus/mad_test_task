import asyncio
from typing import Annotated

from fastapi import Depends, FastAPI, File, Form, UploadFile

from config.config import S3_API_URL
from models import create_all_tables
from repo.db import DB, get_db
from schemas import StatusSchema, MemSchema
from services import get_file_extension, S3Api

app = FastAPI()

s3_api = S3Api(S3_API_URL)


@app.on_event("startup")
async def on_startup():
    # Можно переделать на alembic
    await create_all_tables()


@app.get("/memes")
async def get_mems(db: DB = Depends(get_db),
                   limit: int = 10,
                   offset: int = 0) -> list[MemSchema]:
    return await db.mem.all(limit=limit, offset=offset)


@app.get("/memes/{uuid}")
async def get_mem(uuid: str,
                  db: DB = Depends(get_db)) -> MemSchema | StatusSchema:
    mem = await db.mem.get(uuid)
    if mem is None:
        return StatusSchema(status='error | NOT FOUND')
    return mem


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


@app.put("/memes/{uuid}")
async def update_mem(uuid: str,
                     file: Annotated[UploadFile, File()],
                     text: Annotated[str, Form()] = '',
                     db: DB = Depends(get_db)) -> MemSchema:
    mem = await db.mem.get(uuid)
    old_file_extension = mem.file_extension

    await db.mem.update(
        mem,
        text=text,
        file_extension=get_file_extension(file.filename),
        url=None,
    )

    asyncio.create_task(s3_api.update(db, mem, file, old_file_extension))  # специально без await

    return mem


@app.delete("/memes/{uuid}")
async def delete_mem(uuid: str,
                     db: DB = Depends(get_db)) -> StatusSchema:
    mem = await db.mem.get(uuid)
    await db.mem.delete(mem)

    asyncio.create_task(s3_api.delete(mem))  # специально без await

    return StatusSchema(status='ok')
