""" Module for marshmallow validators. """
import re
from marshmallow import ValidationError

from ..models.user import User

# regex expressions to be used by validators
email_regex = re.compile(
    r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
name_regex = re.compile(r"^[a-zA-Z]+(([' .-][a-zA-Z ])?[a-zA-Z]*)*$")


def email_syntax_validator(data):
    """
    Checks if given email is at least 6 chars, correct email syntax &
    raises a ValidationError otherwise
    """

    if len(data) > 5:
        if not re.match(email_regex, data):
            raise ValidationError(f'{data} is not a valid email address')
    else:
        raise ValidationError('Email address must be 6 characters or more')


def email_exists_validator(data):
    """
    Checks if given email is at least 6 chars, correct email syntax & not
    regisered already. Raises a ValidationError otherwise
    """

    if len(data) > 5:
        if not re.match(email_regex, data):
            raise ValidationError(f'{data} is not a valid email address')
        else:
            if User.query.filter_by(email=data).first():
                raise ValidationError(f'{data} is already registered')
    else:
        raise ValidationError('Email address must be 6 characters or more')


def name_validator(data):
    """
    Checks if given name is at least 1 character and only contains letters,
    numbers and non consecutive fullstops, hyphens, spaces and apostrophies.
    """
    if not len(data) > 0:
        raise ValidationError('Name is required')
    else:
        if not re.match(name_regex, data):
            raise ValidationError(
                'Name must start and end with a letter, only contain letters, non-consecutive fullstops, hyphens, spaces and apostrophies') #noqa
