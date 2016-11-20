from flask import render_template, flash, redirect
from app import app
from flask import jsonify

from .forms import LoginForm
from .forms import InputForm

from app import db,models
#from flask.ext.sqlalchemy import SQLAlchemy
#db = SQLAlchemy(app)

# Code executed for localhost:5000/index route
@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'User'}
    posts = [
        {
            'person': {'nickname': 'Sam'},
            'task': 'Write some code.',
            'done': 'no'
        },
        {
            'person': {'nickname': 'Fran'},
            'task': 'Debug my app.',
            'done': 'yes'
        }
    ]
    return render_template('index.html',
                           title='Home',
                           user=user,
                           posts=posts)

# POST requests bring input data to this code.
# Code executed for localhost:5000/login route
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit(): # if True, show user inputs [POST]
        flash('Login requested for OpenID="%s", remember_me=%s' %
              (form.openid.data, str(form.remember_me.data)))
        return redirect('/index')
    # if False, set up login page for user input [GET]
    return render_template('login.html',
                           title='Sign In',
                           form=form,
                           providers=app.config['OPENID_PROVIDERS'])


@app.route('/in',methods=['GET','POST'])
def input():
    form = InputForm()
    if form.validate_on_submit(): # True, show users inputs [POST]
        user = {'nickname':'input'}
        u = models.User()
        u.nickname = form.user.data
        u.task = form.task.data
        if form.done.data == False: u.done = 'No'
        else: u.done = 'Yes'
        db.session.add(u)
        db.session.commit()
        return redirect('/db')
    else:
        return render_template('input.html',
                           title='input',
                           form=form)
    

# Code executed for localhost:5000/index route
@app.route('/db')
def showdb():
    user = {'nickname':'Sven'}
    users = models.User.query.all()
    lst = [ ]
    for u in users:
        dct = u.symTable()
        lst.append(dct)

    return render_template('index.html',
                            title='Home',
                            user=user,
                            posts=lst)

  
@app.route('/posts/')
def get_posts():
    users = models.User.query.all()
    #return jsonify( {'posts': [ post.to_json() for post in posts] } )
    return jsonify(users[0].to_json())
