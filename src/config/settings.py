from pydantic_settings import BaseSettings
from dotenv import load_dotenv


class Settings(BaseSettings):
    ENV: str = "development"
    DATABASE_URL: str = "sqlite:///./test.db"
    DB_NAME: str
    DB_USER: str
    DB_PASSWORD: str
    DB_HOST: str
    DB_PORT: str

    class Config:
        env_file = ".env"


settings = Settings()
