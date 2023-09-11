"""
Copyright (c) 2023 - present imitor.com
"""
import os
from datetime import timedelta

from dotenv import find_dotenv, load_dotenv

from stage_one.utils.utils import cache_constants

load_dotenv(find_dotenv())


class Config(object):
    """App config object"""

    DEBUG = False
    # Set up the App SECRET_KEY
    SECRET_KEY = os.getenv("SECRET_KEY", cache_constants.secret_key)
    # Bad idea, whenever app reloads, it logs out all users
    # JWT_SECRET_KEY = cache_constants.secret_key
    JWT_SECRET_KEY = SECRET_KEY
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(
        seconds=int(os.getenv("ACCESS_TOKEN_EXPIRES"))
    )  # access tokens expiration
    JWT_TOKEN_LOCATION = ["headers", "cookies"]
    # suppress sqlalchemy modification errors
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    LANGUAGES = ["en", "fr", "es"]
    # print(SECRET_KEY)
    # Mailing credentials
    MAIL_SERVER = os.getenv("MAIL_SERVER")
    MAIL_PORT = int(os.getenv("MAIL_PORT"))
    MAIL_USERNAME = os.getenv("MAIL_USERNAME")
    MAIL_PASSWORD = os.getenv("MAIL_PASSWORD")
    MAIL_USE_TLS = False
    MAIL_USE_SSL = os.getenv("MAIL_USE_SSL")
    MAIL_DEBUG = False


class ProductionConfig(Config):
    """Production Config object"""

    SQLALCHEMY_DATABASE_URI = os.getenv("DB_URI")


class DevelopmentConfig(Config):
    """Development Config object"""

    DEBUG = True
    sql_lite = "sqlite:///development.db"
    SQLALCHEMY_DATABASE_URI = os.getenv("DB_URI", default=sql_lite)


class TestingConfig(Config):
    """Testing Config object"""

    DEBUG = True
    sql_lite = "sqlite:///test.db"
    SQLALCHEMY_DATABASE_URI = sql_lite


configs = {
    "development": DevelopmentConfig,
    "production": ProductionConfig,
    "testing": TestingConfig,
}
