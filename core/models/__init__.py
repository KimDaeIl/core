# Created models.__init__.py by KimDaeil on 03/31/2018

from . import *
from core.server.utils.orm import db
import datetime

__all__ = ["db", "String", "Int", "DateTime", "BigInt"]


class BaseColumn(db.Column):
    def __init__(self, *args, **kwarg):
        if 'nullable' not in kwarg:
            kwarg['nullable'] = False

        super().__init__(*args, **kwarg)


class String(BaseColumn):
    def __init__(self, name, length=0, **kwargs):
        if length == 0:
            length = None

        super().__init__(name, db.String(length), **kwargs)


class Int(BaseColumn):
    def __init__(self, name, **kwargs):
        super().__init__(name, db.Integer, **kwargs)


class BigInt(BaseColumn):
    def __init__(self, name, **kwargs):
        super().__init__(name, db.BigInteger, **kwargs)


class DateTime(BaseColumn):
    def __init__(self, name, **kwargs):
        # TODD 2018. 04. 17. make sure that is timezone
        # consider below terms
        # 1. making time zone about server and user
        # 2. make time zone about server
        if 'default' not in kwargs:
            kwargs['default'] = datetime.datetime.utcnow()

        super().__init__(name, db.DateTime, **kwargs)
