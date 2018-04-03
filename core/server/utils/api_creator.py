# Created api_creator.py by KimDaeil on 04/01/2018


from flask import Response
from flask import json
from core.server.utils.validator import validator_decorator


class ApiCreator(object):
    def __init__(self, req):
        self.req = req
        self.func_list = []

    def add(self, func):
        if callable(func):
            self.func_list.append(func)

    @validator_decorator()
    def run(self, status="200", data={}):
        mimetype = "application/json"

        while len(self.func_list) > 0 and status == "200":
            func = self.func_list.pop(0)
            status_code, data = func(self.req)

        return Response(response=json.dumps(data), status=status, mimetype=mimetype)
