from flask_sqlalchemy import SQLAlchemy
from flask import Flask, url_for, render_template, request, redirect, session
from werkzeug.security import generate_password_hash, check_password_hash

from config import BaseConfig
from email_validator import *


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = BaseConfig.DB_PATH
app.config['SECRET_KEY'] = BaseConfig.SECRET_KEY
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class User(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    password = db.Column(db.String(80))
    email = db.Column(db.String, nullable=False)

    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/register', methods=['GET', 'POST'])
def register():

    if request.method == 'POST':

        username = request.form['username']
        print('username', username)
        user = User.query.filter_by(username=username).first()

        if user is not None:

            return 'User exists!'

        email = request.form['email']

        if check_email_validation(email):

            password = generate_password_hash(request.form['password'])

            new_user = User(
                username=username,
                password=password,
                email=email
            )

            db.session.add(new_user)
            db.session.commit()

            return redirect(url_for('index'))

        else:

            return 'email is not valid.'

    return render_template('register.html')


if __name__ == '__main__':
    app.debug = True
    db.create_all()
    app.run(host='127.0.0.1')
