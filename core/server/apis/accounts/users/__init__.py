# Created users.__init__.py by KimDaeil on 03/31/2018
from . import *
from . import post
from flask import request

from core.server.utils.api_creator import ApiCreator
from core.server.apis.common import BaseResource
from core.server.meta.common import get_sign_up
from core.server.utils.validations.common import session_validator

__all__ = ["Users"]


class Users(BaseResource):
    def post(self, *args, **kwargs):
        api_creator = ApiCreator()
        api_creator.add(post.validate())
        api_creator.add(post.create_user())
        api_creator.add(post.create_session())
        # api_creator.add(post.send_auth_mail())
        result = api_creator.run(
            key=get_sign_up("required"),
            req=request)

        return result

    def get(self, *args, **kwargs):
        api_creator = ApiCreator()
        api_creator.add(post.validate())
        result = api_creator.run(
            key=get_sign_up("required"),
            req=request)

        return result

    @session_validator()
    def put(self, *args, **kwargs):
        api_creator = ApiCreator()
        result = api_creator.run(
            key=get_sign_up("required"),
            req=request
        )
        return result

    def delete(self, *args, **kwargs):
        return {"Users": "get"}
