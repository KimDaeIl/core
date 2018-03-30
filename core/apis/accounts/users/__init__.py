# Created users.__init__.py by KimDaeil on 03/31/2018
from . import *

baseResource = __import__('core.apis.common', globals(), locals(), ["BaseResource"], 0)

__all__ = ["Users"]


class Users(baseResource.BaseResource):
    def post(self, *args, **kwargs):
        return {"Users": "get"}

    def get(self, *args, **kwargs):
        return {"Users": "get"}

    def put(self, *args, **kwargs):
        return {"Users": "get"}

    def delete(self, *args, **kwargs):
        return {"Users": "get"}
