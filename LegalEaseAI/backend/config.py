import os
from dotenv import load_dotenv

load_dotenv()


class Settings:
    APP_NAME: str = os.getenv("APP_NAME", "LegalEase")
    APP_VERSION: str = os.getenv("APP_VERSION", "1.0.0")

    GEMINI_API_KEY: str = os.getenv("GEMINI_API_KEY", "")


settings = Settings()