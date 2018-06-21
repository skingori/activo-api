import re


def valid_id(id):
    return re.match('-[a-zA-Z0-9]', id)
