import os

basedir = os.path.abspath(os.path.dirname(__file__))

# print(homedir)

class Config(object):
  # HOST = str(os.environ.get("HOST"))
  # DATABASE = str(os.environ.get("DATABASE"))
  # USERNAME = str(os.environ.get("USERNAME"))
  # PASSWORD = str(os.environ.get("PASSWORD"))
  HOST = 'localhost'
  DATABASE = 'garena'
  USERNAME = 'root'
  PASSWORD = 'root'
  SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://' + USERNAME + ':' + PASSWORD + '@' + HOST + '/' + DATABASE
  SQLALCHEMY_TRACK_MODIFICATIONS = False
  SQLALCHEMY_RECORD_QUERIES = True