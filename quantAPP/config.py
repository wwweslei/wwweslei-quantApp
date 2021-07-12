import os
from os import environ, path
from dotenv import load_dotenv

basedir = path.dirname(__file__)
basePath = path.dirname(basedir)
load_dotenv(path.join(basedir, ".env"))


class Config:
    """Base config."""

    SECRET_KEY = environ.get("SECRET_KEY")
    API_KEY = environ.get("API_KEY")
    url = "https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&interval=1min&apikey=EL5PEVKNPNABAHJB&symbol="
    url_day = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&interval=1min&apikey=EL5PEVKNPNABAHJB&symbol="
    CPF = environ.get("CPF")
    KEY = environ.get("KEY")
    SESSION_COOKIE_NAME = environ.get("SESSION_COOKIE_NAME")
    STATIC_FOLDER = "static"
    TEMPLATES_FOLDER = "templates"
    TEMPLATES_AUTO_RELOAD = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basePath, "banco.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False
    DEBUG_TB_INTERCEPT_REDIRECTS = False
    FLASK_ADMIN_SWATCH = "cerulean"
    ENV = 'development'


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
    print(config.SQLALCHEMY_DATABASE_URI)
