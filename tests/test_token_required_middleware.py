from os import getenv
from flask import json
from api.utilities.constants import (
    NO_BEARER_MSG, NO_TOKEN_MSG,
    SERVER_ERROR_MESSAGE,
    SIGNATURE_ERROR, EXPIRED_TOKEN_MSG,
    INVALID_TOKEN_MSG
)
from .helpers.generate_token import generate_token
from api import api_v1_base_url


class TestTokenRequiredMiddleware:
    def test_token_required_when_a_token_does_not_contain_bearer(self, client):
        response = client.get(f'{api_v1_base_url}/asset-categories/stats',
                              headers={'Authorization': 'bb'})
        response_json = json.loads(response.data.decode('utf-8'))

        assert response_json['status_code'] == 400
        assert response_json['message'] == NO_BEARER_MSG['message']

    def test_token_required_with_invalid_token(self, client):
        response = client.get(f'{api_v1_base_url}/asset-categories/stats',
                              headers={'Authorization': 'Bearer invalid_token'})
        response_json = json.loads(response.data.decode('utf-8'))

        assert response_json['status_code'] == 401
        assert response_json['message'] == INVALID_TOKEN_MSG['message']
        
    def test_token_required_with_expired_token(self, client):
        response = client.get(f'{api_v1_base_url}/asset-categories/stats',
                              headers={'Authorization': generate_token(0)})
        response_json = json.loads(response.data.decode('utf-8'))

        assert response_json['status_code'] == 400
        assert response_json['message'] == EXPIRED_TOKEN_MSG['message']
