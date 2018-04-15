# Created validator.py by KimDaeil on 04/03/2018
import functools
from core.server.apis.common.exceptions import *


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


def is_valid_length(data, min, max):
    is_valid = False

    if isinstance(str, int):
        data_len = len(data)
        is_valid = True if min <= data_len and data_len <= max else False

    return is_valid
