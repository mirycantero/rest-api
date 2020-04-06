from flask import Flask

from .db import db
from .cereal import Cereal


def init_app(app: Flask):
    from sqlalchemy.engine.url import URL

    url = URL(
        drivername=app.config['DB_DRIVER'],
        username=app.config['DB_USER'],
        password=app.config['DB_PASSWORD'],
        host=app.config['DB_HOST'],
        port=app.config['DB_PORT'],
        database=app.config['DB_NAME'])

    # Override the original value with the generated URI
    app.config['SQLALCHEMY_DATABASE_URI'] = str(url)

    db.init_app(app)
