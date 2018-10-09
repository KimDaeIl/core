# Created users.post.py by KimDaeil on 10/09/2018

from core.server.utils.common.security import generate_salt, make_session_salt
from core.server.utils.validations.user import decryption_data
from . import UnauthorizedException
from . import UserModel

from . import validate_uid

essential = ["uid"]
keys = ["uid"]
nullable = []
validation_function = {
    "uid": lambda x: x
}


def get_salt(data):
    result = {}

    uid = data.get("uid", "")
    salt = ""

    if uid:
        salt = __get_user_salt(validate_uid(uid))
    else:
        salt = __create_new_salt()

    result["salt"] = salt
    return result


def __create_new_salt():
    return make_session_salt(generate_salt())


def __get_user_salt(uid):
    if not uid:
        raise UnauthorizedException()

    user = UserModel.find_by_email(uid)

    if not user or not user.id:
        raise UnauthorizedException()

    return decryption_data(user.salt)
