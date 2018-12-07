import os # use env variable for email and password


class Config:
    SECRET_KEY = 'mysecret' # set secret key for forms to work
    basedir = os.path.abspath(os.path.dirname(__file__))
    SQLALCHEMY_DATABASE_URI = 'sqlite:///'+os.path.join(basedir,'data.sqlite')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ['EMAIL_USERNAME']
    MAIL_PASSWORD = os.environ['EMAIL_PASSWORD']