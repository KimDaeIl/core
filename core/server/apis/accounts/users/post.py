# Created users.post.py by KimDaeil on 03/31/2018
from core.server.meta.common import get_sign_up
from core.server.utils.validations.user import *


# validate: check essential data to sign up
def validate():
    def _(req):
        status = "200"
        data = {}

        req_data = req.form.to_dict()
        req_data.update(req.args.to_dict())

        #  uid
        validate_uid(req_data.get("uid"))

        # password
        validate_password(req_data.get("password"))

        # birthYear
        validate_birth_year(req_data.get("birthYear"))

        # birthMonth
        validate_birth_month(req_data.get("birthMonth"))

        # birthDay
        # validate_birth_day(req_data.get("birthDay"))

        # gender


        return status, data

    return _


# create user
def create_user():
    def _(req):
        status = "200"
        data = {}

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
