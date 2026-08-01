from pydantic_settings import BaseSettings,SettingsConfigDict


class Settings(BaseSettings):

    APP_NAME:str="student App"
    DATABASE:str="sqlite:///student.db"

    model_config=SettingsConfigDict(
        env_file=".env"
    )

settings=Settings()
