from os import getenv

from flask import json

from api.utilities.constants import CHARSET
from .mocks.asset_category import (
    valid_asset_category_data,
    invalid_asset_category_data
)

api_v1_base_url = getenv('API_BASE_URL_V1')


class TestAssetCategoriesEndpoints:
    def test_asset_categories_stats_endpoint(self, client, new_asset_category, init_db, auth_header):
        new_asset_category.save()
        response = client.get(f'{api_v1_base_url}/asset-categories/stats',
                              headers=auth_header)
        response_json = json.loads(response.data.decode(CHARSET))
        assert response.status_code == 200
        assert response_json['status'] == 'success'
        assert isinstance(response_json['data'], list)
        assert len(response_json['data']) is not 0
        assert response_json['data'][0]['name'] == 'Laptop'
        new_asset_category.delete()

    def test_create_asset_categories_endpoint_with_valid_data(self, client, new_asset_category, init_db, auth_header):
        data = json.dumps(valid_asset_category_data)
        response = client.post(
            f'{api_v1_base_url}/asset-categories', data=data,
            headers=auth_header
        )
        response_json = json.loads(response.data.decode(CHARSET))
        assert response.status_code == 201
        assert response_json['data']['name'] == valid_asset_category_data['name']
        assert response_json['data']['customAttributes'] == valid_asset_category_data['attributes']
        assert response_json['status'] == 'success'
        
    def test_create_asset_categories_endpoint_with_invalid_data(self, client, new_asset_category, init_db, auth_header):
        data = json.dumps(invalid_asset_category_data)
        response = client.post(
            f'{api_v1_base_url}/asset-categories', data=data, headers=auth_header
        )

        response_json = json.loads(response.data.decode(CHARSET))
        assert response.status_code == 422
        assert response_json['status'] == 'error'
