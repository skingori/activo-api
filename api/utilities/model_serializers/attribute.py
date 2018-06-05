from marshmallow import fields, post_load, validate

from .base_schemas import BaseSchema
from .validators.validators import string_length_60_validator
from ..messages.error_messages import serialization_errors
from api.models.attribute import Attribute


class AttributeSchema(BaseSchema):
    """Attribute model schema"""

    label = fields.String(required=True,
                          validate=string_length_60_validator,
                          error_messages={
                              'required':
                              serialization_errors['field_required']})
    is_required = fields.Boolean(required=True,
                                 error_messages={
                                     'required':
                                     serialization_errors['field_required']})
    input_control = fields.String(required=True,
                                  validate=string_length_60_validator,
                                  error_messages={
                                      'required':
                                      serialization_errors['field_required']})
    choices = fields.String(required=True,
                            validate=validate.Length(
                                max=250,
                                error=serialization_errors[
                                    'string_length'].format('250')),
                            error_messages={
                                'required':
                                serialization_errors['field_required']})

    @post_load
    def create_attribute(self, data):
        """Return attribute object after successful loading into schema"""

        return Attribute(**data)
