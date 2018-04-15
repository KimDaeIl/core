# Created exception.py by KimDaeil on 04/08/2018
from flask import current_app
from core.server.meta.error_code import error


class DefaultException(Exception):
    def __init__(self, *args, **kwargs):
        # Exception.__init__(self)

        if not isinstance(kwargs["code"], str):
            code = str(kwargs["code"])

        self.status_code = code
        self.data = {}

        self.data["attribute"] = kwargs.get("attribute", "")
        self.data["details"] = error.get(self.status_code).get(self.data.get("attribute")).get(kwargs.get("details"))

        print(self.data)

    def __call__(self, *args, **kwargs):
        return current_app.response_class(data=self.data, status=self.status_code)


# 400
class BadRequestException(DefaultException):
    def __init__(self, attribute=None, details=None):
        super(BadRequestException, self).__init__(code=400, attribute=attribute, details=details)


# 401
class UnauthorizedException(DefaultException):
    def __init__(self, attribute=None, details="default"):
        super(UnauthorizedException, self).__init__(code=401, attribute=attribute, details=details)


# 404
class NotFoundException(DefaultException):
    def __init__(self, attribute=None, details="default"):
        super(NotFoundException, self).__init__(code=404, attribute=attribute, details=details)


# 405
class MethodNotAllowedException(DefaultException):
    def __init__(self, attribute=None, details="default"):
        super(MethodNotAllowedException, self).__init__(code=405, attribute=attribute, details=details)


# 408
class RequestTimeoutException(DefaultException):
    def __init__(self, attribute=None, details="default"):
        super(RequestTimeoutException, self).__init__(code=408, attribute=attribute, details=details)


# 500
class InternalServerErrorException(DefaultException):
    def __init(self, attribute=None, details="default"):
        super(InternalServerErrorException, self).__init(code=500, attribute=attribute, details=details)
