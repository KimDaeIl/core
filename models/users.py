# Created users.py by KimDaeil on 04/14/2018
from datetime import datetime

from models import *

from server.utils.security import make_hashed


class UserModel(db.Model):
    __tablename__ = 'USERS'

    id = BigInt("id", primary_key=True, index=True, server_default=seq_users_id.next_value())
    uid = String("uid", 255, index=True)
    salt = String("salt", 256)
    password = String("password", 256)
    birth_year = Int("birth_year", default=1970)
    birth_month = Int("birth_month", default=1)
    birth_day = Int("birth_day", default=1)
    push_token = String("push_token", 256, default="", server_default="t")
    receive_push = Bool("receive_push", default=True, server_default="t")
    receive_marketing = Bool("receive_marketing", default=True, server_default="t")
    gender = String("gender", 1, default="f")
    created_at = DateTime("created_at")

    __table_agrs__ = (db.UniqueConstraint("uid"),
                      db.Index("idx_users_uid", "uid", postgresql_using="hash"))

    session = None

    def __init__(self):
        self.id = 0

    def to_json(self):
        print("models.Users.datetime >> ", self.created_at)
        print("models.Users.password >> ", self.password)
        user = {
            "id": self.id,
            "uid": self.uid,
            "birthYear": self.birth_year,
            "birthMonth": self.birth_month,
            "birthDay": self.birth_day,
            "gender": self.gender,
            "pushToken": self.push_token,
            "push": self.receive_push,
            "marketing": self.receive_marketing,
            "createdAt": self.created_at.isoformat()
        }

        if self.session:
            user.update({"session": self.session.to_json()})

        return user

    def create_user(self):
        result = {}

        if self.id != 0:
            db.session.add(self)
            db.session.commit()
            result = self.to_json()

        return result

    def update_user(self):
        result = {}

        if self.id != 0:
            db.session.add(self)
            db.session.commit()
            result = self.to_json()

        return result

    def delete_user(self):
        result = {}

        if self.id != 0:
            db.session.delete(self)
            db.session.commit()
            result = self.to_json()

        return result

    # def generate_password(self):
    #     self.password = make_hashed("{}{}".format(self.password, self.salt))

    @classmethod
    def find_by_id(cls, user_id):
        user = cls()
        if user_id and isinstance(user_id, int):
            temp_user = db.session.query(cls).filter(cls.id == user_id).first()

            if temp_user:
                user = temp_user

        return user

    @classmethod
    def find_by_email(cls, email):
        user = cls()

        if email:
            temp_user = db.session.query(cls).filter(cls.uid == email).first()

            if temp_user:
                user = temp_user

        return user
