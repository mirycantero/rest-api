from flask import Blueprint, request
from flask_cors import CORS

from ..models import Cereal
from ..core import custom_response


cereals = Blueprint('cereals', __name__)
CORS(cereals)


@cereals.route('/cereals', methods=['GET'])
def get_cereals():
    cereals = Cereal.get_cereals()
    return custom_response(cereals, 200)


@cereals.route('/cereals/<string:name>', methods=['GET'])
def get_cereal(name):
    cereal = Cereal.get_cereal(name)
    return custom_response(cereal, 200)


@cereals.route('/cereals', methods=['POST'])
def post_cereal():
    cereal_payload = request.json

    cereal = Cereal.post_cereal(cereal_payload)
    return custom_response(cereal, 200)


@cereals.route('/cereals/<string:name>', methods=['PUT'])
def put_cereal(name):
    cereal_payload = request.json

    cereal = Cereal.put_cereal(name, cereal_payload)
    return custom_response(cereal, 200)


@cereals.route('/cereals/<string:name>', methods=['DELETE'])
def delete_cereal(name):
    cereal = Cereal.delete_cereal(name)
    return custom_response(cereal, 200)
