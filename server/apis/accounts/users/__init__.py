# Created users.__init__.py by KimDaeil on 03/31/2018

from core.server.apis.common.resource import *
from core.server.apis.common.exceptions import *
from core.server.utils.validations.data import *

from core.models.users import UserModel
from . import post, put, delete

__all__ = ["UserModel"]


class User(BaseResource):
    def post(self, *args, **kwargs):
        creator = ApiCreator()
        creator.add(validate_function)
        creator.add(post.validate_user_data)
        creator.add(post.create_session)
        creator.add(post.save)
        # creator.add(post.send_auth_mail())
        result = creator.run(
            key=post.essential,
            keys=post.keys,
            nullable=post.nullable,
            validation_function=post.validation_function,
            **kwargs
        )

        return result

    @session_validator()
    def put(self, *args, **kwargs):
        # print(kwargs)
        creator = ApiCreator()
        creator.add(put.validate)
        creator.add(put.update_user)
        result = creator.run(
            key=["user_id"],
            **kwargs
        )

        print(result)
        return result

    def get(self):
        from flask import current_app
        return current_app.response_class(data={"get":"dd"})

    @session_validator()
    def delete(self, *args, **kwargs):
        creator = ApiCreator()
        creator.add(delete.validate)
        creator.add(delete.delete_user)
        result = creator.run(
            key=["user_id"],
            **kwargs)
        return result
