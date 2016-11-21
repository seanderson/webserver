
from app import db,models
users = models.User.query.all()
print(users)
for u in users:
    print(u.id,u.nickname,u.task,u.done)
models.User.query.delete()
db.session.commit()
