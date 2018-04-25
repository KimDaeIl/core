# Created apis.utils.__init__.py.py by KimDaeil on 04/01/2018

from .api_creator import ApiCreator
from base64 import b64encode
from hashlib import sha3_256

__all__ = ["ApiCreator", "validator"]


def make_salt(data):
    if data:
        if not isinstance(data, str):
            data = str(data)

        data = data.encode()

        return b64encode(sha3_256(data).digest()).decode('utf-8')
