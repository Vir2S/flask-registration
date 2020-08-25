from validate_email import validate_email


def check_email_validation(email):
	valid = validate_email(email)
	return valid
