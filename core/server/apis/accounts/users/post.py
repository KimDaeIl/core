# Created users.post.py by KimDaeil on 03/31/2018


def validate():
    print("post.validate")

    def _(req, next):
        data = {}
        status = "200"
        return "200", data

    return _
