"""Module for InputControl model."""

from .database import db
from .base.base_model import BaseModel


class InputControl(BaseModel):
    """Class for Attribute db table."""
    
    __tablename__ = 'input_controls'
    name = db.Column(db.String(60), nullable=False)
