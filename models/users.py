from models.movies import Movie

class User:

    def __init__(self, name: str, email: str, age: int, movies: dict):
        self.name = name
        self.email = email
        self.age = age
        self.movies = movies
        self.similares = list()

    def __str__(self):
        return self.name

    def sort_similares(self):
        values = [item[1] for item in self.similares]
        values.sort()
        new_similares_list = list()
        for value in values:
            for item in self.similares:
                if item[1] == value:
                    new_similares_list.append(item)
                    break
        new_similares_list.reverse()
        self.similares = new_similares_list
