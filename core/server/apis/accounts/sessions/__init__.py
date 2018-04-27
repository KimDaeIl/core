# Created __init__.py.py by KimDaeil on 04/28/2018

from flask import request, current_app

from core.server.apis.common import BaseResource
from core.server.utils.api_creator import ApiCreator
from core.server.meta.common import user_meta

from core.models.sessions import SessionModel
from core.models.sessions import SessionMongo
from core.models.users import UserModel

from . import post, get, put, delete


class Sessions(BaseResource):
    def post(self, *args, **kwargs):
        return current_app.response_class(data={"session": "post"})

    def get(self, *args, **kwargs):
        return current_app.response_class(data={"session": "get"})

    def put(self, *args, **kwargs):
        return current_app.response_class(data={"session": "put"})

    def delete(self, *args, **kwargs):
        return current_app.response_class(data={"session": "delete"})