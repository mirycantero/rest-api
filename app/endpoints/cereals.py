from flask import Blueprint, request
from flask_cors import CORS
from werkzeug.exceptions import BadRequest

from app.models import Cereal
from app.schemas import CerealSchema
from app.core import custom_response
from app.auth import requires_auth


cereals = Blueprint('cereals', __name__)
CORS(cereals)

create_cereal_schema = CerealSchema()
update_cereal_schema = CerealSchema(exclude=('name',))


@cereals.route('/cereals', methods=['GET'])
@requires_auth
def get_cereals():
    cereals = Cereal.get_cereals()
    return custom_response(cereals, 200)


@cereals.route('/cereals/<string:name>', methods=['GET'])
@requires_auth
def get_cereal(name):
    cereal = Cereal.get_cereal(name)
    return custom_response(cereal, 200)


@cereals.route('/cereals', methods=['POST'])
@requires_auth
def post_cereal():
    cereal_payload = request.json

    errors = create_cereal_schema.validate(cereal_payload)
    if errors:
        raise BadRequest(str(errors))

    cereal = Cereal.post_cereal(cereal_payload)
    return custom_response(cereal, 201)


@cereals.route('/cereals/<string:name>', methods=['PUT'])
@requires_auth
def put_cereal(name):
    cereal_payload = request.json

    errors = update_cereal_schema.validate(cereal_payload)
    if errors:
        raise BadRequest(str(errors))

    cereal = Cereal.put_cereal(name, cereal_payload)
    return custom_response(cereal, 204)


@cereals.route('/cereals/<string:name>', methods=['DELETE'])
@requires_auth
def delete_cereal(name):
    cereal = Cereal.delete_cereal(name)
    return custom_response(cereal, 204)
