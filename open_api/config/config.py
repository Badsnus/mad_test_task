from os import getenv

from dotenv import load_dotenv

from services import S3Api

load_dotenv()

DATABASE_URL = getenv('DATABASE_URL')
s3_api = S3Api(getenv('S3_API_URL'))
