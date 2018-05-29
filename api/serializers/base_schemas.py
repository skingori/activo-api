""" Module for base marshmallow schema. """
from marshmallow import (Schema, ValidationError, fields, post_load, pre_load,
                         validates)


class BaseSchema(Schema):
    """Base marshmallow schema with common attributes."""
    id = fields.String(dump_only=True)


class AuditableBaseSchema(BaseSchema):
    """ Base marshmallow schema for auditable models. """
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)
    deleted_at = fields.DateTime(dump_only=True)
    created_by = fields.DateTime(dump_only=True)
    updated_by = fields.DateTime(dump_only=True)
    deleted_by = fields.DateTime(dump_only=True)
