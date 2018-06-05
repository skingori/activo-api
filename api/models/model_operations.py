from .database import db
from uuid import uuid4

from ..utilities.validators.delete_validator import delete_validate


class ModelOperations(object):
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

    def delete(self):
        """
        Delete a model instance.
        """
        if delete_validate(self.id):
            db.session.delete(self)
            db.session.commit()
        else:
            print('model operations: not deleted')

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
