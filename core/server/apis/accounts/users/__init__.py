# Created users.__init__.py by KimDaeil on 03/31/2018

from . import *

from flask import request

from core.server.utils.api_creator import ApiCreator
from core.server.apis.common import BaseResource
from core.server.meta.common import user_meta
from core.models.users import Users
from core.server.utils.validations.common import session_validator
from core.server.apis.common.exceptions import *

from . import post, put

__all__ = ["Users"]


class Users(BaseResource):
    def post(self, *args, **kwargs):
        api_creator = ApiCreator()
        api_creator.add(post.validate())
        api_creator.add(post.create_user())
        api_creator.add(post.create_session())
        # api_creator.add(post.send_auth_mail())
        result = api_creator.run(
            key=user_meta["signUp"]["required"],
            req=request,
            **kwargs
        )

        return result

    def get(self, *args, **kwargs):
        raise MethodNotAllowedException(attribute="user", details="get")

    @session_validator()
    def put(self, *args, **kwargs):
        api_creator = ApiCreator()
        api_creator.add(put.validate())
        api_creator.add(put.update_user())
        result = api_creator.run(
            key=user_meta["update"]["required"],
            req=request,
            **kwargs
        )

        print(result)
        return result

    def delete(self, *args, **kwargs):
        return {"Users": "get"}
