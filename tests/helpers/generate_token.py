"""Module for token validation"""

import jwt
from os import getenv as env
from base64 import b64encode
from ..mocks.user import user_one
from os import getenv
from base64 import b64decode, encode
from datetime import datetime


def generate_token():
    secret_key = getenv('JWT_SECRET_KEY')
    payload = {'userInfo': user_one.to_dict()}
    token = jwt.encode(payload, secret_key, algorithm='RS256').decode('utf-8')
    return 'Bearer {0}'.format(token)
