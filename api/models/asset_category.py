from sqlalchemy.orm import column_property
from sqlalchemy import select, func
from .base.auditable_model import AuditableBaseModel
from . import Asset
from .database import db
from ..utilities.validators.delete_validator import delete_validator
from flask import abort
from ..utilities.messages.error_messages import database_errors
from .asset import Asset
from .attribute import Attribute


class AssetCategory(AuditableBaseModel):
    """
    Model for asset categories
    """

    __tablename__ = 'asset_categories'

    name = db.Column(db.String(60), nullable=False)
    assets = db.relationship('Asset', backref='asset_category',
                             cascade='save-update, delete', lazy='dynamic')
    attributes = db.relationship('Attribute', backref='asset_category',
                                 cascade='save-update, delete', lazy='dynamic')

    def get_relationships(self):
        return (self.assets, self.attributes)

    def __repr__(self):
        return '<AssetCategory {}>'.format(self.name)


AssetCategory.assets_count = column_property(
    select([func.count(Asset.id)])
    .where(Asset.asset_category_id == AssetCategory.id))
