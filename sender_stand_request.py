# Импорт настроек из модуля configuration, который содержит параметры конфигурации, такие как URL сервиса
import configuration

# Импорт библиотеки requests для выполнения HTTP-запросов
import requests

# Импорт данных запроса из модуля data, в котором определены заголовки и тело запроса
import data


# POST-запрос на создание нового заказа:
def post_new_order():
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER,
    json = data.order_body)

# GET-запрос на получение заказа по номеру трека:
def get_order_track(track_number):
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER,
                        params = {"t": track_number})