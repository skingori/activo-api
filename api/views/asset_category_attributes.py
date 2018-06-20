"""Module for asset category attribute views"""

from flask_restplus import Resource

from main import api
from ..models.asset_category import AssetCategory
from ..utilities.model_serializers.attribute import AttributeSchema
from ..middlewares.token_required import token_required
from ..middlewares.base_validator import ValidationError
from api.utilities.validators.validate_id import validate_id


@api.route('/asset-categories/<string:id>/attributes')
class AssetCategoryAttributes(Resource):
    """Resource class for asset categories attributes"""

    @token_required
    @validate_id
    def get(self, id):
        """Get attributes of an asset category"""

        asset_category = AssetCategory.get(id)
        if not asset_category or asset_category.deleted:
            raise ValidationError({
                'status': 'error',
                'message': 'Asset category not found'
            }, 404)

        attributes_schema = AttributeSchema(many=True, exclude=['deleted'])
        attributes = attributes_schema.dump(asset_category.attributes
                                            .filter_by(deleted=False)).data

        return {
            'status': 'success',
            'message': 'Asset category attributes retrieved',
            'data': {
                'name': asset_category.name,
                'customAttributes': attributes
            }
        }, 200
