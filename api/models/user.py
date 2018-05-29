"""Module for User model."""

from .database import db
from .base.base_model import BaseModel


class User(BaseModel):
    """Class for user db table."""

    def create_user(self, name, email, image_url=None):
        """ Method to create a user object instance. """
        self.name = name
        self.email = email
        self.image_url = image_url if image_url else None
        return self

    __tablename__ = 'users'
    name = db.Column(db.String(60), nullable=False)
    email = db.Column(db.String(60), nullable=False, unique=True)
    image_url = db.Column(db.String)
