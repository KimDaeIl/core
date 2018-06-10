# Created put.py by KimDaeil on 04/28/2018

from datetime import datetime

from server.utils.security import AESCipher
from models.sessions import SessionModel
from models.users import UserModel

from . import UnauthorizedException, NotFoundException
from . import request


def validate():
    def _(date):
        result = {}

        session = request.headers.get("Authorization", "")

        session_value = AESCipher().decrypt(session).split("_")

        if len(session_value) != 3:
            raise UnauthorizedException("default", "user_info")

        try:
            result["user_id"] = int(session_value[0])
        except ValueError as e:
            result["user_id"] = 0

        result["ip_address"] = session_value[1]
        result["salt"] = session_value[2]

        return result, "200"

    return _


def update_session():
    def _(data):
        result = {}

        user_id = data.get("user_id", 0)
        if not isinstance(user_id, int) or user_id == 0:
            raise UnauthorizedException("default", "user_info")

        session = SessionModel.find_by_id(data.get("user_id", 0))
        session.updated_at = datetime.now()
        result = session.create()

        return result, "200"

    return _


def get_user_info():
    def _(data):
        result = {}

        user = UserModel.find_by_id(data.get("id", 0))

        if user.id == 0:
            raise NotFoundException("user", "default")

        result.update({"user": user.to_json()})
        result["user"].update({"session": data})

        return result, "200"

    return _
