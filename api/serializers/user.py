""" Module with user model schemas. """
from marshmallow import (ValidationError, fields, post_load, validates)

from ..models.user import User
from .base_schemas import BaseSchema
from .validators import email_exists_validator, name_validator


class UserSchema(BaseSchema):
    """ User model schema. """

    name = fields.String(required=True,
                         validate=name_validator,
                         error_messages={'required': 'Name is required'})
    email = fields.String(required=True,
                          validate=email_exists_validator,
                          error_messages={'required': 'Email is required'})
    image_url = fields.String()

    @post_load
    def create_user(self, data):
        """ Return user object after successful loading of data"""
        return User().create_user(**data)
