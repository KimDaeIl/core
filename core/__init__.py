# Created core.__init__.py by KimDaeil on 03/31/2018
from core.server.apis.common.exceptions import *
from core.server.apis.common.response import BaseResponse


def before_first_request():
    from flask import current_app

    from core.models import db
    from core.models.mongos import mongo_init_app

    print("before_first_request")
    current_app.response_class = BaseResponse

    print("before_first_request.db_init")
    db.init_app(current_app)
    db.create_all()

    # print("before_first_request.mongo_init")
    mongo_init_app(current_app)

    # 400
    @current_app.errorhandler(BadRequestException)
    def bed_request_handler(e):
        return e()

    # 401
    @current_app.errorhandler(UnauthorizedException)
    def unauthorized_handler(e):
        return e()

    # 404
    @current_app.errorhandler(NotFoundException)
    def not_found_handler(e):
        return e()

    # 405
    @current_app.errorhandler(MethodNotAllowedException)
    def method_not_allowed_handler(e):
        return e()

    # 500
    @current_app.errorhandler(InternalServerErrorException)
    def internal_server_handler(e):
        return e()
