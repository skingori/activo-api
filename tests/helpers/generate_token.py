"""Module for token generation"""

import jwt
from base64 import b64encode
from ..mocks.user import user_one
from os import getenv
from base64 import b64decode, encode
from datetime import datetime
from api.utilities.constants import UTF_8


def generate_token(exp=None):
    """
    Generates jwt tokens for testing purpose

    params:
        exp: Token Expiration. This could be datetime object or an integer
    result:
        token: This is the bearer token in this format 'Bearer token'
    """

    secret_key = getenv('JWT_SECRET_KEY')
    payload = {'userInfo': user_one.to_dict()}
    payload.__setitem__('exp', exp) if exp is not None else ''
    token = jwt.encode(payload, secret_key, algorithm='RS256').decode(UTF_8)
    return 'Bearer {0}'.format(token)