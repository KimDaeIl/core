# Created resource.py by KimDaeil on 03/31/2018
from flask_restful import Resource
from server.utils.api_creator import ApiCreator
from server.apis.common.exceptions import MethodNotAllowedException


class BaseResource(Resource):
    def post(self):
        raise MethodNotAllowedException(attribute="default", details="default")

    def get(self):
        raise MethodNotAllowedException(attribute="default", details="default")

    def put(self):
        raise MethodNotAllowedException(attribute="default", details="default")

    def delete(self):
        raise MethodNotAllowedException(attribute="default", details="default")
