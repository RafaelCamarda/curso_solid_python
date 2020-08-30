from .user import User


class Manager(User):
    def __init__(self, username, email):
        super().__init__(username, email)

    @staticmethod
    def pay_bill():
        "Paying bill..."

    @staticmethod
    def code():
        pass
