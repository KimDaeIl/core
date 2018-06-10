# Created delete.py by KimDaeil on 04/28/2018

from core.server.utils import AESCipher
from core.models.sessions import SessionModel
from . import UnauthorizedException, NotFoundException


def validate():
    def _(data):
        result = {}

        print("session.delete.validate")
        session = data.get("Authorization", "")

        result["user_id"] = data["user_id"]
        # session_value = AESCipher().decrypt(session).split("_")

        # if len(session_value) != 3:
        #     raise UnauthorizedException("default", "user_info")
        #
        # try:
        #     result["user_id"] = int(session_value[0])
        # except ValueError as e:
        #     result["user_id"] = 0
        #
        # result["ip_address"] = session_value[1]
        # result["salt"] = session_value[2]
        return result, "200"

    return _


def delete_session():
    def _(data):
        result = {}

        user_id = data.get("user_id", 0)
        if not isinstance(user_id, int) or user_id == 0:
            raise UnauthorizedException("default", "user_info")

        session = SessionModel.find_by_id(data.get("user_id", 0))

        if session.id == 0:
            raise NotFoundException("session", "default")

        session.delete_session()

        result["session"] = session.to_json()

        return result, "200"

    return _
