# Created sessions.py by KimDaeil on 04/17/2018

from datetime import datetime

from models import *
from server.utils.security import AESCipher
from server.utils.security import make_hashed
from flask import request

from models.mongos.sessions import SessionMongo


class SessionModel(db.Model):
    __tablename__ = 'SESSIONS'

    id = BigInt("id", primary_key=True, index=True, autoincrement=False)
    session = String("session", 256)
    ip_address = String("ip_address", 40)
    platform = String("platform", 64)
    platform_version = String("platform_version", 64)
    salt = String("salt", 126)
    updated_at = DateTime("updated_at")
    created_at = DateTime("created_at")

    __table_agrs__ = (db.Index("idx_sessions_session", "session", postgresql_using="hash"))

    def __init__(self):
        self.id = 0

    def to_json(self, has_salt=False):
        json = {
            # "id": self.id,
            "session": self.session,
            "ipAddress": self.ip_address if self.ip_address else "",
            "platform": self.platform if self.platform else "",
            "platform_version": self.platform_version if self.platform_version else "",
            "updated_at": self.updated_at.isoformat() if self.updated_at else "",
            "createdAt": self.created_at.isoformat() if self.created_at else ""
        }

        if has_salt:
            json["id"] = self.id
            json["salt"] = self.salt

        return json

    def create(self):
        session = {}
        if self.id and self.id > 0:
            db.session.add(self)
            db.session.commit()

            session = self.insert_or_update_in_mongo()

        return session

    def update_session(self, user):
        self.salt = make_salt(user.get("salt", ""))
        self.session = generate_session(user.get("id"), request.remote_addr, self.salt)

    def insert_or_update_in_mongo(self):
        session = self.to_json(True)

        SessionMongo.create_session(session)

        if "salt" in session:
            del session["salt"]

        if "_id" in session:
            del session["_id"]

        return session

    def delete_session(self):
        session = {}
        if self.id != 0:
            db.session.delete(self)
            db.session.commit()

            session = self.to_json(True)

            SessionMongo.delete_session(session)

        return session

    @classmethod
    def create_by_user(cls, user):
        if user is None or "id" not in user:
            # TODO: 2018. 04. 20. raise error
            pass

        user_agent = request.user_agent

        session = cls()
        session.id = user.get("id", 0)
        session.salt = make_salt(user.get("salt", ""))
        session.session = generate_session(user.get("id"), request.remote_addr, session.salt)
        session.ip_address = request.remote_addr
        session.platform = user_agent.platform if user_agent.platform else ""
        session.platform_version = user_agent.version if user_agent.version else ""

        return session

    @classmethod
    def find_by_id(cls, user_id):
        session = cls()

        if user_id and isinstance(user_id, int) and user_id > 0:
            temp_session = db.session.query(SessionModel).filter(SessionModel.id == user_id).first()

            if temp_session:
                session = temp_session

        return session


def make_salt(salt):
    return make_hashed("{}{}".format(salt, datetime.now()))


def generate_session(_id, ip_address, salt):
    session = "{}_{}_{}".format(_id, ip_address, salt)
    session = AESCipher().encrypt(session)

    return session
