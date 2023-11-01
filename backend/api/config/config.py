import os

from decouple import config


class Config:
    SECRET_KEY=config("SECRET_KEY", 'secret')


class DevConfig(Config):
    DEBUG=config("DEBUG", cast=bool)


class ProductionConfig(Config):
    DEBUG=config("DEBUG", cast=bool)


config_dict={
    'dev': DevConfig,
    'prod': ProductionConfig
}