from os import getenv

from dotenv import load_dotenv

load_dotenv()

BUCKET_NAME = getenv('BUCKET_NAME')
ACCESS_KEY = getenv('ACCESS_KEY')
SECRET_KEY = getenv('SECRET_KEY')
DOWNLOAD_URL = getenv('DOWNLOAD_URL')
