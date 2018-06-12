from flask import Blueprint
api_v1_base_url = '/api/v1'
api_blueprint = Blueprint('api_blueprint', __name__, url_prefix=api_v1_base_url)
