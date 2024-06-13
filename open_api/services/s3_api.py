import aiohttp
from fastapi import UploadFile

from models import Mem
from repo.db import DB


class S3Api:
    def __init__(self, url: str) -> None:
        self.url = url
        self.upload_url = self.url + '/upload'
        self.delete_url = self.url + '/delete'

    @staticmethod
    def get_key(uuid: str, file_extension: str) -> str:
        return uuid + '.' + file_extension

    async def create(self, db: DB, mem: Mem, file: UploadFile) -> None:
        # TODO check status code
        async with aiohttp.ClientSession() as session:
            resp = await session.post(self.upload_url, data=dict(
                file=await file.read(),
                key=self.get_key(mem.uuid, mem.file_extension),
            ))
            json = await resp.json()
            await db.mem.update(mem, url=json['url'])

    async def update(self,
                     db: DB,
                     mem: Mem,
                     file: UploadFile,
                     old_file_extension: str) -> None:
        # TODO check status code
        async with aiohttp.ClientSession() as session:
            resp = await session.post(self.upload_url, data=dict(
                file=await file.read(),
                key=self.get_key(mem.uuid, mem.file_extension),
            ))
            json = await resp.json()
            await db.mem.update(mem, url=json['url'])

            if old_file_extension != mem.file_extension:
                await self.delete(mem, old_file_extension)

    async def delete(self, mem: Mem, old_file_extension: str = None) -> None:
        async with aiohttp.ClientSession() as session:
            await session.delete(self.delete_url, data=dict(
                key=self.get_key(mem.uuid, old_file_extension or mem.file_extension),
            ))
