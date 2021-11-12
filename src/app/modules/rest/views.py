from flask.views import MethodView
from flask_smorest import Blueprint
from http import HTTPStatus

from .business import encrypt_text, decrypt_text
from .schemas import Request, Response, BaseResponse

rest_api = Blueprint("Encryption", "rest_api", url_prefix="/api/v1",
                     description="Verilen metni AES algoritması ile şifrelemek ve geri çözmek için kullanılır")


@rest_api.route("/encrypt")
class Encrypt(MethodView):
    @rest_api.arguments(Request, location="json")
    @rest_api.response(status_code=HTTPStatus.OK, schema=Response)
    @rest_api.alt_response(status_code=HTTPStatus.BAD_REQUEST, schema=BaseResponse)
    def post(self, args):
        """ Verilen metni AES algoritması ile şifrelemek için kullanılır """
        return encrypt_text(args)


@rest_api.route("/decrypt")
class Encrypt(MethodView):
    @rest_api.arguments(Request, location="json")
    @rest_api.response(status_code=HTTPStatus.OK, schema=Response)
    @rest_api.alt_response(status_code=HTTPStatus.BAD_REQUEST, schema=BaseResponse)
    def post(self, args):
        """ Verilen AES hash kodunun (Base64) şifresini çözmek için kullanılır """
        return decrypt_text(args)
