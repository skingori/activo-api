"""Module to validate resource id from url parameters"""

import re
from functools import wraps

from api.middlewares.base_validator import ValidationError


def is_valid_id(id):
    """Check if id is valid"""
    return re.match('^[-a-zA-Z0-9_]*$', id)


def validate_id(function):
    """Decorator function for views to validate id"""

    @wraps(function)
    def decorated_function(*args, **kwargs):
        if not is_valid_id(kwargs.get('id', None)):
            raise ValidationError({
                'status': 'error',
                'message': 'Invalid id in parameter'
            }, 400)
        return function(*args, **kwargs)
    return decorated_function
