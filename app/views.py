from flask import render_template, flash, redirect, request, url_for
from app import app
from flask import jsonify
from flask_login import login_required, login_user, logout_user


from app import db,models
#from flask.ext.sqlalchemy import SQLAlchemy
#db = SQLAlchemy(app)


from .forms import LoginForm
from .forms import InputForm
from .forms import RegistrationForm
from .models import User

# Code executed for localhost:5000/index route
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html',
                           title='Home')

# Login
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    flash('got to login form')
    if form.validate():
        print "VALID FORM"
    print("FORM ERRORS " + str(form.errors))

    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user)
            flash('login success.')
            return jsonify( {"login" : "true"} ) #redirect(request.args.get('next') or url_for('index'))
        flash('Invalid username or password.')
    flash('not valid on submit, so redering login page')
    return render_template('login.html',form=form)


# register new user
@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.is_submitted():
        print "SUBMITTED FORM"

    if form.validate():
        print "VALID FORM"
    print("FORM ERRORS " + str(form.errors))
    if form.validate_on_submit():
        flash("email " + form.email.data)
        flash("pws " + form.password.data)
        user = User(email=form.email.data,
                    password=form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('You can now login.')
        return redirect('/login')
    flash('rendering register.html')
    return render_template('register.html', form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.')
    return redirect(url_for('index'))

# For testing
@app.route('/secret')
@login_required
def secret():
    return 'Only authenticated users are allowed!'


@app.route('/in',methods=['GET','POST'])
@login_required
def input():
    form = InputForm()
    if form.validate_on_submit(): # True, show users inputs [POST]

        # get appropriate user and update their task
        u = User.query.filter_by(email=form.email.data).first()
        if u is not None:
            u.task = form.task.data
            if form.done.data == True:
                u.done = 'Yes'
            else:
                u.done = 'No'
            db.session.add(u)
            db.session.commit()
            return redirect('/db')
        flash('That user email is not in the database.')
        return render_template('input.html',title='input',form=form)
    else:
        return render_template('input.html',
                           title='input',
                           form=form)
    

# Code executed for localhost:5000/db route
@app.route('/db')
@login_required
def showdb():
    users = User.query.all()
    lst = [ ]
    for u in users:
        dct = u.symTable()
        lst.append(dct)

    return render_template('db.html',
                            title='Database View',
                            posts=lst)

# Testing json form of data  
@app.route('/dbjsn')
@login_required
def get_posts():
    users = models.User.query.all()
    return jsonify( {'tasks': [ user.to_json() for user in users] } )

