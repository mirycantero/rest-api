from flask import Flask

from app.endpoints.cereals import cereals
from app.endpoints.health import health


def init_app(app: Flask):
    app.register_blueprint(cereals)
    app.register_blueprint(health)
