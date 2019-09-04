from app import env


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
        f'postgresql+psycopg2://{env.CLOUDSQL_USER}:{env.CLOUDSQL_PASSWORD}'
        f'@localhost:{env.CLOUDSQL_PORT}/{env.CLOUDSQL_DATABASE}'
    )
    DEBUG = True


class DevelopmentConfig(Config):
    """
    Development Configuration - default config
    """

    SQLALCHEMY_DATABASE_URI = (
        f'postgresql+psycopg2://{env.CLOUDSQL_USER}:{env.CLOUDSQL_PASSWORD}'
        f'@{env.CLOUDSQL_HOST}:{env.CLOUDSQL_PORT}/{env.CLOUDSQL_DATABASE}'
        f'?host=/cloudsql/{env.CLOUDSQL_CONNECTION_NAME}'
    )
    DEBUG = True


class ProductionConfig(Config):
    """
    Production Configuration
    """

    SQLALCHEMY_DATABASE_URI = env.SQLALCHEMY_DATABASE_URI
    DEBUG = False


# way to map the value of `FLASK_ENV` to a configuration
config = {
    "local": LocalConfig,
    "dev": DevelopmentConfig,
    "prod": ProductionConfig
}
