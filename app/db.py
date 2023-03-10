from app.user import User

class Database():

    userlist: list = []

    def __init__(self):
        pass

    def add_user(self, username: str, password: str):
        if len(username) >= 3 and len(username) <= 20 and username.isascii():
            new_user = User(username, password, None)
            self.userlist.append(new_user)
        else:
            print('Username is not valid. Username must be at least 3 characters and max. 20 characters and ascii.')
            pass

    def delete_user(self, username: str, password_hash: str):
        pass

    def change_password(self, username: str, new_password: str):
        pass

