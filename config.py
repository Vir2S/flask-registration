class BaseConfig():
	"""Base configuration."""
	# main config
	SECRET_KEY = 'my_secret_key'
	SECURITY_PASSWORD_SALT = 'my_password_salt'
	DB_PATH = 'sqlite:///database.db'
