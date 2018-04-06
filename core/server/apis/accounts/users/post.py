# Created users.post.py by KimDaeil on 03/31/2018
from core.server.meta.common import get_sign_up


# validate: check essential data to sign up
def validate():
    def _(req):
        status = "200"
        data = {}

        post_required = get_sign_up("required")

        for k in post_required:
            pass

        return status, data

    return _


def create_user():
    def _(req):
        pass

    return _

# create user

# create session

# auth by email
