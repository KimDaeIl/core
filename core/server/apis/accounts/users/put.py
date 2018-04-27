# Created users.put.py by KimDaeil on 03/31/2018


from core.server.utils.validations.user import *
from . import NotFoundException, InternalServerErrorException
from core.models.users import Users
from core.server.utils.security import make_hashed, generate_password
from . import user_meta


def validate():
    def _(data):
        result = {}
        keys_all = user_meta.get("update").get("all")
        nullables = user_meta.get("update").get("nullable")

        print("user.put.validate.data >> ", data)
        validation_functions = {
            "password": lambda v: validate_password(v),
            "birthYear": lambda v: validate_birth_year(v),
            "birthMonth": lambda v: validate_birth_month(result["birthYear"], v),
            "birthDay": lambda v: validate_birth_day(result["birthYear"], result["birthMonth"], v),
            "user_id": lambda v: v if isinstance(v, int) else 0
        }

        for key in keys_all:
            if key in data:
                data_value = data[key]
                print("user.qput.validate.key >> ", key, " / ", data[key])

                if data_value is None:
                    if (isinstance(data_value, str) and len(data_value)) or \
                                    (isinstance(data_value, int) or data_value) == 0:
                        if key in nullables:
                            data_value = ""
                        else:
                            raise BadRequestException(attribute=key, details="notNullable")

                else:
                    # validation
                    data_value = validation_functions.get(key)(data_value)

                result[key] = data_value

        print("user.put.validate.result >> ", result)
        return result, "200"

    return _


def update_user():
    def _(data):
        result = {}

        print("user.put.update_user.data >> ", data)
        print("user.put.update_user.password >> ", AESCipher().encrypt(data.get("password")))
        user = Users.find_by_id(data.get("user_id", 0))

        if not user:
            raise NotFoundException(attribute="user", details="id")

        if "password" in data:
            user.salt = make_hashed(datetime.now())
            user.password = data["password"]

            generate_password(user)

        if "birthYear" in data:
            user.birth_year = data["birthYear"]

        if "birthMonth" in data:
            user.birth_month = data["birthMonth"]

        if "birthDay" in data:
            user.birth_day = data["birthDay"]
        result["user"] = user.create_user()
        #
        # if "id" not in result:
        #     raise InternalServerErrorException(attribute="default", details="default")

        return result, "200"

    return _
