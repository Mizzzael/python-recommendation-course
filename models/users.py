from models.movies import Movie

class User:

    def __init__(self, name: str, email: str, age: int, movies: dict):
        self.name = name
        self.email = email
        self.age = age
        self.movies = movies
        self.similares = dict()
        self.weight = list()

    def __str__(self):
        return self.name
