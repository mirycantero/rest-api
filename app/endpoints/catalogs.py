from flask import Blueprint
from flask_cors import CORS

from ..models import Industry, State, Gender, Project
from ..core import custom_response

catalogs = Blueprint('catalogs', __name__)
CORS(catalogs)


@catalogs.route('/industries', methods=['GET'])
def get_industries():
    """Fetches all the industries."""

    industries = Industry.get_industries()
    return custom_response(industries, 200)


@catalogs.route('/states', methods=['GET'])
def get_states():
    """Fetches all the states."""

    states = State.get_states()
    return custom_response(states, 200)


@catalogs.route('/genders', methods=['GET'])
def get_genders():
    """Fetches all the genders."""

    genders = Gender.get_genders()
    return custom_response(genders, 200)


@catalogs.route('/projects', methods=['GET'])
def get_projects():
    """Fetches all the projects."""

    projects = Project.get_projects()
    return custom_response(projects, 200)
