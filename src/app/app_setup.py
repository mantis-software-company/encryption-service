import logging
from datetime import datetime

from flask import Flask
from flask_smorest import Api
from pyctuator.pyctuator import Pyctuator

from ..app.modules.rest.views import rest_api
from ..utils.settings import apply_settings

logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger(__name__)

actuator = Pyctuator(
    flask_app,
    app_name='crypt-service',
    app_description='Crypt/Encrypt Service API',
    app_url=flask_app.config.get("ACTUATOR_BASE_URI").rstrip("actuator"),
    pyctuator_endpoint_url=flask_app.config.get("ACTUATOR_BASE_URI"),
    registration_url=None
)
actuator.set_build_info(
    name="crypt-service",
    version="1.0.0",
    time=datetime.fromisoformat("2021-10-12T00:00"),
)
api = Api(flask_app, spec_kwargs=flask_app.config.get("SWAGGER_AUTHORIZATION_SETTINGS"))
print(api)
Api.DEFAULT_ERROR_RESPONSE_NAME = None
api.register_blueprint(rest_api)
