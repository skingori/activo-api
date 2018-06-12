"""Module for token validation"""

from flask import request
from os import getenv as env
from base64 import b64decode
import jwt
from functools import wraps
from api.utilities.constants import (
    NO_BEARER_MSG, NO_TOKEN_MSG,
    SERVER_ERROR_MESSAGE,
    SIGNATURE_ERROR, EXPIRED_TOKEN_MSG,
    INVALID_TOKEN_MSG
)


def token_required(function):
    """Authentication decorator. Validates token from the client"""

    @wraps(function)
    def decorated_function(*args, **kwargs):
        token = request.headers.get('Authorization')
        from .base_validator import ValidationError

        if not token:
            raise ValidationError(NO_TOKEN_MSG)

        elif 'bearer' not in token.lower():
            raise ValidationError(NO_BEARER_MSG)

        try:
            token = token.split(' ')[1]
            if(env('FLASK_ENV') == 'testing'):
                public_key = env('JWT_PUBLIC_KEY_TEST')
            else:
                public_key64 = env('JWT_PUBLIC_KEY')
                public_key = b64decode(public_key64).decode('utf-8')
            decoded_token = jwt.decode(
                token,
                public_key,
                algorithms=['RS256'],
                options={
                    'verify_signature': True,
                    'verify_exp': True
                }
            )
        except ValueError:
            raise ValidationError(SERVER_ERROR_MESSAGE, 500)

        except TypeError:
            raise ValidationError(SERVER_ERROR_MESSAGE, 500)

        except jwt.ExpiredSignatureError:
            raise ValidationError(EXPIRED_TOKEN_MSG)

        except jwt.DecodeError as error:
            if str(error) == 'Signature verification failed':
                raise ValidationError(SIGNATURE_ERROR, 500)

            else:
                raise ValidationError(INVALID_TOKEN_MSG, 401)

        # setting the payload to the request object and can be accessed with \
        # request.decoded_token from the view
        setattr(request, 'decoded_token', decoded_token)
        return function(*args, **kwargs)

    return decorated_function
