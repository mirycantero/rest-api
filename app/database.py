import os
from flask import Flask

from app.models import db


def _initialize_data():
    # Get data dir relative to this file
    script_path = os.path.abspath(os.path.join(
        __file__, '../../tools/db_data/cereal.csv'))

    with open(script_path, 'r') as f:
        con = db.engine.raw_connection()
        cur = con.cursor()
        next(f)  # Skip the header row
        cur.copy_from(f, 'cereal', sep=',')
        con.commit()


def init_app(app: Flask):
    if app.config.get('INITIALIZE_DATA'):
        _initialize_data()
