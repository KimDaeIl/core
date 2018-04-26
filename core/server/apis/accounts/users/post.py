# Created users.post.py by KimDaeil on 03/31/2018


from core.server.utils.validations.user import *
from . import InternalServerErrorException
from core.models.users import Users, generate_password
from core.models.sessions import Sessions
from core.server.utils import make_hashed


# validate: check essential data to sign up
def validate():
    def _(data):
        #  uid
        validate_uid(data.get("uid"))

        # password
        validate_password(data.get("password"))

        # birth_date
        data["birthYear"], data["birthMonth"], data["birthDay"] = validate_birth_date(data.get("birthYear"),
                                                                                      data.get("birthMonth"),
                                                                                      data.get("birthDay"))

        # birthMonth
        validate_gender(data.get("gender"))

        return data, "200"

    return _


# create user
# 가입 타입 및 조건에 맞게 데이터 파싱: 현재는 없음..ㅋㅋㅋ
# 소셜이나 전번 가입 시
def create_user():
    def _(data):
        result = {}

        user = Users()
        user.id = None
        user.uid = data.get("uid")
        user.salt = make_hashed(datetime.now())
        user.password = make_hashed("{}{}".format(data.get("password"), user.salt))
        user.birth_year = data.get("birthYear")
        user.birth_month = data.get("birthMonth")
        user.birth_day = data.get("birthDay")
        user.gender = data.get("gender")

        result["user"] = user.create_user()

        if result.get("id") == 0:
            raise InternalServerErrorException(attribute="create", details="user")

        return result, "200"

    return _


# create session
def create_session():
    def _(data):
        # if "id" not in data and data["id"] is None:
        #     TODO: 2018. 04. 20. raise ERROR
        # pass

        session = Sessions.create_by_user(data.get("user", {}))

        if session.id == 0:
            # TODO: 2018. 04. 20. raise error
            pass

        data['user'].update({"session": session.create()})
        return data, "200"

    return _


# auth by email
def send_auth_mail():
    def _(req):
        status = "200"
        data = {}

        return data, "200"

    return _
