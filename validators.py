from validate_email import validate_email


def check_username_validation(username):
    return False if len(username) <= 4 else True


def check_email_validation(email):
    return validate_email(email)


def check_password_validation(password):
    return False if len(password) <= 6 else True
