from models.users import User
from models.movies import Movie
from math import sqrt


def getMovies(rates):
    return {
    "Kizunomogatari": Movie(name="Kizunomogatari", category='eichi', rate=rates[0]),
    "Gall Force": Movie(name="Gall Force", category='sci-fy', rate=rates[1]),
    "Hellow World": Movie(name="Hellow World", category='sci-fy', rate=rates[2]),
    "High School DxD": Movie(name="High School DxD", category='eichi', rate=rates[3]),
    "New Genesis Evangelion": Movie(name="New Genesis Evangelion", category='sci-fy', rate=rates[4]),
 }


metera = User(name='Metera', age=25, email='metera@yande.re', movies=getMovies([2.1, 4.1, 2.1, 5.0, 1.1]))
rosetta = User(name='Rosetta', age=26, email='rosetta@yande.re', movies=getMovies([4.1, 3.2, 5.0, 5.0, 4.0]))
zooey = User(name='Zooey', age=24, email='zooey@yande.re', movies=getMovies([3.1, 2.2, 1.0, 4.0, 2.5]))
djeeta = User(name='Djeeta', age=22, email='djeeta@yande.re', movies=getMovies([5.0, 1.2, 3.0, 2.0, 1.5]))
zayon = User(name='Zayon', age=25, email='zayon@yande.re', movies=getMovies([None, 3.2, None, 3.4, 2.0]))

list_users = [metera, rosetta, zooey, djeeta, zayon]
list_comparation = list()

# for user in list_users:
#     rate_movies = list()
#     for movie in user.movies.values():
#         zayon_movie_rate = zayon.movies[movie.name].rate
#         if zayon_movie_rate:
#             rate_movies.append((zayon_movie_rate - movie.rate)**2)
#
#     list_comparation.append([user.name, 1/(1+sqrt(sum(rate_movies)))])
#
# min_rate_range = max([item[1] for item in list_comparation])
# for item in list_comparation:
#     if item[1] == min_rate_range:
#         print(item[0], item[1])
#         break

for user in list_users:
    for user_to_compare in list_users:
        if user != user_to_compare:
            rate_movies = list()
            for movie in user.movies.values():
                other_user_movie_rate = user_to_compare.movies[movie.name].rate
                if other_user_movie_rate and movie.rate:
                    rate_movies.append((other_user_movie_rate - movie.rate)**2)
            user.similares.append([user_to_compare.name, (1 / (1 + sqrt(sum(rate_movies))))])
    user.sort_similares()

print(zayon.similares)
print(djeeta.similares)
print(metera.similares)
print(zooey.similares)
print(rosetta.similares)