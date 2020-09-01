class User():
    def __init__(self, username, email):
        self._username = username
        self._email = email

    def work(self):
        raise NotImplementedError
