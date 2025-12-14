# Анатолий Шеповалов, 38-я когорта — Финальный проект. Инженер по тестированию плюс
import requests

from configuration import URL_SERVICE, CREATE_ORDER_PATH, GET_ORDER_BY_TRACK_PATH
from data import order_body

def test_get_order_by_track_returns_200():
    create_response = requests.post(
        URL_SERVICE + CREATE_ORDER_PATH,
        json=order_body
    )
    track = create_response.json().get("track")

    response = requests.get(
        URL_SERVICE + GET_ORDER_BY_TRACK_PATH,
        params={"t": track}
    )

    assert response.status_code == 200