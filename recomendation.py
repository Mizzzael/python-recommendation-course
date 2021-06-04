from models.users import User
from models.movies import Movie
from math import sqrt
from recomendation_utils import get_similaris_euclideano, get_weight


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
djeeta = User(name='Djeeta', age=22, email='djeeta@yande.re', movies=getMovies([5.0, 2.2, 3.0, 3.0, 1.8]))
zayon = User(name='Zayon', age=25, email='zayon@yande.re', movies=getMovies([None, 3.2, None, 3.4, 2.0]))

list_users = [metera, rosetta, zooey, djeeta, zayon]
list_comparation = list()

for user in list_users:
    for user_to_compare in list_users:
        if user != user_to_compare:
            x = list()
            y = list()
            for (X,Y) in zip(list(user.movies.values()), list(user_to_compare.movies.values())):
                if X.rate == None or Y.rate == None: continue
                x.append(float(X.rate))
                y.append(float(Y.rate))
            user.similares.update({user_to_compare.name: get_similaris_euclideano([x, y])})

list_rate_weight = dict()
list_rate_sims = dict()
for (key, movie) in zip(zayon.movies.keys(), zayon.movies.values()):
    if movie.rate == None:
        list_movie_rates = list()
        list_movie_sims = list()
        similares = 0.0
        for user in list_users:
            if user == zayon: continue
            similares = zayon.similares[user.name]
            if user.movies[key].rate != None:
                list_movie_rates.append(user.movies[key].rate)
                list_movie_sims.append(zayon.similares[user.name])
        list_rate_weight.update({
            key: get_weight(similares, list_movie_rates)
        })
        list_rate_sims.update({
            key: sum(list_movie_sims)
        })

recommendation_rate = dict()
for (key, weight) in zip(list_rate_weight.keys(), list_rate_weight.values()):
    recommendation_rate.update({
        key: (float(weight) - float(list_rate_sims[key]))
    })

media_rate = list(filter(lambda v: v.rate != None, list(zayon.movies.values())))
media = sum([media.rate for media in media_rate])/len(media_rate)

for (key, values) in zip(recommendation_rate.keys(), recommendation_rate.values()):
    if values >= media:
        print(key)
