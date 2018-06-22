"""Module to validate resource id from url parameters"""

import re


def validate_id(id):
    """Validate id string"""
    return re.match('^[-a-zA-Z0-9_]*$', id)
