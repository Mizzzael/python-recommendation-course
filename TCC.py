from data_base_test import user
from recomendation_utils import recommendation, set_langs_by_users_rates, items_similares, recommendationsByItem

user_lists = {k: v for k, v in filter(lambda item: item[0] != 'Vaseraga',user.items())}

recommendation(user['Vaseraga'], user_lists)
langs = set_langs_by_users_rates(user)
print(recommendationsByItem(user, items_similares(langs), 'Vaseraga'))