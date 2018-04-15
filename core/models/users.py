# Created users.py by KimDaeil on 04/14/2018


class Users:
    id = 1

    def __init__(self, uid, password, birth_year, birth_month, birth_day, gender):
        self.uid = uid
        self.password = password
        self.birth_year = birth_year
        self.birth_month = birth_month
        self.birth_day = birth_day
        self.gender = gender

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
        return self.to_json(ignore_password=False)
