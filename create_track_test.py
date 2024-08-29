# Роман Каракчиев, 20-я когорта — Финальный проект. Инженер по тестированию плюс

# Импортируем модуль sender_stand_request, содержащий функции для отправки HTTP-запросов к API.
import sender_stand_request

# Получение заказа по треку заказа:
def get_order():
    track_number = sender_stand_request.post_new_order()
    return track_number.json() ["track"]

# Проверка, что код ответа равен 200:
def test_track_order():
    track_number = get_order()
    get_response = sender_stand_request.get_order_track(track_number)
    assert get_response.status_code == 200