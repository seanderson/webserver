import os
basedir = os.path.abspath(os.path.dirname(__file__))


#SQLALCHEMY_DATABASE_URI = 'postgresql:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_DATABASE_URI = 'postgresql:///tododb'
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

### from before

CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'

OPENID_PROVIDERS = [
    {'name': 'Yahoo', 'url': 'https://me.yahoo.com'}]

