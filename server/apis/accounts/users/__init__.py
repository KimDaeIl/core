# Created users.__init__.py by KimDaeil on 03/31/2018

# from . import *

from server.apis.common import BaseResource, ApiCreator
from server.utils.validations.common import session_validator
from flask import request

from models.users import UserModel
from server.apis.common.exceptions import *
from . import post, put, delete

__all__ = ["UserModel"]


class Users(BaseResource):
    def post(self, *args, **kwargs):
        creator = ApiCreator()
        creator.add(post.validate())
        creator.add(post.create_user())
        creator.add(post.create_session())
        # creator.add(post.send_auth_mail())
        result = creator.run(
            key=["uid", "password", "birthYear", "birthMonth", "birthDay", "gender"],
            req=request,
            **kwargs
        )

        return result

    def get(self, *args, **kwargs):
        raise MethodNotAllowedException(attribute="default", details="default")

    @session_validator()
    def put(self, *args, **kwargs):
        creator = ApiCreator()
        creator.add(put.validate())
        creator.add(put.update_user())
        result = creator.run(
            key=["user_id"],
            req=request,
            **kwargs
        )

        print(result)
        return result

    @session_validator()
    def delete(self, *args, **kwargs):
        creator = ApiCreator()
        creator.add(delete.validate())
        creator.add(delete.delete_user())
        result = creator.run(
            key= ["user_id"],
            req=request,
            **kwargs)
        return result