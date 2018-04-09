# Created user.py by KimDaeil on 04/08/2018
import re
from flask import current_app

from core.server.meta.common import user_meta
from core.server.apis.common.exceptions import BadRequestException


def validate_uid(uid):
    is_valid = False
    email_meta = user_meta.get("email")

    if not isinstance(uid, str):
        uid = str(uid)

    is_valid = True if email_meta.get("minLength") <= len(uid) <= email_meta.get("maxLength") else False
    is_valid = is_valid and bool(re.match(r"^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$", uid))

    if not is_valid:
        raise BadRequestException("uid")


def validate_password(password):
    is_valid = False
    password_meta = user_meta.get("password")
    if not isinstance(password, str):
        password = str(password)

    # TODO 2018.04. 08: decryption by AES with key in config of app

    is_valid = True if password_meta.get("minLength") <= len(password) <= password_meta.get('maxLength') else False
    is_valid = is_valid and bool(r"(?=.*[a-z])(?=.*[0-9])(?=.*[A-Z])(?=.*[{0}])(?=.{{{1}}},{{{2}}})".format(
        password_meta.get("special").get("enum"),
        password_meta.get("minLength"),
        password_meta.get("maxLength")))

    if not is_valid:
        raise BadRequestException("password")


def validate_birth_year(year):
    year_meta = user_meta.get("birthYear")

    if not isinstance(year, int):
        try:
            year = int(year)
        except ValueError as e:
            raise BadRequestException("birthYear")

    if year_meta.get("minLength") > year > year_meta.get("maxLength"):
        raise BadRequestException("birthYear")


def validate_birth_month(month):
    month_meta = user_meta.get("birthMonth")

    if not isinstance(month, int):
        try:
            month = int(month)
        except ValueError:
            raise BadRequestException("birthMonth")

    print(month_meta)
    if month_meta.get("minLength") > month > month_meta.get("maxLength"):
        raise BadRequestException("birthMonth")
