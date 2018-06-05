from marshmallow import fields, post_load, validate

from .base_schemas import BaseSchema
from api.models.assets import Asset


class AssetSchema(BaseSchema):
    """Asset model schema"""

    tag = fields.String(required=True,
                        validate=(string_length_60_validator,
                                  string_validator),
                        error_messages={
                            'required':
                            serialization_errors['field_required']})
    serial = fields.String(required=True,
                           validate=(string_length_60_validator,
                                     string_validator),
                           error_messages={
                               'required':
                               serialization_errors['field_required']})

    @post_load
    def create_asset(self, data):
        """Return asset object after successful loading of data"""

        return Asset(**data)
