# Created sessions.py by KimDaeil on 04/17/2018

from datetime import datetime

from flask import request

from core.models import *
from core.models.mongos.sessions import SessionMongo
from core.server.utils.encryption import AESCipher


class Sessions(db.Model):
    __tablename__ = "SESSIONS"

    id = BigInt("id", primary_key=True, index=True)
    session = String("session", 256)
    ip_address = String("ip_address", 40)
    platform = String("platform", 64)
    platform_version = String("platform_version", 64)
    ##
    salt = String("salt", 126)
    created_at = DateTime("created_at")

    def to_json(self, has_salt=False):
        json = {
            "id": self.id,
            "session": self.session,
            "ipAddress": self.ip_address if self.ip_address else "",
            "platform": self.platform if self.platform else "",
            "platform_version": self.platform_version if self.platform_version else "",
            "createdAt": self.created_at.isoformat() if self.created_at else ""
        }

        if has_salt:
            json["salt"] = self.salt

        return json

    def create(self):
        session = {}
        if self.id and self.id > 0:
            db.session.add(self)
            db.session.commit()

            if self.id > 0:
                session = self.to_json(True)

                SessionMongo.create(session)

                if "salt" in session:
                    del session["salt"]

        return session

    @classmethod
    def create_by_user(cls, user):
        from core.server.utils import make_salt
        if user is None or "id" not in user:
            # TODO: 2018. 04. 20. raise error
            pass

        user_agent = request.user_agent

        session = cls()
        session.id = user.get("id", 0)
        session.salt = make_salt("{}{}".format(user.get("salt", ""), datetime.now()))
        session.session = generate_session(user.get("id"), request.remote_addr, session.salt)
        session.ip_address = request.remote_addr
        session.platform = user_agent.platform if user_agent.platform else ""
        session.platform_version = user_agent.version if user_agent.version else ""

        return session

    @classmethod
    def find_by_id(cls, user_id):
        session = None

        if user_id and isinstance(user_id, int) and user_id > 0:
            session = db.session.query(Sessions).filter(Sessions.id == user_id).first()

        return session if session else Sessions


def generate_session(_id, ip_address, salt):
    session = "{}_{}_{}".format(_id, ip_address, salt)
    session = AESCipher().encrypt(session)

    return session
