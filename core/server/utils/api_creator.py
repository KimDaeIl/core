# Created api_creator.py by KimDaeil on 04/01/2018


from flask import Response
from flask import json


class ApiCreator(object):
    def __init__(self, req):
        self.req = req
        self.func_list = []

    def add(self, next_func):
        if callable(next_func):
            self.func_list.append(next_func)

    def run(self):
        data = {}
        status_code = "200"
        mimetype = 'application/json'

        while len(self.func_list) > 0 and status_code == "200":
            func = self.func_list.pop(0)
            status_code, data = func(self.req, self.func_list.pop(0) if len(self.func_list) > 0 else None)

        return Response(response=json.dumps(data), status=int(status_code), mimetype=mimetype)
