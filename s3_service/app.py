from typing import Annotated

from fastapi import FastAPI, File, Form

from config import BUCKET_NAME, DOWNLOAD_URL, s3

app = FastAPI()


@app.post("/upload")
async def create_file(file: Annotated[bytes, File()], key: Annotated[str, Form()]):
    s3.put_object(
        Body=file,
        Bucket=BUCKET_NAME,
        Key=key,
        ContentType='application/octet-stream',
    )
    return {'url': DOWNLOAD_URL + f'/{key}'}
