import os
from tortoise import Tortoise
from dotenv import load_dotenv

load_dotenv()

async def init():

    await Tortoise.init(
        db_url=f'{DB_TYPE}://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}',
        modules={'models':['app.models']}
    )

    await