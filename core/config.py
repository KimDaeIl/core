class Config(object):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class TestConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://root:root1592@api-dev-rds.c2w11tiph4ya.ap-northeast-2.rds.amazonaws.com:5432/test'


class ProductConfig(Config):
    # SQLALCHEMY_DATABASE_URI = 'postgresql://root:root1592@api-dev-rds.c2w11tiph4ya.ap-northeast-2.rds.amazonaws.com:5432/test'
    pass


def get_config(is_test=True):
    return TestConfig if is_test else ProductConfig
