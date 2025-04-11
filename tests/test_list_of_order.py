import allure
import requests
from urls import Urls



class TestGetResponseListOfOrder:
    @allure.title('Проверка получения списка заказов в теле ответа')
    def test_get_list_of_orders_in_body(self):
        headers = {"Content-type": "application/json"}
        response = requests.get(Urls.URL_GET_ORDER, headers=headers)
        assert response.status_code == 200
        assert isinstance(response.json()['orders'], list)