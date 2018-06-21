from flask_restplus import Resource
from flask import request, jsonify

from main import api
from api.middlewares.token_required import token_required
from api.utilities.model_serializers.asset import AssetSchema
from api.utilities.validators.valid_id import valid_id
from api.models.asset_category import AssetCategory
from api.middlewares.base_validator import ValidationError


@api.route('/assets')
class AssetResource(Resource):
    """
    Resource class for carrying out CRUD operations on asset entity
    """

    @token_required
    def post(self):
        """
        An endpoint that creates a new asset in the database
        """
        asset_schema = AssetSchema()
        request_data = request.get_json()
        category_id = request_data['asset_category_id']
        if not valid_id(category_id):
            raise ValidationError(
                {'message': 'Invalid asset category id'}, 400)
        asset_category = AssetCategory.get(category_id)
        if not asset_category:
            raise ValidationError(dict(
                message='Asset category not found'))
        new_asset = asset_schema.load_object_into_schema(request_data)
        new_asset.save()
        return {
            'message': 'asset successfully saved',
            'status': 'success',
            'status_code': 201
            }, 201

