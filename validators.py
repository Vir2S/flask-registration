from validate_email import validate_email


def check_username_validation(username):
    if len(username) <= 4:
        return False
    return True


def check_email_validation(email):
    valid = validate_email(email)
    return valid


def check_password_validation(password):
    if len(password) <= 6:
        return False
    return True
