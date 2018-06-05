from flask import jsonify, request
from flask_restplus import Resource
# from api.views import api_blueprint
from api.middlewares.base_validator import ValidationError
from api.models.asset_category import AssetCategory
from api.models.attribute import Attribute
from api.models.input_control import InputControl
from api.utilities.to_json import to_json
from main import api


@api.route('/asset-categories')
class AssetCategoryResource(Resource):

    def post(self):
        """Process / routes and returns 'Welcome to the AM api' as json."""

        try:
            fields = request.get_json()
            attributes = list(eval(fields['attributes'][1:-1]))
        except Exception:
            raise ValidationError(
                { 
                    'message': 'Please provide a valid json',
                    'description': 'Json keys and values should be in string'
                }
            )
        asset_category = AssetCategory(name=fields['name'])

        asset_category.save()
             
        custom_attributes = []

        input_control = InputControl.query.filter_by(name='text').first()

        for attribute in attributes:
            category_atrribute = Attribute(
                name=attribute['name'],
                asset_category_id=asset_category.id,
                is_required=attribute['is_required'].lower() == 'true',
                input_control_id=input_control.id
            )

            category_atrribute_json = to_json(category_atrribute)
            del(category_atrribute_json['input_control_id'])
            category_atrribute_json['input_control'] = input_control.name
            category_atrribute.save()
            custom_attributes.append(category_atrribute_json)

        return jsonify(
            dict(
                data=dict(
                    message='Category Created',
                    id=asset_category.id,
                    name=asset_category.name,
                    description=asset_category.description,
                    custom_attributes=custom_attributes
                )
            )
            ), 201
