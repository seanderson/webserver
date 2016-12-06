# webserver
(The sister android app is at https://github.com/seanderson/TodoWeb)

This builds a todo app on the web backed by a postgres database.  The
simple idea is to authenticate a user and then associate each
registered user with exactly one task.

The various stages are handled as commits:

1. Initial commit: Get and Post from Todo server with database.  

1. Added authentication this is the part I do here.

1. Added JSON to interact with phone app.

1. Install on Heroku and test with the phone app.

I have reinterpreted Miguel Grinberg's discussion of Flask-based web
programming.  This simplifies his presentation, aiming for those
interested in a basic authenticated application with a supporting
Postgres database.  The final product is runnable on Heroku.

## Installation

Set up flask
`virtualenv flask`

Activate your flask microenvironment.
`source flask/bin/activate`

Set up the requirements.
`pip install -r requirements.txt`

You need to have a postgres database called tododb. You can use postgres tool (somewhere like
`/Applications/Postgres.app/Contents/Versions/latest/bin/`
to `dropdb` and `createdb` as needed.  I don't provide any updating
code and remove any Grinberg has.

Create the new database
`./db_create.py`

Run the app.
`run.py`

You can create an email/password and the then interact with the
database, freely modifying the association between authorized user
emails and their tasks.  That's all it does!




