# Created models.__init__.py by KimDaeil on 03/31/2018

from . import *
from core.server.utils.orm import db

__all__ = []


class BaseOrmModel(db.Model):
    pass
