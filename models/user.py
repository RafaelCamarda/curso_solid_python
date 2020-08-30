class User():
    def __init__(self, username, email):
        self._username = username
        self._email = email

    @staticmethod
    def members():
        return ["username1", "username2", "team1", "team2"]
