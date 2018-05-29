"""Module for application factory."""
from os import getenv
from flask import Flask, jsonify
from flask_migrate import Migrate
from flask_restplus import Api
from api import api_blueprint
from api.middlewares.base_validator import (middleware_blueprint,
                                            ValidationError)

from config import config
from api.models.database import db
from manage import ma

config_name = getenv('FLASK_ENV', default='production')

api = Api(api_blueprint, doc=False)


def initialize_errorhandlers(application):
    ''' Initialize error handlers '''
    application.register_blueprint(middleware_blueprint)
    application.register_blueprint(api_blueprint)


def create_app(config=config[config_name]):
    """Return app object given config object."""
    app = Flask(__name__)
    app.config.from_object(config)

    # initialize error handlers
    initialize_errorhandlers(app)

    # bind app to db
    db.init_app(app)

    # bind marshmallow to app
    ma.init_app(app)

    # import all models
    from api.models import User, Asset, AssetCategory, Attribute

    import api.views

    # initialize migration scripts
    migrate = Migrate(app, db)

    return app


@api.errorhandler(ValidationError)
@middleware_blueprint.app_errorhandler(ValidationError)
def handle_exception(error):
    """Error handler called when a ValidationError Exception is raised"""

    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response