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

# Cutesexyrobutts = [1.0, 5.1, 4.5, 2.3]
# Ishikey = [4.0, 2.1, 1.0, 5.3]
#
# print(get_similaris_euclideano(list([Cutesexyrobutts, Ishikey])))

# print (get_similaris_euclideano({
#     "Cutesexyrobutts": [1.0, 5.0, 4.5, 2.3],
#     "Ishikey": [4.0, 2.1, 1.0, 5.0],
# }))