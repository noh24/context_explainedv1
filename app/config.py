from pydantic_settings import BaseSettings
from dotenv import load_dotenv

load_dotenv()

class Settings(BaseSettings):
    OPENAI_API_KEY: str
    DATABASE_URL: str
    MODEL_NAME: str 
    TIMEZONE: str 
    MAX_VERSES: int = 8
    LESSON_PROMPT: str
    LOCAL_DB_URL: str

    class Config:
        env_file = ".env"
    
settings = Settings()