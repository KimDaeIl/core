# Created exception.py by KimDaeil on 04/08/2018
from flask import current_app, request


class DefaultException(Exception):
    def __init__(self, code="400", keyword=None):
        Exception.__init__(self)

        if not isinstance(code, str):
            code = str(code)

        self.status_code = code
        self.keyword = keyword

    def __call__(self, *args, **kwargs):
        return current_app.response_class(data=self.keyword, status=self.status_code,
                                          method=request.method, url=request.url)


# 400
class BadRequestException(DefaultException):
    def __init__(self, keyword=None):
        super(BadRequestException, self).__init__(code=400, keyword=keyword)


# 401
class UnauthorizedException(DefaultException):
    def __init__(self, keyword=None):
        super(UnauthorizedException, self).__init__(code=401, keyword=keyword)


# 404
class NotFoundException(DefaultException):
    def __init__(self, keyword=None):
        super(NotFoundException, self).__init__(code=404, keyword=keyword)


# 405
class MethodNotAllowedException(DefaultException):
    def __init__(self, keyword=None):
        super(MethodNotAllowedException, self).__init__(code=405, keyword=keyword)


# 408
class RequestTimeoutException(DefaultException):
    def __init__(self, keyword=None):
        super(RequestTimeoutException, self).__init__(code=408, keyword=keyword)


# 500
class InternalServerErrorException(DefaultException):
    def __init(self, keyword=None):
        super(InternalServerErrorException, self).__init(code=500, keyword=keyword)
