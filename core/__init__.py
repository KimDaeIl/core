# Created core.__init__.py by KimDaeil on 03/31/2018
from core.server.apis.common.exceptions import *
from core.server.apis.common.response import BaseResponse


def before_first_request():
    from flask import current_app
    from core.models import db

    current_app.response_class = BaseResponse

    db.init_app(current_app)
    db.create_all()

    print("before_first_request")

    @current_app.errorhandler(BadRequestException)
    def bed_request_handler(e):
        return e()

    @current_app.errorhandler(UnauthorizedException)
    def unauthorized_handler(e):
        return e()

    @current_app.errorhandler(InternalServerErrorException)
    def internal_server_handler(e):
        return e()
