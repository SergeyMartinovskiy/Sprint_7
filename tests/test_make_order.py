import allure
import requests
import pytest
import json
from data import MakeOrder
from urls import Urls

class TestMakeOrder:
    @allure.title('Проверка создания заказа')
    @allure.description('Проверка заказа с вариантами выбора самоката - Черный, '
                        'Серый, Оба сразу, или без указания такового')
    @pytest.mark.parametrize('var_data',
                             [MakeOrder.data_order_with_only_grey_scooter,
                             MakeOrder.data_order_with_only_black_scooter,
                             MakeOrder.data_order_with_black_and_grey_scooter,
                             MakeOrder.data_order_without_scooter]
                             )
    def test_make_order(self,var_data):
        var_data_string = json.dumps(var_data)
        headers = {"Content-type": "application/json"}
        response = requests.post(Urls.URL_GET_ORDER, data=var_data_string, headers=headers)
        assert response.status_code == 201
        response_json = response.json()
        assert 'track' in response_json

