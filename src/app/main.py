from flask import Flask
import logging
from datetime import datetime

from flask import Flask
from flask_smorest import Api
from pyctuator.pyctuator import Pyctuator

from .modules.rest.views import rest_api
from .utils.settings import apply_settings

app = Flask(__name__)


logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger(__name__)

apply_settings(app)

actuator = Pyctuator(
    app,
    app_name='crypt-service',
    app_description='Crypt/Encrypt Service API',
    app_url=app.config.get("ACTUATOR_BASE_URI").rstrip("actuator"),
    pyctuator_endpoint_url=app.config.get("ACTUATOR_BASE_URI"),
    registration_url=None
)
actuator.set_build_info(
    name="crypt-service",
    version="1.0.0",
    time=datetime.fromisoformat("2021-11-12T00:00"),
)
api = Api(app, spec_kwargs=app.config.get("SWAGGER_AUTHORIZATION_SETTINGS"))
Api.DEFAULT_ERROR_RESPONSE_NAME = None
api.register_blueprint(rest_api)

if __name__ == "__main__":
    app.run()