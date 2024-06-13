from os import getenv

from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = getenv('DATABASE_URL')
S3_API_URL = getenv('S3_API_URL')
