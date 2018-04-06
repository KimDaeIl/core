# Created resource.py by KimDaeil on 03/31/2018
from flask_restful import Resource


class BaseResource(Resource):
    def post(self):
        return {"error": "post is not implemented"}

    def get(self):
        return {"error": "get is not implemented"}

    def put(self):
        return {"error": "put is not implemented"}

    def delete(self):
        return {"error": "delete is not implemented"}
