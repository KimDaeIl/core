# Created error_code.py by KimDaeil on 04/03/2018

error = {
    "400": {
        "default": "잘못된 요청입니다",
        "user.post": ["누락된게 있어요", "type", "uid", "password", "birthdayYear", "birthdayMonth", "birthdayDay", "gender"],
        "uid": "uid",
        "password": "password",
        "birthYear": "birthdayYear",
        "birthMonth": "birthdayMonth",
        "birthDay": "birthdayDay",
        "gender": "gender"

    }
}


def get_400_error_message(code):
    return error.get("400").get(code) if code and code in error.get("400").keys() else error.get("400").get("default")