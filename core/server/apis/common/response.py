# Created resopnse.py by KimDaeil on 04/05/2018

from flask import Response
import json
import datetime


class BaseResponse(Response):
    charset = "utf-8"

    def __init__(self, data=[], status="200",
                 method="GET", resource="/", mimetype="application/json"):
        result = {}

        if (status == "200"):
            result["data"] = data
        else:
            if not isinstance(data, list):
                data = [data]

            result["message"] = parse_error_code(status)
            result["details"] = data

        response = ResponseData(status, method, resource, result)
        super(Response, self).__init__(response=json.dumps(response()), status=status,
                                       mimetype=mimetype)


class ResponseData:
    def __init__(self, code, method, resource, result):
        self.code = code
        self.method = method
        self.resource = resource
        self.result = result
        self.timestamp = datetime.datetime.now().timestamp()

    def __call__(self, *args, **kwargs):
        return self.__dict__


def parse_error_code(code):
    from core.server.meta import error_code

    error_msg = ""
    if code:
        error_msg = error_code.get_error_message(code)

    return error_msg
