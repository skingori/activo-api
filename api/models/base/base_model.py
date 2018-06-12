"""Module for Base Model"""
from ..model_operations import ModelOperations
from ..database import db


class BaseModel(db.Model, ModelOperations):
    """ Base model for all database models.

    attributes:
        id (string, reserved):
            a unique identifier for each instance. Autogenerated.
        deleted (bool, required):
            a flag for soft deletion of model instances.
    """

    __abstract__ = True

    id = db.Column(db.String(36), primary_key=True)
    deleted = db.Column(db.Boolean, nullable=True, default=False)
