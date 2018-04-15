# Created users.post.py by KimDaeil on 03/31/2018
from core.server.utils.validations.user import *
from core.models.users import Users


# validate: check essential data to sign up
def validate():
    def _(data):
        status = "200"


        #  uid
        validate_uid(data.get("uid"))

        # password
        validate_password(data.get("password"))

        # birth_date
        validate_birth_date(data.get("birthYear"), data.get("birthMonth"), data.get("birthDay"))

        # birthMonth
        validate_gender(data.get("gender"))

        return status, data

    return _


# create user
# 가입 타입 및 조건에 맞게 데이터 파싱
def create_user():
    def _(req):
        status = "200"
        data = {}

        req_data = req.form.to_dict()
        req_data.update(req.args.to_dict())

        uid = req_data.get("uid")
        # password =

        # user = Users(uid=, password=req_data.get("password"), birth_year=req_data.get("birthYear"),
        #              birth_month=req_data.get("birthMonth"), birth_day=req_data.get("birthDay"),
        #              gender=req_data.get("gender"))

        # user.create_user()

        return status, data

    return _


# create session
def create_session():
    def _(req):
        status = "200"
        data = {}

        return status, data

    return _


# auth by email
def send_auth_mail():
    def _(req):
        status = "200"
        data = {}

        return status, data

    return _
