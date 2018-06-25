"Module for asset category endpoint test"
import pytest

from os import getenv

from flask import json, request

from api.models.asset_category import AssetCategory
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
                                             init_db, auth_header, request_ctx,
                                             mock_request_obj_decoded_token):
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


    def test_get_one_asset_category(self, client, init_db, auth_header):
        """
        Tests that a single asset category can be retrieved
        """
        asset_category = AssetCategory(name='TestLaptop')
        asset_category.save()

        response = client.get('{}/asset-categories/{}'.format(
          api_v1_base_url, asset_category.id), headers=auth_header)

        response_json = json.loads(response.data.decode(CHARSET))

        assert response.status_code == 200
        assert response_json['status'] == 'success'
        assert response_json['data']['name'] == 'TestLaptop'
        assert type(response_json['data']['customAttributes']) == list

    def test_get_one_asset_category_not_found(self, client, init_db,
                                              auth_header):
        """
        Tests that 404 is returned for an asset category that does not exist
        """
        asset_category = AssetCategory(name='TestLaptop')
        asset_category.save()

        response = client.get('{}/asset-categories/-L2'.format(api_v1_base_url),
                              headers=auth_header)

        response_json = json.loads(response.data.decode(CHARSET))
        assert response.status_code == 404
        assert response_json['status'] == 'error'
        assert response_json['message'] == 'Asset category not found'

    def test_get_one_asset_category_invalid_id(self, client, init_db,
                                               auth_header):
        """
        Tests that 400 is returned for an invalid id
        """
        asset_category = AssetCategory(name='TestLaptop')
        asset_category.save()

        response = client.get('{}/asset-categories/L@@'.format(api_v1_base_url),
                              headers=auth_header)

        response_json = json.loads(response.data.decode(CHARSET))
        assert response.status_code == 400
        assert response_json['status'] == 'error'
        assert response_json['message'] == 'Invalid id in parameter'

    def test_delete_asset_category(self, client, init_db, auth_header):
        """
            Tests that a single asset category can be deleted
        """
        asset_category = AssetCategory(name='TestLaptop')
        asset_category.save()

        response = client.delete('{}/asset-categories/{}'.format(
            api_v1_base_url, asset_category.id), headers=auth_header)

        response_json = json.loads(response.data.decode(CHARSET))

        assert response.status_code == 200
        assert response_json['status'] == 'success'

    def test_delete_asset_category_not_found(self, client, init_db,
                                             auth_header):
        """
            Tests that 404 is returned for a category that does not exist on
            delete
        """

        response = client.delete('{}/asset-categories/-L2'.format(
            api_v1_base_url), headers=auth_header)
        response_json = json.loads(response.data.decode(CHARSET))
        assert response.status_code == 404
        assert response_json['status'] == 'error'
        assert response_json['message'] == 'Asset category not found'

    def test_delete_asset_category_invalid_id(self, client, init_db,
                                              auth_header):
        """
        Tests that 400 is returned when id is invalid
        """
        asset_category = AssetCategory(name='TestLaptop')
        asset_category.save()

        response = client.delete('{}/asset-categories/LX@'.format(
            api_v1_base_url), headers=auth_header)

        response_json = json.loads(response.data.decode(CHARSET))
        assert response.status_code == 400
        assert response_json['status'] == 'error'
        assert response_json['message'] == 'Invalid id in parameter'

    def test_asset_categories_list_endpoint(self, client, auth_header):
        response = client.get(f'{api_v1_base_url}/asset-categories',
                              headers=auth_header)
        response_json = json.loads(response.data.decode(CHARSET))

        assert response.status_code == 200
        assert response_json['status'] == 'success'
        assert isinstance(response_json['data'], list)
        assert len(response_json['data']) is not 0
        assert response_json['data'][0]['name'] == 'Headset'

    def test_asset_categories_list_endpoint_args(self, client, auth_header):
        asset_category = AssetCategory(name='Laptop')
        asset_category2 = AssetCategory(name='Chairs')
        asset_category.save()
        asset_category2.save()
        response = client.get(f'{api_v1_base_url}/asset-categories?where=name,like,chairs',
                              headers=auth_header)
        response_json = json.loads(response.data.decode(CHARSET))

        assert response.status_code == 200
        assert response_json['status'] == 'success'
        assert isinstance(response_json['data'], list)
        assert len(response_json['data']) is 1
        assert response_json['data'][0]['name'] == 'Chairs'

        invalid_response = client.get(f'{api_v1_base_url}/asset-categories?where=name,like.chairs',
                                      headers=auth_header)
        invalid_response_json = json.loads(invalid_response.data.decode(CHARSET))

        assert invalid_response.status_code == 400
        assert invalid_response_json['status'] == 'error'
        asset_category.delete()
        asset_category2.delete()

