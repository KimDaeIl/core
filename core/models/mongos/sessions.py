# Created sessions.py by KimDaeil on 04/25/2018

from . import mongo
from datetime import datetime


class SessionMongo:
    @classmethod
    def create(cls, session):

        if session and isinstance(session, dict):
            if "id" in session:
                print("mongos.SessionMongo.create >> ", mongo.db.session.insert(session))

        return session

    @classmethod
    def find_by_id(cls, user_id):
        result = {}
        if user_id and isinstance(user_id, int):
            data = mongo.db.session.find_one({"id": user_id}, {"_id": False})

            if data:
                result = data

        print("mongos.SessionMongo.find_by_id >> ", result)

        return result
