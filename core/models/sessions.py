# Created sessions.py by KimDaeil on 04/17/2018

import base64
from hashlib import sha3_256
from datetime import datetime

from flask import request

from core.models import *
from core.server.utils.encryption import AESCipher


class Sessions(db.Model):
    __tablename__ = "SESSIONS"

    id = BigInt("id", primary_key=True, index=True)
    session = String("session", 256)
    ip_address = String("ip_address", 40)
    platform = String("platform", 64)
    platform_version = String("platform_version", 64)
    salt = String("salt", 126)
    created_at = DateTime("created_at")

    def __init__(self):
        self.salt = make_salt()

    def to_json(self):
        return {
            "id": self.id,
            "session": self.session,
            "ipAddress": self.ip_address if self.ip_address else "",
            "platform": self.platform if self.platform else "",
            "platform_version": self.platform_version if self.platform_version else "",
            "createdAt": self.created_at.isoformat() if self.created_at else ""
        }

    def create_session(self):
        result = {}
        print(self.id)
        if self.id != 0:
            db.session.add(self)
            db.session.commit()
            result = self.to_json()

        return result

    @classmethod
    def create_session_by_user(cls, user):
        if user is None or "id" not in user:
            # TODO: 2018. 04. 20. raise error
            pass

        user_agent = request.user_agent

        session = cls()
        session.id = user.get("id", 0)
        session.session = generate_session(user.get("id"), user.get("uid"), session.salt)
        session.ip_address = request.remote_addr
        session.platform = user_agent.platform if user_agent.platform else ""
        session.platform_version = user_agent.version if user_agent.version else ""

        return session

    @classmethod
    def create_by_login(cls, uid, password):
        pass


def make_salt():
    salt = base64.b64encode(sha3_256(str(datetime.now()).encode()).digest()).decode('utf-8')

    return AESCipher().encrypt(salt)


def generate_session(_id, email, salt):
    session = "{}_{}_{}".format(_id, email, salt)
    session = AESCipher().encrypt(session)

    return session
