from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    APP_NAME: str
    DATABASE_URL: str
    OLLAMA_URL: str
    MODEL_NAME: str

    class Config:
        env_file = ".env"

settings = Settings()