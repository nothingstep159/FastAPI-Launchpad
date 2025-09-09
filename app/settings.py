from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = "sqlite:///./app.db"
    SECRET_KEY: str = "CHANGE_ME_IN_ENV"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()
