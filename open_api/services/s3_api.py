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
    def get_key(mem: Mem) -> str:
        return mem.uuid + '.' + mem.file_extension

    async def create(self, db: DB, mem: Mem, file: UploadFile) -> None:
        # TODO check status code
        async with aiohttp.ClientSession() as session:
            resp = await session.post(self.url + '/upload', data=dict(
                file=await file.read(),
                key=self.get_key(mem),
            ))
            json = await resp.json()
            await db.mem.update(mem, url=json['url'])
