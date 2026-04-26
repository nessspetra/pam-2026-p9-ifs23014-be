import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    APP_PORT = os.getenv("APP_PORT", 5000)
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY") # Tambahkan ini
    SQLALCHEMY_DATABASE_URI = "sqlite:///db/data.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "super-secret")
    ADMIN_USERNAME = os.getenv("ADMIN_USERNAME", "admin")
    ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD", "admin123")