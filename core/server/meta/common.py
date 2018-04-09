# Created common.py by KimDaeil on 04/03/2018
import datetime

user_meta = {
    "signUp": {
        "all": ["uid", "password", "birthYear", "birthMonth", "birthDay", "gender"],
        "required": ["uid", "password", "birthYear", "birthMonth", "birthDay", "gender"],
        "optional": []
    },
    "email": {
        "minLength": 10,
        "maxLength": 255
    },
    "gender": {
        "default": "f",
        "enum": ["m", "f"]
    },
    "password": {
        "maxLength": 16,
        "minLength": 12,
        "special": {
            "minLength": 1,
            "maxLength": 14,
            "enum": "!#\$%&()*+,-./:<>?@\^_~"
        },
        "upper_case": {
            "minLength": 1,
            "maxLength": 14
        }
    },
    "birthYear": {
        "minLength": 1970,
        "maxLength": datetime.datetime.now().year
    },
    "birthMonth": {
        "minLength": 1,
        "maxLength": 12
    }

}


def get_sign_up(code):
    return user_meta.get("signUp").get(code) \
        if code and code in user_meta.get("signUp").keys() \
        else user_meta.get("signUp")
