# Анатолий Шеповалов, 38-я когорта — Финальный проект. Инженер по тестированию плюс
import requests

from configuration import URL_SERVICE, CREATE_ORDER_PATH
from data import order_body

def test_create_order_returns_201_and_track():
    response = requests.post(
        URL_SERVICE + CREATE_ORDER_PATH,
        json=order_body
    )

    assert response.status_code == 201
    assert response.json().get("track") is not None