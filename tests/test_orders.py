# Анатолий Шеповалов, 38-я когорта — Финальный проект. Инженер по тестированию плюс
import requests

from configuration import URL_SERVICE, CREATE_ORDER_PATH, GET_ORDER_BY_TRACK_PATH
from data import order_body

def test_create_order_and_get_by_track():
    create_response = requests.post(
        URL_SERVICE + CREATE_ORDER_PATH,
        json=order_body
    )
    assert create_response.status_code == 201
    track = create_response.json().get("track")
    assert track is not None
    get_response = requests.get(
        URL_SERVICE + GET_ORDER_BY_TRACK_PATH,
        params={"t": track}
    )
    assert get_response.status_code == 200