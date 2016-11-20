from flask.ext.wtf import Form
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired


class LoginForm(Form):
    openid = StringField('openid', validators=[DataRequired()])
    remember_me = BooleanField('remember_me', default=False, validators=[DataRequired()])


class InputForm(Form):
    user = StringField('user', default='me', validators=[DataRequired()])
    task = StringField('task', validators=[DataRequired()])
    done = BooleanField('done', default=False)
