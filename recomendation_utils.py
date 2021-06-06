from math import sqrt

def get_similaris_euclideano(list_of_distances):
    init_list = list_of_distances[0]
    new_list_of_distances = list()
    for (index, item) in enumerate(init_list):
        item_value = float(item)
        for list_to_compare in list_of_distances[1:]:
            item_value = float(item_value) - float(list_to_compare[index])
        new_list_of_distances.append(item_value)
    return (1 / (1 + sqrt(sum([distances**2 for distances in new_list_of_distances]))))


def get_weight(sim, values):
    return sum([value*sim for value in values])

def similares(user, ranked_users):
    similarity_dict = dict()
    for ranked_user in list(ranked_users.items()):
        usr, items = ranked_user
        items_filter_equality = {k: v for k, v in filter(lambda item: user[item[0]] != None, items.items())}
        items_to_compare = {k: v for k, v in filter(lambda item: item[1] != None, user.items())}
        similarity_dict.update({
            usr: get_similaris_euclideano([list(items_to_compare.values()), list(items_filter_equality.values())])
        })
    similarity_dict = {k: v for k, v in sorted(similarity_dict.items(), key=lambda item: item[1])}
    return similarity_dict


def set_rates(user, ranked_users, similarity):
    user_recommentation_rate_dict = {k:v for k, v in filter(lambda item: item[1] == None, user.items())}
    rates = dict()
    for k in user_recommentation_rate_dict.keys():
        weight = 0.0
        rate = 0.0
        for k_ru, v in ranked_users.items():
            if v[k] != None:
                weight += similarity[k_ru]
                rate += similarity[k_ru] * v[k]
        rates.update({k: rate - weight})
    return rates



def recommendation(user, ranked_users):
    similarity = similares(user, ranked_users)
    rates = set_rates(user, ranked_users, similarity)
    rates_of_user = [rate for rate in filter(lambda item: item != None, user.values())]
    rate_media = sum(rates_of_user) / len(rates_of_user)
    for key, rate in rates.items():
        if rate >= rate_media:
            print(f"{key} é recomendável")
        else:
            print(f"A nota de {key}, é {'%.2f' % rate} não recomendável!")
    print(f"Media {'%.2f' % rate_media}")

def set_langs_by_users_rates(users):
    keys = list(users.values())[0].keys()
    langs_dict = dict()

    for key in list(keys):
        langs_dict.update({
            key: {k: v[key] or 0 for k, v in users.items()}
        })
    return langs_dict

def items_similares(items):
    response_dict = dict()
    for k, item in items.items():
        list_compare = {k: v for k, v in filter(lambda item: item[0] != k, items.items())}
        response_dict.update({
            k: similares(item, list_compare)
        })

    return response_dict

def recommendationsByItem(baseItems, sims, user):
    userRate = baseItems[user]
    rate = dict()
    ttSims = {}
    for key, user_rate in userRate.items():
        for simKey, sim in sims[key].items():
            if userRate[simKey] != None or userRate[key] == None: continue
            rate.update({
                simKey: sim * userRate[key]
            })
            ttSims.setdefault(simKey, 0)
            ttSims[simKey] += sim
    r = {i: (s / ttSims[i]) for i, s in rate.items()}
    return r