from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String(64), index=False, unique=False)
    task = db.Column(db.String(120), index=True, unique=False)
    done = db.Column(db.String(5), index=True, unique=False)

    def __repr__(self):
        return '<User %r>q' % (self.nickname)

    def symTable(self):
        '''Return user as a dictionary.'''
        d = {}
        d['id'] = self.id
        d['person'] = {}
        d['person']['nickname'] = self.nickname
        d['task'] = self.task
        d['done'] = self.done
        return d

    def to_json(self):
        json_post = {
            'person': self.nickname,
            'task': self.task
        }
        return json_post


            
