import os
_basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = False

ADMINS = frozenset(['youremail@yourdomain.com'])
SECRET_KEY = 'somethingimpossibletoguess'
APPLICATION_ROOT = _basedir
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(_basedir, 'app.db')
DATABASE_CONNECT_OPTIONS = {}
SERVER_NAME = '127.0.0.1:5000'
THREADS_PER_PAGE = 8

SESSION_COOKIE_PATH = '/'
SESSION_COOKIE_DOMAIN = '127.0.0.1'
#TODO:Разобраться почему не работает и включить
WTF_CSRF_ENABLED = False
WTF_CSRF_SECRET_KEY = "somethingimpossibletoguess"

SESSION_PERMANENT = True