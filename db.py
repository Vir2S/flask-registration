from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
	""" Create user table"""

	__tablename__ = 'User'
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(80), unique=True)
	password = db.Column(db.String(80))
	email = db.Column(db.String, nullable=False)

	def __init__(self, username, password, email):
		self.username = username
		self.password = password
		self.email = email
