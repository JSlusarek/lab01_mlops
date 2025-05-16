# settings.py
from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import field_validator


class Settings(BaseSettings):
    ENVIRONMENT: str
    APP_NAME: str
    DB_PASSWORD: str  # <- nowy sekret!

    model_config = SettingsConfigDict(env_file=".env.dev", env_file_encoding="utf-8")

    @field_validator("ENVIRONMENT")
    @classmethod
    def validate_environment(cls, value):
        allowed = {"dev", "test", "prod"}
        if value not in allowed:
            raise ValueError(f"ENVIRONMENT must be one of {allowed}, got '{value}'")
        return value
