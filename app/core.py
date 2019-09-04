from enum import Enum
from flask import json, Response
from werkzeug.exceptions import HTTPException


class CustomEncoder(json.JSONEncoder):
    def default(self, o):
        # encode enums values by its name
        if isinstance(o, Enum):
            return o.name

        # encode custom classes by using to_json method
        to_json_fn = getattr(o, 'to_json', None)
        if callable(to_json_fn):
            return to_json_fn()

        return json.JSONEncoder.default(self, o)


def custom_response(res, status_code, mimetype="application/json"):
    """
    Custom Response Function
    """
    return Response(
        mimetype=mimetype,
        response=json.dumps(res, cls=CustomEncoder),
        status=status_code
    )


# add specific Exception handlers before this, if needed
# More info at http://flask.pocoo.org/docs/1.0/patterns/apierrors/
def handle_error(Exception):
    """Catches and handles all exceptions, add more specific error Handlers.
    :param Exception
    """
    status_code = 500
    message = "Internal Server Error"
    if isinstance(Exception, HTTPException):
        status_code = Exception.code
        message = str(Exception)
    return custom_response({"message": message}, status_code)
