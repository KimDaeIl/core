# Created users.put.py by KimDaeil on 03/31/2018


from models.users import UserModel
from server.utils.security import AESCipher
from server.utils.validations.user import *
from . import NotFoundException, BadRequestException


def validate():
    def _(data):
        result = {}
        keys_all = ["password", "birthYear", "birthMonth", "birthDay", "user_id"]
        nullables = []

        print("user.put.validate.data >> ", data)
        validation_functions = {
            "password": lambda v: validate_password(v),
            "birthYear": lambda v: validate_birth_year(v),
            "birthMonth": lambda v: validate_birth_month(result["birthYear"], v),
            "birthDay": lambda v: validate_birth_day(result["birthYear"], result["birthMonth"], v),
            "user_id": lambda v: v if isinstance(v, int) else 0
        }

        for k in keys_all:
            if k in data:
                data_value = data[k]
                print("user.qput.validate.key >> ", k, " / ", data[k])

                if data_value is None:
                    if (isinstance(data_value, str) and len(data_value)) or \
                                    (isinstance(data_value, int) or data_value) == 0:
                        if k in nullables:
                            data_value = ""
                        else:
                            raise BadRequestException(attribute=k, details="notNullable")

                else:
                    # validation
                    data_value = validation_functions.get(k)(data_value)

                result[k] = data_value

        print("user.put.validate.result >> ", result)
        return result, "200"

    return _


def update_user():
    def _(data):
        result = {}

        print("user.put.update_user.data >> ", data)
        print("user.put.update_user.password >> ", AESCipher().encrypt(data.get("password")))
        user = UserModel.find_by_id(data.get("user_id", 0))

        if not user:
            raise NotFoundException(attribute="user", details="id")

        if "password" in data:
            user.password = data["password"]
            user.generate_password()

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

        return result, "200"

    return _
