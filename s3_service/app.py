from typing import Annotated

from fastapi import FastAPI, File, Form

from config import BUCKET_NAME, DOWNLOAD_URL, s3

app = FastAPI()


@app.get('/')
async def ping():
    return 'ok'


@app.post('/upload')
async def upload_file(file: Annotated[bytes, File()], key: Annotated[str, Form()]) -> dict:
    s3.put_object(
        Body=file,
        Bucket=BUCKET_NAME,
        Key=key,
        ContentType='application/octet-stream',
    )
    return {'url': DOWNLOAD_URL + f'/{key}'}


@app.delete('/delete')
async def delete_file(key: Annotated[str, Form()]) -> dict:
    s3.delete_object(
        Bucket=BUCKET_NAME,
        Key=key,
    )
    return {'status': 'ok'}
