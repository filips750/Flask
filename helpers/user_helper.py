from DB_wrappers.models import Users
import re


def verify_profile_permission(email, password):
    user = Users.query.filter_by(email = email, hashed_pwd = password).first()
    if user:
        return True
    return False

def verify_email(email):
    email_validate_pattern = r"^\S+@\S+\.\S+$"
    return re.match(email_validate_pattern, email) 


verify_email("filips750@gmail.com")