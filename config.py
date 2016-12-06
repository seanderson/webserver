import os
basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'postgresql:///tododb'
# migration IS NOT supported
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

# Note that WTF_CRF is disabled!
CSRF_ENABLED = True
WTF_CSRF_ENABLED = False
# This should be a better key
SECRET_KEY= 'you-will-never-guess'

OPENID_PROVIDERS = [
    {'name': 'Yahoo', 'url': 'https://me.yahoo.com'}]

