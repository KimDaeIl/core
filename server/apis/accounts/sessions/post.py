# Created post.py by KimDaeil on 04/28/2018

from . import NotFoundException, UnauthorizedException
from core.server.utils.common.security import make_password_hash
from core.models.sessions import SessionModel
from core.models.users import UserModel


def validate():
    def _(data):
        result = {}

        keys_all = ["uid", "password"]
        nullables = []

        for k in keys_all:
            if k in data:
                if data[k] is None and k in nullables:
                    data[k] = "" if isinstance(data[k], str) else 0

                result[k] = data[k]

        return result, "200"

    return _


def find_user():
    def _(data):
        result = {}

        user = UserModel.find_by_email(data.get("uid", ""))

        if user.id == 0:
            raise NotFoundException(attribute="user", details="default")

        password = make_password_hash(data.get("password", ""), user.salt)

        if user.uid != data.get("uid", "") or user.password != password:
            raise UnauthorizedException(attribute="default", details="login")

        result["user"] = user.to_json()

        return result, "200"

    return _


def create_session():
    def _(data):
        result = {}

        print("session.post.create_session >> ", data)
        if "user" in data and "id" in data["user"]:
            session = SessionModel.find_by_id(data["user"]["id"])

            if session.id != 0:
                session.update_session(data["user"])

                data.get("user", {}).update(session.create())
                result = data

        return result, "200"

    return _
