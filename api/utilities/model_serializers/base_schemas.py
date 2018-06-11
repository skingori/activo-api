""" Module for base marshmallow schema. """
from marshmallow import Schema, fields
from flask import make_response, json, abort
from json import JSONDecodeError

from ..messages.error_messages import serialization_errors
from ...middlewares.base_validator import ValidationError


class BaseSchema(Schema):
    """Base marshmallow schema with common attributes."""
    id = fields.String(dump_only=True)
    deleted = fields.Boolean()

    def load_into_schema(self, data):
        """Helper function to load raw request data into schema"""

        try:
            data, errors = self.loads(data)
        except JSONDecodeError:
            raise ValidationError(serialization_errors['json_invalid'], 400)

        if errors:
            raise ValidationError({'errors': errors}, 422)

        return data


class AuditableBaseSchema(BaseSchema):
    """ Base marshmallow schema for auditable models. """
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)
    deleted_at = fields.DateTime(dump_only=True)
    created_by = fields.DateTime(dump_only=True)
    updated_by = fields.DateTime(dump_only=True)
    deleted_by = fields.DateTime(dump_only=True)
