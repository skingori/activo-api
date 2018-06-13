"""Module for User model."""

from .database import db
from .base.base_model import BaseModel


class User(BaseModel):
    """Class for user db table."""

    __tablename__ = 'users'

    name = db.Column(db.String(60), nullable=False)
    email = db.Column(db.String(60), nullable=False, unique=True)
    image_url = db.Column(db.String)

    def __repr__(self):
        return f'<User {self.name}>'
