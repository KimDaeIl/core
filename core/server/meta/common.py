# Created common.py by KimDaeil on 04/03/2018


user_meta = {
    "signUp": {
        "all": ["type", "uid", "password", "birthdayYear", "birthdayMonth", "birthdayDay", "gender"],
        "required": ["type", "uid", "password", "birthdayYear", "birthdayMonth", "birthdayDay", "gender"],
        "optional": []
    },
    "type": {
        "default": "email",
        "enum": ["email"]},
    "uid": {
        "type": "email",
        "minLength": 10,
        "maxLength": 255
    },
    "gender": {
        "default": "f",
        "enum": ["m", "f"]
    },
    "password": {
        "maxLength": 16,
        "minLength": 8,
        "special": {
            "minLength": 1,
            "maxLength": 14,
            "enum": ["!#$%&()*+,-./:<>?@\^_~"]
        },
        "upper_case": {
            "minLength": 1,
            "maxLength": 14
        }
    }

}


def get_required_for_sign_up():
    return user_meta.get("signUp").get("required")
