# Created accounts.__init__.py by KimDaeil on 03/31/2018
from . import *
from flask import Blueprint
from flask_restful import Api
from .users import Users

__all__ = ["users_blue_print"]

users_blue_print = Blueprint("users", __name__, url_prefix="/users")
api = Api(users_blue_print)

api.add_resource(Users, '', 'user')
api.add_resource(Users, '/<int:user_id>', endpoint='user_with_id')
