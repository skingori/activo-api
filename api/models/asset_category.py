from .database import db
from sqlalchemy import ForeignKey

class AssetCategory(db.Model):
    __tablename__ = 'asset_category'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    assets = db.relationship('Asset_',
                              backref='asset',
                              lazy='select')
    deleted = db.Column(db.Boolean, default=False)

    def delete(self):
        """
        Delete a model instance.
        """
        if delete_validate(self.id):
            db.session.delete(self)
            db.session.commit()
        else:
            print('model operations: not deleted')

def delete_validate(id, model, children_models=None):
    asset_category = AssetCategory.query.filter_by(id=id).first()
    if not asset_category:
        print('no asset cat found')
        return False
    if children_models:
        for child in children_models:
            for asset in asset_category.child:
                if not asset.deleted:
                    print(f'asset category has asset {asset.name} and was not deleted')
                    return False

    return True


class Asset_(db.Model):
    __tablename__ = 'asset'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    asset_category_id = db.Column(db.Integer,
                        db.ForeignKey('asset_category.id'),
                        nullable=False)
    deleted = db.Column(db.Boolean, default=False)
