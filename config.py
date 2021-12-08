from starlette.config import Config

config = Config(".env")

DATABASE = config("DATABASE")
USER = config("USER")
PASSWORD = config("PASSWORD")
TOKEN = config("TOKEN")
