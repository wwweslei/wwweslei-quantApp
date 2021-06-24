import os
from os import environ, path
from dotenv import load_dotenv

basedir = path.dirname(__file__)
basePath = path.dirname(basedir)
load_dotenv(path.join(basedir, ".env"))


class Config:
    """Base config."""

    SECRET_KEY = environ.get("SECRET_KEY")
    CPF = environ.get("CPF")
    KEY = environ.get("KEY")
    SESSION_COOKIE_NAME = environ.get("SESSION_COOKIE_NAME")
    DEBUG = True
    STATIC_FOLDER = "static"
    TEMPLATES_FOLDER = "templates"
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basePath, "banco.db")
    # FLASK_APP = environ.get('FLASK_APP')
    # FLASK_ENV = environ.get('FLASK_ENV')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False


class ProdConfig(Config):
    FLASK_ENV = "production"
    DEBUG = False
    TESTING = False
    DATABASE_URI = environ.get("PROD_DATABASE_URI")


class DevConfig(Config):
    FLASK_ENV = "development"
    DEBUG = True
    TESTING = True
    DATABASE_URI = environ.get("DEV_DATABASE_URI")


if __name__ == "__main__":
    config = Config()
    print(config.SECRET_KEY)
