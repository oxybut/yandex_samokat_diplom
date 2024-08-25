# Роман Каракчиев, 20-я когорта — Финальный проект. Инженер по тестированию плюс

# Импортируем модуль sender_stand_request, содержащий функции для отправки HTTP-запросов к API.
import sender_stand_request

# Импортируем модуль data, в котором определены данные, необходимые для HTTP-запросов.
import data


def get_new_track(order_response):
    return order_response.json().get("track")


data.params_get["t"] = get_new_track(sender_stand_request.order_response)


# Автоматизация теста к API
def positive_assert():
    track_response = sender_stand_request.get_order(data.params_get)
    assert track_response.status_code == 200


def test_order():
    positive_assert()