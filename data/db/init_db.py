import os

from fastapi import FastAPI
from tortoise import Tortoise
from tortoise.contrib.test import initializer
from tortoise.contrib.fastapi import register_tortoise
import toml

from __future__ import annotations
from pathlib import Path
from typing import Any

from pydantic import (
    AnyHttpUrl,
    BaseSettings,
    EmailStr,
    HttpUrl,
    PostgresDsn,
    RedisDsn,
    validator,
)

class Paths:
    #ToDo: check if root dir es ok
    ROOT_DIR: Path = Path(__file__).parent.parent.parent
    BASE_DIR: Path = ROOT_DIR / "app"
    TEMPLATES_DIR: Path = ROOT_DIR / "templates"
    STATIC_FILES_DIR: Path = ROOT_DIR / "static"
    EMAIL_TEMPLATES_DIR: Path = ROOT_DIR / "emails"
    LOGIN_PATH: Path = ROOT_DIR / "auth/login"

class Settings(BaseSettings):
    @property
    def PATHS(self) -> Paths:
        return Paths()

    SECRET_KEY: str
    DEBUG: bool = False
    AUTH_TOKEN_LIFETIME_SECONDS = 3600
    SERVER_HOST: AnyHttpUrl = "http://localhost:8000"
    SENTRY_DSN: HttpUrl | None = None
    PAGINATION_PER_PAGE: int = 20

    REDIS_URL: RedisDsn

settings = Settings()



TORTOISE_ORM = {
    "connections": {
        "default": settings.DATABASE_URI
    },
    "apps": {
        "models": {
            "models": ["app.users.models", "aerich.models"],
            "default_connection": "default",
        },
    },
}

def register_db(app: FastAPI) -> None:
    register_tortoise(
        app,
        config=TORTOISE_ORM,
        generate_schemas=False,
        add_exception_handlers=True,
    )

