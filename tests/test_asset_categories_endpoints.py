"Module for asset category endpoint test"

from os import getenv

from flask import json

from api.utilities.constants import CHARSET
from .mocks.asset_category import (
    valid_asset_category_data,
    invalid_asset_category_data,
    valid_asset_category_data_without_attributes
)
from api.utilities.messages.error_messages import serialization_errors

api_v1_base_url = getenv('API_BASE_URL_V1')


class TestAssetCategoriesEndpoints:
    """"
    Asset Category endpoints test
    """

    def test_asset_categories_stats_endpoint(self, client, new_asset_category,
                                             init_db, auth_header):
        """
        Should pass when getting asset categories stats
        """
        
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

    def test_create_asset_categories_endpoint_with_valid_data(self, client,
                                                              new_asset_category,  # noqa
                                                              init_db,
                                                              auth_header):
        """
        Should pass when valid data is provided
        """

        data = json.dumps(valid_asset_category_data)
        response = client.post(
            f'{api_v1_base_url}/asset-categories', data=data,
            headers=auth_header
        )
        response_json = json.loads(response.data.decode(CHARSET))
        assert response.status_code == 201
        assert response_json['data']['name'] == valid_asset_category_data['name']  # noqa
        assert response_json['data']['customAttributes'] == valid_asset_category_data['attributes']  # noqa
        assert response_json['status'] == 'success'

    def test_create_asset_categories_endpoint_with_valid_data_without_attributes(self, client, new_asset_category, init_db, auth_header):  # noqa
        """
        Should pass when valid data without attributes is provided
        """

        data = json.dumps(valid_asset_category_data_without_attributes)
        response = client.post(
            f'{api_v1_base_url}/asset-categories', data=data,
            headers=auth_header
        )
        response_json = json.loads(response.data.decode(CHARSET))
        assert response.status_code == 201
        assert response_json['data']['name'] == valid_asset_category_data_without_attributes['name']  # noqa
        assert response_json['data']['customAttributes'] == []
        assert response_json['status'] == 'success'
        
    def test_create_asset_categories_endpoint_without_asset_category_name(self,
                                                                          client,  # noqa
                                                                          new_asset_category,  # noqa
                                                                          init_db,  # noqa
                                                                        auth_header):  # noqa
        """
        Should fail when asset category name is not data is provided
        """
        
        data = json.dumps({})
        response = client.post(
            f'{api_v1_base_url}/asset-categories', data=data,
            headers=auth_header
        )

        response_json = json.loads(response.data.decode(CHARSET))
        assert response.status_code == 422
        assert response_json['status'] == 'error'
        assert response_json['errors']['name'][0] == serialization_errors['field_required']  # noqa
    
    def test_create_asset_categories_endpoint_with_invalid_attributes_data(self,  # noqa
                                                                           client,  # noqa
                                                                           new_asset_category,  # noqa
                                                                           init_db,  # noqa
                                                                        auth_header):  # noqa
        """
        Should fail when invalid attributes data is provided
        """
        
        data = json.dumps(invalid_asset_category_data)
        response = client.post(
            f'{api_v1_base_url}/asset-categories', data=data,
            headers=auth_header
        )

        response_json = json.loads(response.data.decode(CHARSET))
        assert response.status_code == 422
        assert response_json['status'] == 'error'
        assert response_json['errors']['0']['label'][0] == serialization_errors['field_required']  # noqa
