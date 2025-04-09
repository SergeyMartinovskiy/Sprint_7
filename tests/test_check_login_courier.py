import allure
import pytest
import requests
import random_data
import data
from urls import Urls


class TestCheckLoginCourier:
    @allure.title('Тест на успешную авторизацию под своим логином и паролем')
    def test_login_courier_with_true_data(self):
        login = random_data.gen_fake_login_courier()
        password = random_data.gen_fake_password()
        firstname = random_data.gen_fake_first_name()

        payload = {
            'login': login,
            'password': password,
            'firstname': firstname
            }

        response = requests.post(Urls.URL_MAKE_COURIER, data=payload)
        assert response.status_code == 201
        login_payload = {
            'login': login,
            'password': password,
            }
        response_login = requests.post(Urls.URL_LOGIN_COURIER, data=login_payload)
        assert response_login.status_code == 200
        assert 'id' in response_login.text



    @allure.title('Проверка получения ошибки "Недостаточно данных для входа" '
                  'при передачи в теле запроса пустого поля')
    @pytest.mark.parametrize('empty_field',
                             [data.empty_login_field, data.empty_password_field])
    def test_login_courier_without_one_required_field(self, empty_field):
        response = requests.post(Urls.URL_LOGIN_COURIER, data=empty_field)
        assert response.status_code == 400
        response_json = response.json()
        assert response_json.get('message') == 'Недостаточно данных для входа'



    @allure.title('Проверка получения ошибки "Учетная запись не найдена" '
                  'при передачи в теле запроса неправильных данных полей логина или пароля')
    @pytest.mark.parametrize('incorrectly_filled_in_fields',
                             [data.data_with_incorrect_login, data.data_with_incorrect_password])
    def test_login_courier_with_incorrect_loginor_password(self, incorrectly_filled_in_fields):
        response = requests.post(Urls.URL_LOGIN_COURIER, data=incorrectly_filled_in_fields)
        assert response.status_code == 404
        response_json = response.json()
        assert response_json.get('message') == 'Учетная запись не найдена'




