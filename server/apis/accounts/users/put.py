# Created users.put.py by KimDaeil on 03/31/2018


from core.models.users import UserModel
from core.server.utils.validations.user import *
from . import NotFoundException, BadRequestException, UnauthorizedException


def validate(data):
    result = {}
    keys = ["password", "birthYear", "birthMonth", "birthDay", "user_id", "salt"]
    nullable = ["password", "birthYear", "birthMonth", "birthDay", "user_id", "salt"]

    print("user.put.py.validate.data >> ", data)
    validation_functions = {
        "password": lambda v: v,
        "salt": lambda v: v,
        "birthYear": lambda v: validate_birth_year(v),
        "birthMonth": lambda v: validate_birth_month(result["birthYear"], v),
        "birthDay": lambda v: validate_birth_day(result["birthYear"], result["birthMonth"], v),
        "user_id": lambda v: v if isinstance(v, int) else 0
    }

    for key in keys:
        if key in data:
            data_value = validation_functions.get(key, lambda x: x)(data[key])
        else:
            if key in nullable:
                continue
            else:
                print(__name__, ".validate >> ", "value not in data or nullable >> {}".format(key))
                raise UnauthorizedException()
            # if data_value is None:
            #     if (isinstance(data_value, str) and len(data_value)) or \
            #             (isinstance(data_value, int) or data_value) == 0:
            #         if key in nullable:
            #             continue
            #         else:
            #             raise BadRequestException(attribute=key, details="notNullable")
            #
            # else:
            # data_value = validation_functions.get(key)(data_value)

        result[key] = data_value

    if not any(result.keys() & set(nullable)):
        print(__name__, ".validate >> ", "noting to update")
        raise UnauthorizedException()
    print("user.put.py.validate.result >> ", result)
    return result


def update_user(data):
    result = {}

    # print("user.put.py.update_user.data >> ", data)
    # print("user.put.py.update_user.password >> ", AESCipher().encrypt(data.get("password")))
    user = UserModel.find_by_id(data.get("user_id", 0))

    if not user:
        raise NotFoundException(attribute="user", details="id")

    if "password" in data:
        user.password = data["password"]
        user.salt = data["salt"]

    if "birthYear" in data:
        user.birth_year = data["birthYear"]

    if "birthMonth" in data:
        user.birth_month = data["birthMonth"]

    if "birthDay" in data:
        user.birth_day = data["birthDay"]

    result["user"] = user.update_user()
    #
    # if "id" not in result:
    #     raise InternalServerErrorException(attribute="default", details="default")

    return result
