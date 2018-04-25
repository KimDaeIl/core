# Created users.py by KimDaeil on 04/14/2018
from core.models import *


class Users(db.Model):
    __tablename__ = "USERS"

    id = db.Column("id", db.BigInteger, primary_key=True, index=True, autoincrement=True)
    uid = String("uid", 255, index=True)
    salt = String("salt", 56)
    password = String("password", 256)
    birth_year = Int("birth_year", default=1970)
    birth_month = Int("birth_month", default=1)
    birth_day = Int("birth_day", default=1)
    gender = String("gender", default='f')
    created_at = DateTime("created_at")

    session = None

    def to_json(self):
        print("models.Users.datetime >> ", self.created_at)
        user = {
            "id": self.id,
            "uid": self.uid,
            "birthYear": self.birth_year,
            "birthMonth": self.birth_month,
            "birthDay": self.birth_day,
            "gender": self.gender,
            "createdAt": self.created_at.isoformat()
        }

        user.update({"session": self.session.to_json() if self.session else {}})

        return user

    def create_user(self):
        result = {}

        if self.id != 0:
            db.session.add(self)
            db.session.commit()
            result = self.to_json()

        return result
