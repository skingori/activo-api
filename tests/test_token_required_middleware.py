from os import getenv
from flask import json
from api.utilities.constants import (
    NO_BEARER_MSG, NO_TOKEN_MSG,
    SERVER_ERROR_MESSAGE,
    SIGNATURE_ERROR, EXPIRED_TOKEN_MSG,
    INVALID_TOKEN_MSG
)


class TestTokenRequiredMiddleware:
    def test_token_required_when_a_token_does_not_contain_bearer(self, client):
        response = client.get('/api/v1/asset-categories/stats',
                              headers={'Authorization': 'bb'})
        response_json = json.loads(response.data.decode('utf-8'))

        assert response_json['status_code'] == 400
        assert response_json['message'] == NO_BEARER_MSG['message']

    def test_token_required_with_invalid_token(self, client):
        response = client.get('/api/v1/asset-categories/stats',
                              headers={'Authorization': 'Bearer kkk'})
        response_json = json.loads(response.data.decode('utf-8'))

        assert response_json['status_code'] == 401
        assert response_json['message'] == INVALID_TOKEN_MSG['message']
