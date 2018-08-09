# Created __init__.py.py by KimDaeil on 04/28/2018
from core.server.apis.common.resource import *

from core.models.users import UserModel
from core.models.sessions import SessionModel

from core.server.apis.common.exceptions import *

from core.server.utils.validations.data import *
from core.server.utils.validations.user import *
from . import post, get, put, delete


class Session(BaseResource):
    # login by uid as email
    def post(self, *args, **kwargs):
        creator = ApiCreator()
        creator.add(validate_function)
        creator.add(post.find_user)
        creator.add(post.create_session)
        result = creator.run(
            key=post.essential,
            keys=post.keys,
            nullable=post.nullable,
            validation_function=post.validation_function,
            **kwargs
        )

        return result

    # get salt for login
    @session_validator()
    def get(self, *args, **kwargs):
        print("session.get")
        creator = ApiCreator()
        creator.add(validate_function)
        creator.add(get.validate_request)
        result = creator.run(
            key=get.essential,
            keys=get.keys,
            nullable=get.nullable,
            validation_function=get.validation_function,
            **kwargs
        )

        return result

    # login by session
    @session_validator()
    def put(self, *args, **kwargs):
        creator = ApiCreator()
        creator.add(put.validate)
        creator.add(put.update_session)
        creator.add(put.get_user_info)
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
        creator.add(delete.validate)
        creator.add(delete.delete_session)
        result = creator.run(
            key=[],
            req=request,
            **kwargs
        )
        return result
