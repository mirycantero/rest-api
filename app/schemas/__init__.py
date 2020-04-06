from flask import Flask
from flask_marshmallow import Marshmallow

from .schemas import CerealSchema


def init_app(app: Flask):
    Marshmallow(app)
