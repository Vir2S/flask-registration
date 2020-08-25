from validate_email import validate_email


def check_email_validation(email):

	print('email', email)

	valid = validate_email(email)
	print('valid', valid)
	return valid
