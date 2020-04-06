from flask import Flask

from app.endpoints.cereals import cereals


def init_app(app: Flask):
    app.register_blueprint(cereals)
