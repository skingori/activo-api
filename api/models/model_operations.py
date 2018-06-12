"""Module for generic model operations mixin."""
from datetime import datetime
from uuid import uuid4

from .database import db
from ..utilities.validators.delete_validator import delete_validator
from ..middlewares.base_validator import ValidationError
from ..utilities.messages.error_messages import database_errors


class ModelOperations(object):
    """Mixin class with generic model operations."""
    def save(self):
        """
        Save a model instance
        :return: Model instance
        """
        db.session.add(self)
        db.session.commit()
        return self

    def update(self, **kwargs):
        """
        update entries
        """
        for field, value in kwargs.items():
            setattr(self, field, value)
        db.session.commit()

    @classmethod
    def get(cls, id):
        """
        return entries by id
        """
        return cls.query.get(id)

    def get_relationships(self):
        """
        Method to get all child relationships a model has. Overide in the
        subclass if the model has child models.
        """
        raise NotImplementedError("The get_relationships method must be overriden in all child model classes") #noqa

    def delete(self):
        """
        Soft delete a model instance.
        """
        if delete_validator(self.get_relationships()):
            self.deleted = True
            db.session.add(self)
            db.session.commit()
        else:
            raise ValidationError(dict(
                message=database_errors['model_delete_children']),
                                  status_code=403)

    @classmethod
    def _query(cls):
        """
        return all database entries
        """
        all_entries = cls.query
        return all_entries

    @classmethod
    def count(cls):
        """
        return total entries in the database
        """
        counts = cls.query.count()
        return counts
