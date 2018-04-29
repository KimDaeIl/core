# Created users.delete.py by KimDaeil on 03/31/2018
from . import UnauthorizedException, NotFoundException
from . import UserModel
from core.models.sessions import SessionModel


def validate():
    def _(data):
        result = {}

        keys_all = ["user_id"]
        nullables = []

        validate_functions = {
            "user_id": lambda v: v if v and isinstance(v, int) else 0
        }

        for k in keys_all:
            if k in data and k in validate_functions:
                result[k] = validate_functions.get(k)(data[k])

        return result, "200"

    return _


def delete_user():
    def _(data):
        result = {}

        if data is None or "user_id" not in data:
            raise UnauthorizedException(attribute="default", details="user_info")

        user = UserModel.find_by_id(user_id=data.get("user_id", 0))

        print("delete_user >> ", 0, user)
        if user.id == 0:
            raise NotFoundException(attribute="user", details="uid")

        print("delete_user >> ", user.to_json())
        result["user"] = user.delete_user()

        session = SessionModel.find_by_id(user_id=data.get("user_id", 0))

        print("delete_user >> ", 2)
        if session and session.id != 0:
            print("delete_user >> ", 2 - 1)
            result["user"].update({"sesison": session.delete_session()})

            print("delete_user >> ", 2 - 1)

        print("delete_user >> ", 3)
        return result, "200"

    return _
