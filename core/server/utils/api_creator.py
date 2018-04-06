# Created api_creator.py by KimDaeil on 04/01/2018


from flask import current_app
from core.server.utils.validator import validator_decorator


class ApiCreator(object):
    def __init__(self, req):
        self.req = req
        self.func_list = []

    def add(self, func):
        if callable(func):
            self.func_list.append(func)

    @validator_decorator()
    def run(self, **kwargs):

        result = kwargs["result"] if kwargs is not None and "result" in kwargs else {}
        status = kwargs["status"] if kwargs is not None and "status" in kwargs else "400"

        while len(self.func_list) > 0 and status == "200":
            func = self.func_list.pop(0)
            status, result = func(self.req)

        response = current_app.response_class(data=result, status=status,
                                              method=self.req.method, resource=self.req.path)

        # TODO 2018. 04. 06: make log contain of request or response

        return response
