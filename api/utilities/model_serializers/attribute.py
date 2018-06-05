from marshmallow import fields, post_load, validate

from .base_schemas import BaseSchema
from api.models.attribute import Attribute


class AttributeSchema(BaseSchema):
    """Attribute model schema"""

    label = fields.String(required=True,
                          validate=validate.Length(
                              max=60, error='Value cannot be greater than 60 characters'),
                          error_messages={'required': 'This field is required'})
    is_required = fields.Boolean(required=True)
    input_control = fields.String(required=True,
                                  validate=validate.Length(
                                      max=60, error='Value cannot be greater than 60 characters'),
                                  error_messages={'required': 'This field is required'})
    choices = fields.String(required=True,
                            validate=validate.Length(
                                max=250, error='Value cannot be greater than 250 characters'),
                            error_messages={'required': 'This field is required'})

    @post_load
    def create_attribute(self, data):
        """Return attribute object after successful loading into schema"""

        return Attribute(**data)
