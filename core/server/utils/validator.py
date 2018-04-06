# Created validator.py by KimDaeil on 04/03/2018
import functools
from core.server.meta.error_code import get_400_error_message


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
                        error_list.append(get_400_error_message(k))

                if len(error_list) > 0:
                    status = "400"
                    result = error_list

            else:

                status = "400"
                result = get_400_error_message(None)

            return func(*args, status=status, result=result)

        return validator

    return validator_wrapper
