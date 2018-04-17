# Created users.py by KimDaeil on 04/14/2018
from core.models import *
import datetime


class Users(db.Model):
    __tablename__ = "USERS"

    id = BigInt("id", primary_key=True, index=True, autoincrement=True)
    uid = String("uid", 255, unique=True)
    password = String("password", 256)
    birth_year = Int("birth_year", default=1970)
    birth_month = Int("birth_month", default=1)
    birth_day = Int("birth_day", default=1)
    gender = String("gender", default='f')
    created_at = DateTime("created_at")

    def __init__(self, uid, password, birth_year, birth_month, birth_day, gender,
                 created_at=datetime.datetime.now()):
        self.uid = uid
        self.password = password
        self.birth_year = birth_year
        self.birth_month = birth_month
        self.birth_day = birth_day
        self.gender = gender
        self.created_at = created_at

    def to_json(self, ignore_password=True):
        user = {
            "id": self.id,
            "uid": self.uid,
            "birthYear": self.birth_year,
            "birthMonth": self.birth_month,
            "birthDay": self.birth_day,
            "gender": self.gender
        }

        if not ignore_password:
            user["password"] = self.password

        return user

    def create_user(self):
        print("create_user")
        db.session.add(self)
        print("commit", db.session.commit())
        return self.to_json(ignore_password=False)
