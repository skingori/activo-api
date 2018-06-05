""" Module for delete validator. """

from marshmallow import ValidationError
from ...models.asset_category import Asset_, AssetCategory


def delete_validate(id):
    asset_category = AssetCategory.query.filter_by(id=id).first()
    if not asset_category:
        print('no asset cat found')
        return False
    for asset in asset_category.assets:
        if not asset.deleted:
            print(f'asset category has asset {asset.name} and was not deleted')
            return False

    return True
