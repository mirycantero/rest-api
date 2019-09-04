from flask import Blueprint
from flask_cors import CORS

from ..models import Employee
from ..core import custom_response

employees = Blueprint('employees', __name__)
CORS(employees)


@employees.route('/employees', methods=['GET'])
def get_employees():
    """Fetches all the employees."""

    employees = Employee.get_employees()
    return custom_response(employees, 200)
