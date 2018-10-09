# Created users.post.py by KimDaeil on 10/09/2018

from core.server.utils.common.security import generate_salt, make_session_salt
from . import UnauthorizedException
from . import UserModel

from . import validate_int

essential = ["user_id"]
keys = ["user_id"]
nullable = []
validation_function = {
    "user_id": lambda x: validate_int(x, min=0, default=0)
}


def get_salt(data):
    result = {}

    user_id = data.get("user_id", 0)
    salt = ""

    if user_id:
        salt = __get_user_salt(user_id)
    else:
        salt = __create_new_salt()

    result["salt"] = salt
    return result


def __create_new_salt():
    return make_session_salt(generate_salt())


def __get_user_salt(user_id):
    if not user_id:
        raise UnauthorizedException()

    user = UserModel.find_by_id(user_id)

    if not user or not user.id:
        raise UnauthorizedException()

    return user.salt