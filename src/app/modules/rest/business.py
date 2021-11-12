import base64
import traceback
from http import HTTPStatus

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from flask import current_app
from flask_smorest import abort

from .utils import ResponseObject


def _get_aes_cipher():
    AES_KEY = base64.b64decode(current_app.config.get('AES_KEY'))
    AES_IV = base64.b64decode(current_app.config.get('AES_IV'))
    return AES.new(AES_KEY, AES.MODE_CBC, AES_IV)


def encrypt_text(args):
    text = args.get('text')
    try:
        text = pad(text.encode('utf-8'), AES.block_size)
        text = base64.b64encode(_get_aes_cipher().encrypt(text))
    except Exception as e:
        tb = traceback.format_exc()
        return abort(http_status_code=HTTPStatus.BAD_REQUEST, message="An error occurred while encrypting text",
                     messages=tb, exc=e)
    return ResponseObject(data={'text': text}, status=HTTPStatus.OK)


def decrypt_text(args):
    text = args.get('text')
    try:
        text = base64.b64decode(text)
        text = unpad(_get_aes_cipher().decrypt(text), AES.block_size)
    except Exception as e:
        tb = traceback.format_exc()
        return abort(http_status_code=HTTPStatus.BAD_REQUEST, message="An error occurred while decrypting text",
                     messages=tb, exc=e)
    return ResponseObject(data={'text': text}, status=HTTPStatus.OK)
