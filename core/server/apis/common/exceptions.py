# Created exception.py by KimDaeil on 04/08/2018
from flask import current_app, request
from werkzeug.exceptions import HTTPException


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


class BadRequestException(DefaultException):
    def __init__(self, keyword=None):
        super(BadRequestException, self).__init__(code=400, keyword=keyword)
