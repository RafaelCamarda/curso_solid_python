class Repo():

    def __init__(self, id, name, stars):
        self._id = id
        self._name = name
        self._stars = stars

    def __str__(self):
        return f'id: {self._id} name: {self._name}, stars: {self._stars}'
