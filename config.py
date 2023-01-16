from datetime import timedelta
import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))

load_dotenv(os.path.join(basedir, ".env"))


class Config(object):
    SECRET_KEY = os.getenv("SECRET_KEY")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    REMEMBER_COOKIE_DURATION = timedelta(seconds=10)


class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = "sqlite:////" + os.path.join(
        basedir, "jwt_generator_api.db"
    )
