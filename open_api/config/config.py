from os import getenv

from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = getenv('DATABASE_URL')
