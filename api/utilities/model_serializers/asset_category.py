from marshmallow import fields, post_load, validate

from .base_schemas import BaseSchema
from api.models.asset_category import AssetCategory


class AssetCategorySchema(BaseSchema):
    """Asset category model schema"""

    name = fields.String(required=True,
                         validate=validate.Length(
                             max=60, error='Value cannot be greater than 60 characters'),
                         error_messages={'required': 'This field is required'})

    @post_load
    def create_asset_category(self, data):
        """Return asset category object after successful loading of data"""

        return AssetCategory(**data)
