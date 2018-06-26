import os

class Configuration(object):
    DEBUG = True
    PORT = int(os.getenv('PORT','22222'))
    HOST = '140.86.15.104'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'mysql://' \
            + os.getenv('MYSQLCS_USER_NAME','root') + ':' \
            + os.getenv('MYSQLCS_USER_PASSWORD','password') + '@' \
            + os.getenv('MYSQLCS_CONNECT_STRING', \
            '127.0.0.1:3306/sample_db')
