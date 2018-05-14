# Created __init__.py.py by KimDaeil on 04/28/2018

from core.server.apis.common import BaseResource
from core.server.utils.api_creator import ApiCreator
from core.server.utils.validations.common import session_validator
from flask import request, current_app

from . import post, get, put, delete


class Sessions(BaseResource):
    def post(self, *args, **kwargs):
        creator = ApiCreator()
        creator.add(post.validate())
        creator.add(post.find_user())
        creator.add(post.create_session())
        result = creator.run(
            key=["uid", "password"],
            req=request,
            **kwargs
        )

        return result

    @session_validator()
    def get(self, *args, **kwargs):
        return current_app.response_class(data={"session": "get"})

    @session_validator()
    def put(self, *args, **kwargs):
        creator = ApiCreator()
        creator.add(put.validate())
        creator.add(put.update_session())
        result = creator.run(
            key=[],
            req=request,
            **kwargs
        )
        return result

    @session_validator()
    def delete(self, *args, **kwargs):
        creator = ApiCreator()
        creator.add(delete.validate())
        creator.add(delete.delete_session())
        result = creator.run(
            key=[],
            req=request,
            **kwargs
        )
        return result
