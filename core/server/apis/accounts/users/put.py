# Created users.put.py by KimDaeil on 03/31/2018


from core.server.utils.validations.user import *
from . import NotFoundException, InternalServerErrorException
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
                    valid_data = function_dict.get(key)(data_value)
                    data_value = valid_data if valid_data else data_value

                result[key] = data_value
        print("user.put.validate.result >> ", result)
        return result, "200"

    return _


def update_user():
    def _(data):
        result = {}

        print("user.put.update_user.data >> ", data)
        user = Users.find_by_id(data.get("user_id", 0))

        if not user:
            raise NotFoundException(attribute="user", details="id")

        for key in data.keys():
            setattr(user, key, data[key])

        print("update_user >> ", user.to_json())
        # result = user.create_user()
        #
        # if "id" not in result:
        #     raise InternalServerErrorException(attribute="default", details="default")

        return result, "200"

    return _
