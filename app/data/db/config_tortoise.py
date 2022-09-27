from __future__ import annotations

from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise


def register_db(fastapi_app: FastAPI) -> None:
    register_tortoise(
        app=fastapi_app,
        db_url='sqlite://app/data/db/db.sqlite3',
        modules={'models': ['app.data.models.models']},
        generate_schemas=True,
        add_exception_handlers=True,
    )
