from marshmallow import fields, post_load, validate

from .base_schemas import BaseSchema
from api.models.assets import Asset


class AssetSchema(BaseSchema):
    """Asset model schema"""

    tag = fields.String(required=True,
                        validate=validate.Length(
                            max=60, error='Value cannot be greater than 60 characters'),
                        error_messages={'required': 'This field is required'})
    serial = fields.String(required=True,
                           validate=validate.Length(
                               max=60, error='Value cannot be greater than 60 characters'),
                           error_messages={'required': 'This field is required'})

    @post_load
    def create_asset(self, data):
        """Return asset object after successful loading of data"""

        return Asset(**data)
