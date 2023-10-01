# Михаил Кузнецов, 8а когорта — Финальный проект. Инженер по тестированию плюс
import sender_stand_request
import data

# Автотест
def test_create_order_by_track():
    response_3 = sender_stand_request.post_new_order(data.order_body)
    track = {"t": response_3.json()["track"]}
   
# Получение сведений о заказе по номеру трека
    response_4 = sender_stand_request.get_new_order(track)
    assert response_4.status_code == 200
    order_info = response_4.json()
 
