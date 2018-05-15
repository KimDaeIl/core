# Created __init__.py.py by KimDaeil on 04/24/2018

from flask_pymongo import PyMongo
# from .sessions import SessionMongo

from server.apis.common.exceptions import InternalServerErrorException

__all__ = ["mongo"]

mongo = PyMongo()


def mongo_init_app(app):
    if app:
        mongo.init_app(app, config_prefix='MONGODB')
        # mongo.HOST = app.config["MONGODB_HOST"]
        # mongo.PORT = app.config["MONGODB_PORT"]
    else:
        raise InternalServerErrorException(attribute="default", details="mongodb")