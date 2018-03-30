# Created resource.py by KimDaeil on 03/31/2018
from flask_restful import Resource

__all__ = ["BaseResource"]


class BaseResource(Resource):
    def post(self, *args, **kwargs):
        return {"error": "post is not implemented"}

    def get(self, *args, **kwargs):
        return {"error": "get is not implemented"}

    def put(self, *args, **kwargs):
        return {"error": "put is not implemented"}

    def delete(self, *args, **kwargs):
        return {"error": "delete is not implemented"}
