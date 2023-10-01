# Михаил Кузнецов, 8а когорта — Финальный проект. Инженер по тестированию плюс
import configuration
import requests
import data

# Создание заказа
def post_new_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
                         json=body,
                         headers=data.headers)
response_1 = post_new_order(data.order_body)

# Сохранение и получение заказа по трек-номеру
def get_new_order(track):
    return requests.get(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
                        params=track)
response_2 = get_new_order(data.order_body)


