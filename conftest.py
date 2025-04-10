import allure
import pytest
import requests
from urls import Urls
from random_data import gen_fake_login_courier, gen_fake_password, gen_fake_first_name



@allure.title('Создание курьера. Болванка')
@pytest.fixture(scope='function')
def create_courier():
    payload = {
        'login': gen_fake_login_courier(),
        'password': gen_fake_password(),
        'firstname': gen_fake_first_name()
    }
    response = requests.post(Urls.URL_MAKE_COURIER, data=payload)

    login_payload = payload.copy()
    login_payload.pop('firstname', None)

    id_courier = requests.post(Urls.URL_LOGIN_COURIER, json = login_payload).json().get('id')
    yield response
    requests.delete(Urls.URL_DELETE_COURIER + '/' + str(id_courier))

