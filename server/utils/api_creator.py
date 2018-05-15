# Created api_creator.py by KimDaeil on 04/01/2018


from flask import current_app

from server.utils.validations.common import validator_decorator


class ApiCreator(object):
    def __init__(self):
        self.func_list = []

    def add(self, func):
        if callable(func):
            self.func_list.append(func)

    @validator_decorator()
    def run(self, **kwargs):

        data = kwargs["data"] if kwargs is not None and "data" in kwargs else {}
        status = kwargs["status"] if kwargs is not None and "status" in kwargs else "400"

        while len(self.func_list) > 0 and status == "200":
            func = self.func_list.pop(0)
            data, status = func(data)

        print("ApiCreator.run.status >> ", status)
        print("ApiCreator.run.data >> ", data)

        response = current_app.response_class(data=data)

        return response