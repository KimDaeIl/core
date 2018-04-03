# Created users.__init__.py by KimDaeil on 03/31/2018
from . import *
from . import post
from flask import request

from core.server.apis.common import BaseResource
from core.server.utils.api_creator import ApiCreator
from core.server.meta.common import get_required_for_sign_up

__all__ = ["Users"]


class Users(BaseResource):
    def post(self, *args, **kwargs):
        return {"Users": "get"}

    def get(self, *args, **kwargs):
        api_creator = ApiCreator(request)
        api_creator.add(post.validate())
        result = api_creator.run(key=get_required_for_sign_up, req=request)
        return result

    def put(self, *args, **kwargs):
        return {"Users": "get"}

    def delete(self, *args, **kwargs):
        return {"Users": "get"}
