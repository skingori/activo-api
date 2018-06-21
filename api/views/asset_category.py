from flask_restplus import Resource
from flask import request, jsonify

from api.models import AssetCategory
from main import api
from api.middlewares.token_required import token_required
from api.utilities.model_serializers.asset_category import AssetCategorySchema
from api.utilities.model_serializers.attribute import AttributeSchema


@api.route('/asset-categories')
class AssetCategoryResource(Resource):
    """
    Resource class for peforming crud on the asset categories
    """

    @token_required
    def post(self):
        """
        Creates asset categories and the corresponding attributes
        """

        request_data = request.get_json()

        asset_category_schema = AssetCategorySchema()
        asset_category = asset_category_schema.load_object_into_schema(
            request_data)

        attributes_data = request_data.get('attributes')
        attributes = []

        if attributes_data:
            attributes_schema = AttributeSchema(many=True,
                                                exclude=['id', 'deleted'])

            attributes = attributes_schema.load_object_into_schema(
                attributes_data)

            asset_category.attributes = attributes
            attributes = attributes_schema.dump(attributes).data

        asset_category = asset_category.save()

        response = jsonify({
            "status": 'success',
            "data": {
                "name": asset_category.name,
                "customAttributes": attributes
            }
        })

        response.status_code = 201
        return response




@api.route('/asset-categories/stats')
class AssetCategoryStats(Resource):
    """
    Resource class for getting asset categories and
    their corresponding asset counts
    """

    @token_required
    def get(self):
        """
        Gets asset categories and the corresponding asset count
        """
        asset_categories = AssetCategory._query(request.args)
        data = []
        for asset_category in asset_categories:
            data.append({
                'id': asset_category.id,
                'name': asset_category.name,
                'asset_count': asset_category.assets_count
            })
        return {
            'status': 'success',
            'data': data
        }
