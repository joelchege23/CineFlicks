import os

from decouple import config

BASE_DIR=os.path.dirname(os.path.realpath(__file__))


class Config:
    SECRET_KEY=config("SECRET_KEY", 'secret')
    SQLALCHEMY_TRACK_MODIFICATIONS=False

class DevConfig(Config):
    DEBUG=config("DEBUG", cast=bool)
    SQLALCHEMY_ECHO=True
    SQLALCHEMY_DATABASE_URI='sqlite:///' + os.path.join(BASE_DIR, 'db.sqlite3')

class ProductionConfig(Config):
    DEBUG=config("DEBUG", cast=bool)


config_dict={
    'dev': DevConfig,
    'prod': ProductionConfig
}