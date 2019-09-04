"""
Use this file only for loading and documenting all the required environment
    variables across the app.
"""

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
