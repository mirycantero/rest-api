import os

from .config import config
from .core import handle_error
from flask import Flask
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from werkzeug.exceptions import default_exceptions


def create_app(test_config=None):
    app = Flask(__name__)

    env = os.environ.get("FLASK_ENV", "dev")
    app.config.from_object(config[env])

    app.config["SQLALCHEMY_ECHO"] = False

    from .models import db

    db.init_app(app)  # initialize Flask SQLALchemy with this flask app
    Marshmallow(app)
    Migrate(app, db)

    from .endpoints.cereals import cereals
    app.register_blueprint(cereals)

    for exc in default_exceptions:
        app.register_error_handler(exc, handle_error)

    return app
