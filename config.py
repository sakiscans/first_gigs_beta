import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, ".env"))

class Config: 
    SECRET_KEY = os.environ.get("SECRET_KEY", "dev-only-change-me")
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL") or (
        "sqlite://" + os.path.join(basedir, "firstgigs.db")
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False 

class DevelopmentConfig(Config):
    DEBUG = True 


class TestingConfig(Config): 
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite://:memory:"

    WTF_CSRF_ENABLED = False # Disable CSRF protection for testing


class ProductionConfig(Config): 
    DEBUG = False
    SECRET_KEY = os.environ.get("SECRET_KEY")


config = {
    "development": DevelopmentConfig, 
    "testing": TestingConfig, 
    "production": ProductionConfig, 
}
