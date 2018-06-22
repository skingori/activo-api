from os import getenv

from flask import json

from api.utilities.constants import CHARSET
from .mocks.asset import (
	asset, no_tag, no_serial, non_existing_category, invalid_category_id
)

api_v1_base_url = getenv('API_BASE_URL_V1')


class TestAssetEndpoints:
	def test_for_non_existing_category(self, client, init_db, auth_header):
		"""Tests if a supplied asset_category_id exists in the database"""

		data = json.dumps(non_existing_category)
		response = client.post(f'{api_v1_base_url}/assets',
							   headers=auth_header, data=data)
		response_json = json.loads(response.data.decode(CHARSET))

		assert response.status_code == 400
		assert response_json['status'] == 'error'
		assert response_json['message'] == 'Asset category not found'

	def test_for_invalid_category_id(self, client, init_db, auth_header):
		"""
		Tests if a supplied asset_category_id is in the right format. If it is
		not in the right format, there is no need to make database call
		"""

		data = json.dumps(invalid_category_id)
		response = client.post(f'{api_v1_base_url}/assets',
							   headers=auth_header, data=data)
		response_json = json.loads(response.data.decode(CHARSET))

		assert response.status_code == 400
		assert response_json['status'] == 'error'
		assert response_json['message'] == 'Asset category not found'

	def test_for_missing_tag(self, client, init_db,
							 auth_header, new_asset_category):
		"""Tests if 'tag' attribute is missing in the supplied asset object"""

		new_asset_category.save()
		no_tag['asset_category_id'] = new_asset_category.id
		data = json.dumps(no_tag)
		response = client.post(f'{api_v1_base_url}/assets',
								headers=auth_header, data=data)
		response_json = json.loads(response.data.decode(CHARSET))

		assert response.status_code == 422
		assert response_json['status'] == 'error'
		assert response_json['message'] == 'An error occurred'
		assert response_json['errors'] == {'tag': ['This field is required']}

	def test_for_missing_serial(self, client, init_db, auth_header,
								new_asset_category):
		"""
		Tests if 'serial' attribute is missing in the supplied asset object
		"""

		new_asset_category.save()
		no_serial['asset_category_id'] = new_asset_category.id
		data = json.dumps(no_serial)
		response = client.post(f'{api_v1_base_url}/assets',
								headers=auth_header, data=data)
		response_json = json.loads(response.data.decode(CHARSET))

		assert response.status_code == 422
		assert response_json['status'] == 'error'
		assert response_json['message'] == 'An error occurred'
		assert response_json['errors'] == {
			'serial': ['This field is required']
		}

	def test_for_valid_data(self, client, init_db, auth_header,
							new_asset_category):
		new_asset_category.save()
		"""test when all required conditions are met"""

		asset['asset_category_id'] = new_asset_category.id
		data = json.dumps(asset)
		response = client.post(f'{api_v1_base_url}/assets',
								headers=auth_header, data=data)
		response_json = json.loads(response.data.decode(CHARSET))

		assert response.status_code == 201
		assert response_json['status'] == 'success'
		assert response_json['message'] == 'asset successfully saved'
