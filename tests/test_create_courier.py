
import allure
import requests
from random_data import gen_fake_login_courier, gen_fake_first_name, gen_fake_password
from urls import Urls
from data import empty_login, empty_password, valid_login



class TestCreateCourier:
    @allure.title('Проверка на создание курьера, на возврат ответа код 201 и тело ответа "ok:True"')
    def test_valid_create_courier(self):
        payload = {
            'login': gen_fake_login_courier(),
            'password': gen_fake_password(),
            'firstname': gen_fake_first_name()
        }
        response = requests.post(Urls.URL_MAKE_COURIER, data = payload)
        assert response.status_code == 201 and response.json() == {'ok':True}

    @allure.title('Получение ошибки "Этот логин уже используется" '
                  'при повторном создании курьера с имеющимся логином')
    @allure.description("Необходимость заведения бага: ожидаемое сообщение не совпало с реальным."
                        "ОР - 'Этот логин уже используется', "
                        "ФР - 'Этот логин уже используется. Попробуйте другой.'")
    def test_create_courier_with_used_login(self):
        payload = {
            'login': valid_login,
            'password': gen_fake_password(),
            'firstname': gen_fake_first_name()
        }
        response = requests.post(Urls.URL_MAKE_COURIER, data=payload)
        assert response.status_code == 409
        response_json = response.json()
        assert response_json.get('message') == 'Этот логин уже используется'



    @allure.title('Получение ошибки "Недостаточно данных для создания учетной записи"'
                  ' при попытке создать курьера с незаполненным полем Login')
    def test_create_courier_without_login_in_login_field(self):
        payload = {
                'login': empty_login,
                'password': gen_fake_password(),
                'firstname': gen_fake_first_name()
        }
        response_empty_login = requests.post(Urls.URL_MAKE_COURIER, data=payload)
        assert response_empty_login.status_code == 400
        response_json = response_empty_login.json()
        assert response_json.get('message') == 'Недостаточно данных для создания учетной записи'


    @allure.title('Получение ошибки "Недостаточно данных для создания учетной записи" '
                  'при попытке создать курьера с незаполненным полем Password')
    def test_create_courier_without_password_in_password_field(self):
        payload = {
                'login': gen_fake_login_courier(),
                'password': empty_password,
                'firstname': gen_fake_first_name()
        }
        response_empty_password = requests.post(Urls.URL_MAKE_COURIER, data=payload)
        assert response_empty_password.status_code == 400
        response_json = response_empty_password.json()
        assert response_json.get('message') == 'Недостаточно данных для создания учетной записи'
