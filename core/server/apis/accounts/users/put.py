# Created users.put.py by KimDaeil on 03/31/2018


from core.server.utils.validations.user import *
from core.models.users import Users
from . import user_meta


def validate():
    def _(data):
        data_value = None
        result = {}
        keys_all = user_meta.get("update").get("all")
        nullables = user_meta.get("update").get("nullable")

        print("user.put.validate.data >> ", data)
        function_dict = {
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
                    data_value = function_dict.get(key)(data_value)

                result[key] = data_value

        return result, "200"

    return _


def update_user():
    def _(data):
        result = {}

        return result, "200"

    return _
