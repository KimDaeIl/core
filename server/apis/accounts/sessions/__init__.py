# Created __init__.py.py by KimDaeil on 04/28/2018

from core.server.apis.common.resource import *
from core.server.apis.common.exceptions import *
from . import post, put, delete


class Sessions(BaseResource):
    # login by uid as email
    def post(self, *args, **kwargs):
        creator = ApiCreator()
        creator.add(post.validate())
        creator.add(post.find_user())
        creator.add(post.create_session())
        result = creator.run(
            key=["uid", "password", "salt"],
            req=request,
            **kwargs
        )

        return result

    # login by session
    @session_validator()
    def put(self, *args, **kwargs):
        creator = ApiCreator()
        creator.add(put.validate())
        creator.add(put.update_session())
        creator.add(put.get_user_info())
        result = creator.run(
            key=[],
            req=request,
            **kwargs
        )
        return result

    # logout
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
