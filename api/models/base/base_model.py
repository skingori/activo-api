"""Module for Base Model"""

import uuid
from sqlalchemy.dialects.postgresql import UUID

from ..model_operations import ModelOperations
from ..database import db


class BaseModel(db.Model, ModelOperations):
    """ Base model """

    __abstract__ = True

    id = db.Column(db.String(60), primary_key=True, default=uuid.uuid4)
