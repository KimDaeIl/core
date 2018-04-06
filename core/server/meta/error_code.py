# Created error_code.py by KimDaeil on 04/03/2018

error = {
    "400": {
        "default": "bed request",
        "user.post": ["type", "uid", "password", "birthdayYear", "birthdayMonth", "birthdayDay", "gender"],
        "uid": "uid",
        "password": "password",
        "birthYear": "birthdayYear",
        "birthMonth": "birthdayMonth",
        "birthDay": "birthdayDay",
        "gender": "gender"

    }
}

"""
    400: bed request,
    401: unauthorized
    404: not found
    405: method not allowed
    408: request timeout
    500: internal server error
    503: service unavailable
    """
__allowed_error = ["400", "401", "404", "405", "408", "500", "503"]


def get_400_error_message(code):
    return error.get("400").get(code) if code and code in error.get("400").keys() else error.get("400").get("default")


def get_error_message(code):

    print("error code is {}".format(code))
    if code in __allowed_error:
        return error.get(code).get("default")

    return error.get("400").get("default")
