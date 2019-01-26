import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

class Config(object):
  SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
  SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
    'sqlite:///' + os.path.join(basedir, 'app.db')
  SQLALCHEMY_TRACK_MODIFICATIONS = False
  LOG_TO_STDOUT = os.environ.get('LOG_TO_STDOUT')
  
  MAIL_SERVER = 'smtp.googlemail.com'
  MAIL_PORT = 587
  MAIL_USE_TLS = True
  MAIL_USERNAME = 'huzii.yevhenii@gmail.com'
  MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
  ADMINS = ['zoof24@gmail.com']

  POSTS_PER_PAGE = 5
  LANGUAGES = ['en', 'ru']

  MULTILLECT_ACCOUNT_ID = '952'
  MULTILLECT_SECRET_KEY = '73fbdfdd92d3822006f935fccabe0020'
  MULTILLECT_URL = 'https://api.multillect.com/translate/json/1.0/'