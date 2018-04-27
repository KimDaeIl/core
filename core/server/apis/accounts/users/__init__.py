# Created users.__init__.py by KimDaeil on 03/31/2018

from . import *

from flask import request

from core.server.utils.api_creator import ApiCreator
from core.server.apis.common import BaseResource
from core.server.meta.common import user_meta
from core.models.users import UserModel
from core.server.utils.validations.common import session_validator
from core.server.apis.common.exceptions import *

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
            key=user_meta["post"]["required"],
            req=request,
            **kwargs
        )

        return result

    def get(self, *args, **kwargs):
        raise MethodNotAllowedException(attribute="user", details="get")

    @session_validator()
    def put(self, *args, **kwargs):
        creator = ApiCreator()
        creator.add(put.validate())
        creator.add(put.update_user())
        result = creator.run(
            key=user_meta["update"]["required"],
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
            key=user_meta["delete"]["required"],
            req=request,
            **kwargs)
        return result
