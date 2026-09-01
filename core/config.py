from pydantic_settings import BaseSettings,SettingsConfigDict
import os

class Settings(BaseSettings):

    APP_NAME:str="student App"
    DATABASE_URL: str  # Pydantic automatically reads DATABASE_URL from .env or system env

    model_config=SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore"  # Prevents errors if extra variables exist in .env
    )

settings=Settings()
