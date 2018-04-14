# Created core.__init__.py by KimDaeil on 03/31/2018
from core.server.apis.common.exceptions import *
from core.server.apis.common.response import BaseResponse


def before_first_request():
    from flask import current_app

    current_app.response_class = BaseResponse
    print("before_first_request")

    @current_app.errorhandler(BadRequestException)
    def bed_request_handler(e):
        return e()
