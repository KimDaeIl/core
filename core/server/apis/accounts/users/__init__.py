# Created users.__init__.py by KimDaeil on 03/31/2018
from . import *
from . import post
from flask import request, current_app

BaseResource = __import__("core.server.apis.common", globals(), locals(), ["BaseResource"], 0).BaseResource
ApiCreator = __import__("core.server.utils.api_creator", globals(), locals(), ["ApiCreator"], 0).ApiCreator
__all__ = ["Users"]


class Users(BaseResource):
    def post(self, *args, **kwargs):
        return {"Users": "get"}

    def get(self, *args, **kwargs):
        api_creator = ApiCreator(request)
        api_creator.add(post.validate())

        result = api_creator.run()
        return result

    def put(self, *args, **kwargs):
        return {"Users": "get"}

    def delete(self, *args, **kwargs):
        return {"Users": "get"}
