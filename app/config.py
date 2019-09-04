import os
from dotenv import load_dotenv
load_dotenv()

# Flask config #

FLASK_ENV = os.environ.get('FLASK_ENV')

# CloudSQL config #

CLOUDSQL_USER = os.environ.get("CLOUDSQL_USER")
CLOUDSQL_PASSWORD = os.environ.get("CLOUDSQL_PASSWORD")
CLOUDSQL_DATABASE = os.environ.get("CLOUDSQL_DATABASE")
CLOUDSQL_HOST = os.environ.get("CLOUDSQL_HOST")
CLOUDSQL_PORT = os.environ.get("CLOUDSQL_PORT")
CLOUDSQL_CONNECTION_NAME = os.environ.get("CLOUDSQL_CONNECTION_NAME")

SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI")


# more configuration options here http://flask.pocoo.org/docs/1.0/config/
class Config:
    """
    Base Configuration
    """

    SQLALCHEMY_TRACK_MODIFICATIONS = False


class LocalConfig(Config):
    """
    Local development Configuration
    """

    SQLALCHEMY_DATABASE_URI = (
        f'postgresql+psycopg2://{CLOUDSQL_USER}:{CLOUDSQL_PASSWORD}'
        f'@localhost:{CLOUDSQL_PORT}/{CLOUDSQL_DATABASE}'
    )
    DEBUG = True


class DevelopmentConfig(Config):
    """
    Development Configuration - default config
    """

    SQLALCHEMY_DATABASE_URI = (
        f'postgresql+psycopg2://{CLOUDSQL_USER}:{CLOUDSQL_PASSWORD}'
        f'@{CLOUDSQL_HOST}:{CLOUDSQL_PORT}/{CLOUDSQL_DATABASE}'
        f'?host=/cloudsql/{CLOUDSQL_CONNECTION_NAME}'
    )
    DEBUG = True


class ProductionConfig(Config):
    """
    Production Configuration
    """

    SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI
    DEBUG = False


# way to map the value of `FLASK_ENV` to a configuration
config = {
    "local": LocalConfig,
    "dev": DevelopmentConfig,
    "prod": ProductionConfig
}
