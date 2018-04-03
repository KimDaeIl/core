# Created validator.py by KimDaeil on 04/03/2018
import functools


def validator_decorator(*args, **kwargs):
    def validator_wrapper(func):
        @functools.wraps(func)
        def validator(*args, **kwargs):
            """
            data validation

            body, query data 고려


            """
            status = "400"
            data = {"result": "validator"}

            return func(*args, status=status, data=data)

        return validator

    return validator_wrapper
