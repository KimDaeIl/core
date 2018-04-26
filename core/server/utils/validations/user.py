# Created user.py by KimDaeil on 04/08/2018
import re
from datetime import datetime

from core.server.meta.common import user_meta
from core.server.apis.common.exceptions import BadRequestException
from core.server.utils.encryption import AESCipher


def validate_uid(uid):
    is_valid = False
    email_meta = user_meta.get("email")

    if not isinstance(uid, str):
        uid = str(uid)

    is_valid = True if email_meta.get("minLength") <= len(uid) <= email_meta.get("maxLength") else False
    is_valid = is_valid and bool(re.match(r"^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$", uid))

    if not is_valid:
        raise BadRequestException("uid", "format")


def validate_password(password):
    print("server.utils.validations.validate_password >> ", "password")
    password_meta = user_meta.get("password")

    if not isinstance(password, str):
        password = str(password)

    # TODO 2018.04. 08: decryption by AES with key in config of app
    password = AESCipher().decrypt(password)

    # 길이
    if len(password) < password_meta.get("minLength") or password_meta.get('maxLength') < len(password):
        raise BadRequestException("password", "length")

    if not bool(re.match(r"(?=.*[a-z])(?=.*[0-9])(?=.*[A-Z])(?=.*[{0}])(?=.{{{1},{2}}})".format(
            password_meta.get("special").get("enum"),
            password_meta.get("minLength"),
            password_meta.get("maxLength")), password)):
        raise BadRequestException("password", "format")


def validate_birth_date(year, month, day):
    print("server.utils.validations.validate_birth_date >> ")
    year = validate_birth_year(year)
    month = validate_birth_month(year, month)
    day = validate_birth_day(year, month, day)

    return year, month, day


def validate_birth_year(year):
    print("server.utils.validations.validate_birth_year >> ", year)

    year_meta = user_meta.get("birthYear")

    if not isinstance(year, int):
        try:
            year = int(year)
        except ValueError:
            raise BadRequestException("typeError", "int")

    if year_meta.get("minLength") > year > datetime.now().year:
        raise BadRequestException("birthYear", "outOfRange")

    return year


def validate_birth_month(year, month):
    print("server.utils.validations.validate_birth_month >> ", year, month)

    month_meta = user_meta.get("birthMonth")

    if not isinstance(month, int):
        try:
            month = int(month)
        except ValueError:
            raise BadRequestException("typeError", "int")

    if month_meta.get("minLength") > month > month_meta.get("maxLength"):
        raise BadRequestException("birthMonth", "outOfRange")

    now = datetime.now()
    if year == now.year and month < now.month:
        raise BadRequestException("birthMonth", "outOfNow")

    return month


def validate_birth_day(year, month, day):
    print("server.utils.validations.validate_birth_day >> ", year, month, day)
    if not isinstance(day, int):
        try:
            day = int(day)
        except ValueError:
            raise BadRequestException("typeError", "int")

    import calendar

    last_day = calendar.monthrange(int(year), int(month))[1]
    if 1 > day > last_day:
        raise BadRequestException("birthYear", "outOfRangeMonth")

    now = datetime.now()
    today = now.day
    if now.year == year and now.month == month and day < today:
        raise BadRequestException("birthDay", "oufOfNow")

    return day


def validate_gender(gender):
    meta = user_meta.get("gender")

    if gender not in meta.get("enum"):
        raise BadRequestException("gender", "format")
