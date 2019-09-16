import os
#from sayhello import app

SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:MySQL.@localhost/message_board'
SECRET_KEY = os.getenv('SECRET_KEY', 'secret string')