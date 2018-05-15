# Created validator.py by KimDaeil on 04/03/2018
import functools

from models.mongos.sessions import SessionMongo
from models.sessions import SessionModel
from server.utils.security import AESCipher
from flask import request

from server.apis.common.exceptions import *


def validator_decorator(*args, **kwargs):
    def validator_wrapper(func):
        @functools.wraps(func)
        def validator(*args, **kwargs):

            """
            will need to handle resettable data if it added like state message etc.
            """

            data = request.form.to_dict()
            data.update(request.args.to_dict())
            data.update(kwargs)

            need_keys = kwargs.get("key")
            for k in need_keys:

                if k not in data or data[k] == "":
                    print("key >>", k)
                    print("data >>", data)
                    raise BadRequestException(attribute=k, details="default")

            return func(*args, status="200", data=data)

        return validator

    return validator_wrapper


def session_validator():
    def validator_wrapper(func):
        @functools.wraps(func)
        def check_session(*args, **kwargs):

            session = request.headers.get("Authorization")
            print("server.utils.validations.session >>", session)

            # check session to valid
            if session is None or len(session) == 0:
                raise UnauthorizedException(attribute="default", details="default")

            # parse to validate
            session_list = AESCipher().decrypt(session).split("_")

            # 1-1. length validation
            if len(session_list) != 3:
                raise UnauthorizedException(attribute="default", details="user_info")

            # 1-2. first value of session_list is id for user
            # parse string to int
            try:
                user_id = int(session_list[0])
            except ValueError as e:
                raise UnauthorizedException(attribute="default", details="user_info")

            # 2. is id valid number?
            if kwargs.get("user_id", 0) != user_id:
                raise UnauthorizedException(attribute="default", details="user_info")

            # 3. find session in NoSQL and parse to equal
            sessions = SessionMongo.find_by_id(user_id)

            # invalid session data
            if len(sessions) == 0:
                sessions = SessionModel.find_by_id(user_id)

                if sessions.id != 0:
                    sessions = SessionMongo.create_session(sessions.to_json(has_salt=True))

                else:
                    raise UnauthorizedException(attribute="default", details="user_info")

            # parse session data on sessions
            server_session = sessions.get("session", "")

            if len(server_session) != len(session):
                raise UnauthorizedException(attribute="default", details="user_info")

            for s, u in zip(server_session, session):
                print(s, u)
                if s != u:
                    raise UnauthorizedException(attribute="default", details="user_info")
                    break


            return func(*args, **kwargs)

        return check_session

    return validator_wrapper