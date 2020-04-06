from flask_migrate import Migrate
from flask import Flask

from app.models import db


def init_app(app: Flask):
    Migrate(app, db)
