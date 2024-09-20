from typing import Any

from pydantic import ConfigDict, field_validator, EmailStr
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DB_URL: str = "postgresql+asyncpg://postgres:1234567890@localhost:5432/lesson11"
    SECRET_KEY_JWT: str = "1234567890"
    ALGORITHM: str = "HS256"
    MAIL_USERNAME: EmailStr = "postgres@meail.com"
    MAIL_PASSWORD: str = "postgres"
    MAIL_FROM: str = "postgres@meail.com"
    MAIL_PORT: int = 567234
    MAIL_SERVER: str = "postgres"
    REDIS_DOMAIN: str = "localhost"
    REDIS_PORT: int = 6379
    REDIS_PASSWORD: str | None = None
    CLOUDINARY_NANE: str = "dkmre6kv0"
    CLOUDINARY_API_KEY: int = 818979165894816
    CLOUDINARY_API_SECRET: str = "secret"

    @field_validator("ALGORITHM")
    @classmethod
    def validate_algorithm(cls, v: Any):
        if v not in ["HS256", "H512"]:
            raise ValueError("wrong algorithm")
        return v

    model_config = ConfigDict(
        extra="ignore", env_file=".env", env_file_encoding="utf-8"
    )  # noqa



config = Settings()


"""
class Config:
    DB_URL = "postgresql+asyncpg://postgres:1234567890@localhost:5432/lesson11"

    # driver://user:pass@localhost/dbname
    # asyncpg- пишемо, якщо працюємо з асинхронно,postgres - КОРИСТУВАЧ, ТАК І ПИШЕМО ПОСТГРЕС,
    # 1234567890- пароль до постгрес, localhost:5432- звязок, числа 5432 вказані в докері, lesson11- назва бази даних
"""
