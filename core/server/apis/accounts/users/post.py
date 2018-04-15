# Created users.post.py by KimDaeil on 03/31/2018
from core.server.utils.validations.user import *
from core.models.users import Users
from core.server.apis.common.exceptions import InternalServerErrorException


# validate: check essential data to sign up
def validate():
    def _(data):
        print("user.post.validate")
        status = "200"

        #  uid
        validate_uid(data.get("uid"))

        # password
        validate_password(data.get("password"))

        # birth_date
        validate_birth_date(data.get("birthYear"), data.get("birthMonth"), data.get("birthDay"))

        # birthMonth
        validate_gender(data.get("gender"))

        return data, "200"

    return _


# create user
# 가입 타입 및 조건에 맞게 데이터 파싱: 현재는 없음..ㅋㅋㅋ
# 소셜이나 전번 가입 시
def create_user():
    def _(data):
        user = Users(uid=data.get("uid"), password=data.get("password"), birth_year=data.get("birthYear"),
                     birth_month=data.get("birthMonth"), birth_day=data.get("birthDay"),
                     gender=data.get("gender"))

        result = user.create_user()

        if result.get("id") == 0:
            raise InternalServerErrorException(attribute="create", details="user")

        return result, "200"

    return _


# create session
def create_session():
    def _(data):
        result = {}

        return data, "200"

    return _


# auth by email
def send_auth_mail():
    def _(req):
        status = "200"
        data = {}

        return data, "200"

    return _
