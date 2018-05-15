# Created resource.py by KimDaeil on 03/31/2018
from flask_restful import Resource
from server.utils.api_creator import ApiCreator
from flask import request
from server.apis.common.exceptions import MethodNotAllowedException
from server.utils.validations.common import session_validator

__all__ = ["BaseResource", "ApiCreator", "request", "session_validator"]


class BaseResource(Resource):
    def post(self, *args, **kwargs):
        raise MethodNotAllowedException(attribute="default", details="default")

    def get(self, *args, **kwargs):
        raise MethodNotAllowedException(attribute="default", details="default")

    def put(self, *args, **kwargs):
        raise MethodNotAllowedException(attribute="default", details="default")

    def delete(self, *args, **kwargs):
        raise MethodNotAllowedException(attribute="default", details="default")
