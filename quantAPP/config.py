from os import environ, path
from dotenv import load_dotenv

basedir = path.dirname(__file__)
load_dotenv(path.join(basedir, '.env'))


class Config:
    """Base config."""
    SECRET_KEY = environ.get('SECRET_KEY')
    CPF = environ.get('CPF')
    KEY = environ.get('KEY')
    SESSION_COOKIE_NAME = environ.get('SESSION_COOKIE_NAME')
    STATIC_FOLDER = 'static'
    TEMPLATES_FOLDER = 'templates'

class DevConfig(Config):
    FLASK_ENV = 'development'
    DEBUG = True
    TESTING = True
    DATABASE_URI = environ.get('DEV_DATABASE_URI')


if __name__ == "__main__":
    config =Config()
    print(config.SECRET_KEY)
    
