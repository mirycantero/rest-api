import os

from .config import config
from .core import handle_error
from flask import Flask
from flask_marshmallow import Marshmallow
from werkzeug.exceptions import default_exceptions


def create_app(test_config=None):
    app = Flask(__name__)

    # check environment variables to see which config to load
    env = os.environ.get("FLASK_ENV", "dev")
    app.config.from_object(config[env])  # config dict is from app/config.py

    # If set to True SQLAlchemy will log all the statements issued to stderr
    # which can be useful for debugging.
    app.config["SQLALCHEMY_ECHO"] = False

    # register sqlalchemy to this app
    from .models import db

    db.init_app(app)  # initialize Flask SQLALchemy with this flask app
    Marshmallow(app)

    # import and register blueprints http://flask.pocoo.org/docs/1.0/blueprints/
    # from .endpoints.accounts import accounts
    # app.register_blueprint(accounts)

    # register error Handlers
    for exc in default_exceptions:
        app.register_error_handler(exc, handle_error)

    return app
