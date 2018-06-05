from marshmallow import fields, post_load, validate

from .base_schemas import BaseSchema
from api.models.asset_category import AssetCategory


class AssetCategorySchema(BaseSchema):
    """Asset category model schema"""

    name = fields.String(required=True,
                         validate=string_length_60_validator,
                         error_messages={
                             'required':
                             serialization_errors['field_required']})

    @post_load
    def create_asset_category(self, data):
        """Return asset category object after successful loading of data"""

        return AssetCategory(**data)
