from flask import Blueprint
from flask_cors import CORS

from app.core import custom_response

health = Blueprint('health', __name__)
CORS(health)


def gather_database_info() -> dict:
    from app.models import db

    return {
        'dialect': db.engine.dialect.name,
    }


def gather_python_info() -> dict:
    import sys

    return {
        'version': sys.version,
    }


def gather_global_info() -> dict:
    return {
        'database': gather_database_info(),
        'python': gather_python_info(),
    }


@health.route('/', methods=['GET'])
def get_root_status():
    return custom_response({'status': 'ok'}, 200)


@health.route('/health/status', methods=['GET'])
def get_status():
    return custom_response({'status': 'ok'}, 200)


@health.route('/health/info', methods=['GET'])
def get_info():
    return custom_response(gather_global_info(), 200)
