from flask import Flask
from os import environ

APP_NAME = 'rest-api'


def create_app(instance_name):
    app = Flask(APP_NAME, instance_relative_config=True)

    # app.config.from_json(f'{instance_name}.json', silent=True)
    app.config.from_json('local.json', silent=True)
    app.config.from_mapping(environ)

    app.config['FLASK_ENV'] = instance_name

    with app.app_context():
        from app import models
        from app import endpoints
        from app import schemas
        from app import migrations
        from app import database

        models.init_app(app)
        endpoints.init_app(app)
        schemas.init_app(app)
        migrations.init_app(app)
        database.init_app(app)

        return app
