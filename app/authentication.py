from flask_httpauth import HTTPDigestAuth

auth = HTTPDigestAuth()

users= {
    'mo': '123',
}

@auth.get_password
def get_pw(username):
    if username in users:
        return users.get(username)
    return None