from os import getenv
from flask import json
from api import api_v1_base_url
from api.utilities.constants import UTF_8

class TestAssetCategoriesEndpoints:
    def test_asset_categories_stats_endpoint(self, client, new_asset_category, init_db, auth_header):
        new_asset_category.save()
        response = client.get(f'{api_v1_base_url}/asset-categories/stats',
                              headers=auth_header)
        response_json = json.loads(response.data.decode(UTF_8))
        assert response.status_code == 200
        assert response_json['status'] == 'success'
        assert isinstance(response_json['data'], list)
        assert len(response_json['data']) is not 0
        assert response_json['data'][0]['name'] == 'Laptop'
        new_asset_category.delete()
