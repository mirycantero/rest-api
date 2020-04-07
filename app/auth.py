import requests

from flask import request, Flask, current_app, _app_ctx_stack
from functools import wraps
from jose import jwt
from werkzeug.exceptions import Unauthorized

app: Flask = current_app
AUTH0_DOMAIN = app.config['AUTH0_DOMAIN']
AUTH0_API_AUDIENCE = app.config['AUTH0_API_AUDIENCE']
ALGORITHM = 'RS256'


def get_authorization_token():
    """Obtains the access token from the Authorization Header
    """
    auth = request.headers.get('Authorization')
    if not auth:
        raise Unauthorized(description='Authorization header is expected')

    parts = auth.split()

    if len(parts) <= 1:
        raise Unauthorized(
            description='Token not found')

    elif parts[0].lower() != 'bearer':
        raise Unauthorized(
            description='Authorization header must start with Bearer')

    elif len(parts) > 2:
        raise Unauthorized(
            description='Authorization header must be Bearer token')

    token = parts[1]
    return token


def requires_auth(f):
    """Determines if the access token is valid
    """
    @wraps(f)
    def decorated(*args, **kwargs):
        token = get_authorization_token()
        jsonurl = requests.get(f'https://{AUTH0_DOMAIN}/.well-known/jwks.json')
        jwks = jsonurl.json()

        unverified_header = jwt.get_unverified_header(token)
        rsa_key = {}
        for key in jwks["keys"]:
            if key['kid'] == unverified_header['kid']:
                rsa_key = {
                    'kty': key['kty'],
                    'kid': key['kid'],
                    'use': key['use'],
                    'n': key['n'],
                    'e': key['e']
                }
        if rsa_key:
            try:
                payload = jwt.decode(
                    token,
                    rsa_key,
                    algorithms=[ALGORITHM],
                    audience=AUTH0_API_AUDIENCE,
                    issuer=f'https://{AUTH0_DOMAIN}/'
                )
            except jwt.ExpiredSignatureError:
                raise Unauthorized(description='Token is expired')
            except jwt.JWTClaimsError:
                raise Unauthorized(
                    description='Incorrect claims, '
                    'please check the audience and issuer')
            except Exception:
                raise Unauthorized(
                    description='Unable to decode authentication token')

            _app_ctx_stack.top.current_user = payload
            return f(*args, **kwargs)
        raise Unauthorized(description='Unable to find appropriate key')
    return decorated
