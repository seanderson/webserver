from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from . import login_manager
from app import db

class User(db.Model,UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(128))
    task = db.Column(db.String(120), index=True, unique=False)
    done = db.Column(db.String(5), index=True, unique=False)
    
    def init(self):
        self.email = ''
        self.password_hash = ''
        self.task = ''
        self.done = False

    def __repr__(self):
        return '<User %r>q' % (self.email)

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    
    def symTable(self):
        '''Return user as a dictionary.'''
        d = {}
        d['id'] = self.id
        d['person'] = {}
        d['email'] = self.email
        d['task'] = self.task
        d['done'] = self.done
        return d

    def to_json(self):
        json_post = {
            'person': self.email,
            'task': self.task
        }
        return json_post


            

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

#from flask.ext.login import UserMixin
#from yourapp import login_manager

#@login_manager.user_loader
#def get_user(ident):
#  return User.query.get(int(ident))


#class User(db.Model, UserMixin)
#  id = db.Column(db.Integer, primary_key=True)
  ### yada yada, you know what goes here

