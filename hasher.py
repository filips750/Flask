import bcrypt


def hasher(password):
    saltimore = b'$2b$12$oa7jv4ptPB6tJqMrqvIheO'
    return bcrypt.hashpw(bytes(password, 'utf-8'), saltimore)
