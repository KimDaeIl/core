# Created validator.py by KimDaeil on 04/03/2018
import functools
import json
import json.decoder as json_decoder

from core.models.mongos.sessions import SessionMongo
from core.models.sessions import SessionModel
from core.server.utils.common.security import AESCipher
from flask import request

from core.server.apis.common.exceptions import *


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

            try:
                # pass True as silent to request.get_json()
                # then, return None if it has not anything
                json_data = request.get_json(silent=True)

                if json_data:
                    data.update(json_data)

            except json_decoder.JSONDecodeError as e:
                print("validator_decorator: json_decoder.JSONDecodeError >> ", e)
                raise UnauthorizedException()

            # update for remote_addr, platform
            data.update({
                "remote_addr": request.remote_addr,
                "remote_platform": request.user_agent.version,
                "remote_platform_version": request.user_agent.platform
            })

            print("validator_decorator.data:{}".format(data))
            need_keys = kwargs.get("key")
            for k in need_keys:
                # if k not in data or data[k] == "":
                if k not in data:
                    print("key >>", k)
                    print("data >>", data)
                    raise UnauthorizedException()

            return func(*args, status="200", data=data)

        return validator

    return validator_wrapper


def session_validator():
    def validator_wrapper(func):
        @functools.wraps(func)
        def check_session(*args, **kwargs):

            client = request.headers.get("Authorization")

            # 1. check header has 'Authorization' as client access token
            if client and not len(client) == 0:
                print("session_validator >> client invalid data")

            # find by session from client
            session = SessionMongo.find_by_session(client)

            # if not in server, then raise error as a result of return
            if not session or not session.get("id", 0):
                # if "id" not in session or session["id"] == 0:
                print("session_validator >> session is not in mongo server")
                raise UnauthorizedException(attribute="default", details="default")

            server = session.get("session", "")
            if len(server) != len(client):
                print("session_validator >> invalid session")
                raise UnauthorizedException(attribute="default", details="user_info")

            # check ip address on session is equal with client ip.
            if session.get("ipAddress", "") != request.remote_addr:
                print("session_validator >> different ip")
                raise UnauthorizedException(attribute="default", details="user_info")

            kwargs.update({"user_id": session.get("id", 0)})

            return func(*args, **kwargs)

        return check_session

    return validator_wrapper


def validate_session(client):
    print("@@ validate_session")
