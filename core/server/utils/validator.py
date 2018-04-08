# Created validator.py by KimDaeil on 04/03/2018
import functools
from core.server.meta.common import user_meta
from core.server.apis.common.exceptions import *
from werkzeug.exceptions import BadRequest

import re


def validator_decorator(*args, **kwargs):
    def validator_wrapper(func):
        @functools.wraps(func)
        def validator(*args, **kwargs):

            """
            will need to handle resettable data if it added like state message etc.
            """

            req = kwargs.get("req")
            result = None

            status = "200"
            if req:

                error_list = []

                data = req.form.to_dict()
                data.update(req.args.to_dict())

                need_keys = kwargs.get("key")
                for k in need_keys:

                    if k not in data or data[k] == "":
                        raise BadRequestException(k)

                if len(error_list) > 0:
                    status = "400"
                    result = error_list

            else:
                raise BadRequestException(None)

            return func(*args, status=status, result=result)

        return validator

    return validator_wrapper


def validate_uid(uid):
    is_valid = False
    email_meta = user_meta.get("email")

    if not isinstance(uid, str):
        uid = str(uid)

    length = len(uid)

    is_valid = True if email_meta.get("minLength") <= length <= email_meta.get("maxLength") else False
    is_valid = is_valid and re.match(r"^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$", uid)

    if not is_valid:
        raise BadRequestException("uid")


def is_valid_length(data, min, max):
    is_valid = False

    if isinstance(str, int):
        data_len = len(data)
        is_valid = True if min <= data_len and data_len <= max else False

    return is_valid
