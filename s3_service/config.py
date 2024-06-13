from os import getenv

import boto3
from dotenv import load_dotenv

load_dotenv()

BUCKET_NAME = getenv('BUCKET_NAME')
ACCESS_KEY = getenv('ACCESS_KEY')
SECRET_KEY = getenv('SECRET_KEY')
DOWNLOAD_URL = getenv('DOWNLOAD_URL')
ENDPOINT_URL = getenv('ENDPOINT_URL')
REGION_NAME = getenv('REGION_NAME')

s3 = boto3.client(
    's3',
    endpoint_url=ENDPOINT_URL,
    region_name=REGION_NAME,
    aws_access_key_id=ACCESS_KEY,
    aws_secret_access_key=SECRET_KEY,
)
