from os import getenv
from flask import json
from .mocks.user import user_one
from api.views.asset_category import AssetCategoryResource

class TestAssetCategoriesEndpoints:
    def test_asset_categories_stats_endpoint(self, client, new_asset_category, init_db, auth_header):
        new_asset_category.save()
        response = client.get('/api/v1/asset-categories/stats',
                              headers=auth_header)
        response_json = json.loads(response.data.decode('utf-8'))

        assert response.status_code == 200
        assert response_json['status'] == 'success'
        assert isinstance(response_json['data'], list)
        assert len(response_json['data']) is not 0
        assert response_json['data'][0]['name'] == 'Laptop'
        new_asset_category.delete()

    def test_create_asset_categories_endpoint(self, client, new_asset_category, init_db, auth_header):
        response = client.post('/api/v1/asset-categories', headers=auth_header)
        assert response.status_code == 200
        