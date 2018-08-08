# Created post.py by KimDaeil on 04/28/2018

from . import NotFoundException, UnauthorizedException
from core.server.utils.common.security import make_hashed
from core.models.sessions import SessionModel
from core.models.users import UserModel
from core.server.utils.common.security import make_hashed

keys = ["uid", "password", "salt"]
nullable = []



def validate(data):
    result = {}

    keys_all = ["uid", "password", "salt"]
    nullables = []

    for k in keys_all:
        if k in data:
            if data[k] is None and k in nullables:
                data[k] = "" if isinstance(data[k], str) else 0

            result[k] = data[k]

    return result


def find_user(data):
    result = {}
    print("session.post.find_user.data >> ", data)

    user = UserModel.find_by_email(data.get("uid", ""))

    if user.id == 0:
        raise NotFoundException(attribute="user", details="default")

    password = make_hashed(data.get("password"))
    # salt = data.get("hash")

    if user.uid != data.get("uid", "") or user.password != password:
        raise UnauthorizedException(attribute="default", details="login")

    result["user"] = user.to_json()

    return result


def create_session(data):
    result = {}

    if "user" in data and "id" in data["user"]:
        session = SessionModel.find_by_id(data["user"]["id"])

        if session.id == 0:
            session = SessionModel.create_by_user(data["user"])

            session.save()
        data.get("user", {}).update({"session": session.to_json()})

        result = data

    return result
