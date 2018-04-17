# Created users.__init__.py by KimDaeil on 03/31/2018
from . import *
from . import post
from flask import request

from core.server.apis.common import BaseResource
from core.server.utils.api_creator import ApiCreator
from core.server.meta.common import get_sign_up

__all__ = ["Users"]


class Users(BaseResource):
    def post(self):
        api_creator = ApiCreator()
        api_creator.add(post.validate())
        api_creator.add(post.create_user())
        # api_creator.add(post.create_session())
        # api_creator.add(post.send_auth_mail())
        result= api_creator.run(
            key=get_sign_up("required"),
            req=request)

        return result

    def get(self):
        api_creator = ApiCreator()
        api_creator.add(post.validate())
        result, status = api_creator.run(
            key=get_sign_up("required"),
            req=request)

        return result, status

    def put(self):
        return {"Users": "get"}

    def delete(self):
        return {"Users": "get"}
