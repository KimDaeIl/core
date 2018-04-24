# Created validator.py by KimDaeil on 04/03/2018
import functools

from flask import request

from core.models.sessions import Sessions
from core.server.apis.common.exceptions import *
from core.server.utils.encryption import AESCipher


def validator_decorator(*args, **kwargs):
    def validator_wrapper(func):
        @functools.wraps(func)
        def validator(*args, **kwargs):

            """
            will need to handle resettable data if it added like state message etc.
            """

            req = kwargs.get("req")

            data = req.form.to_dict()
            data.update(req.args.to_dict())

            need_keys = kwargs.get("key")
            for k in need_keys:

                if k not in data or data[k] == "":
                    raise BadRequestException(attribute=k, details="default")

            return func(*args, status="200", data=data)

        return validator

    return validator_wrapper


def session_validator():
    def validator_wrapper(func):
        @functools.wraps(func)
        def check_session(*args, **kwargs):
            session = request.headers.get("Authorization")

            if session is None or len(session) == 0:
                raise UnauthorizedException(attribute="default", details="default")

            aes = AESCipher()
            session_list = aes.decrypt(session).split("_")
            print(session_list)

            if len(session_list) != 3:
                raise UnauthorizedException(attribute="user_info", details="default")

            try:
                user_id = int(session_list[0])
            except ValueError as e:
                print(e)
                raise UnauthorizedException(attribute="user_info", details="default")

            # 1. check id
            if kwargs.get("user_id", 0) != user_id:
                raise UnauthorizedException(attribute="user_info", details="id")

            # 2. find session
            session = Sessions.find_by_id(user_id)

            # 3. check ip address

            # 4. check salt


            return func(*args, **kwargs)

        return check_session

    return validator_wrapper


def is_valid_length(data, min, max):
    is_valid = False

    if isinstance(str, int):
        data_len = len(data)
        is_valid = True if min <= data_len and data_len <= max else False

    return is_valid
