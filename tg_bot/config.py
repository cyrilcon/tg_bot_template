import logging

from pathlib import Path
from pydantic import BaseModel, Field
from pydantic_settings import BaseSettings, SettingsConfigDict

BASE_DIR = Path(__file__).resolve().parent.parent


class TgBotConfig(BaseModel):
    token: str
    admin_ids: list[int] | None = None


class RedisConfig(BaseModel):
    host: str = "localhost"
    port: int = 6379
    password: str | None = None
    database: int = 0

    def dsn(self) -> str:
        if self.password:
            return f"redis://:{self.password}@{self.host}:{self.port}/{self.database}"
        return f"redis://{self.host}:{self.port}/{self.database}"


class Config(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=(BASE_DIR / ".env.template", BASE_DIR / ".env"),
        case_sensitive=False,
        env_nested_delimiter="__",
        extra="ignore",
    )

    tg_bot: TgBotConfig = Field(default_factory=TgBotConfig)
    redis: RedisConfig = Field(default_factory=RedisConfig)

    logging_level: int = logging.INFO


config = Config()
