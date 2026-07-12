import os
from dotenv import load_dotenv

# Load Environment Variables
load_dotenv()


class Config:
    """
    Base Configuration
    Used by all environments.
    """

    # Security
    SECRET_KEY = os.getenv("SECRET_KEY")

    # Database
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Upload Settings
    UPLOAD_FOLDER = "app/static/uploads"
    MAX_CONTENT_LENGTH = 100 * 1024 * 1024  # 100 MB

    # Session
    SESSION_PERMANENT = False

    # Cookie Security
    SESSION_COOKIE_HTTPONLY = True
    REMEMBER_COOKIE_HTTPONLY = True

    # Media
    CAMERA_WIDTH = 640
    CAMERA_HEIGHT = 480

    # SmartProctor
    PROJECT_NAME = "SmartProctor"
    PROJECT_VERSION = "1.0.0"