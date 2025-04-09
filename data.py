import random_data
valid_login = 'Sergey'
empty_login = ""
empty_password = ""

invalid_password = 'password'
invalid_login = 'МартинMartin'

empty_login_field = {
            'login': '',
            'password': random_data.gen_fake_password()
            }

empty_password_field = {
            'login': random_data.gen_fake_login_courier(),
            'password': ''
            }

data_with_incorrect_login = {
            'login': invalid_login,
            'password': random_data.gen_fake_password()
            }

data_with_incorrect_password = {
            'login': random_data.gen_fake_login_courier(),
            'password': 'invalid_password'
            }

class MakeOrder:
    data_order_with_only_grey_scooter = {
    "firstName": "Иван",
    "lastName": "Иванов",
    "address": "Ивановская ул., д. 13",
    "metroStation": 4,
    "phone": "+79001002030",
    "rentTime": 5,
    "deliveryDate": "2025-04-20",
    "comment": "Покатаемся",
    "color": [
        "GREY"
    ]
}

    data_order_with_only_black_scooter = {
    "firstName": "Петр",
    "lastName": "Петров",
    "address": "Петровская ул, д. 17",
    "metroStation": 4,
    "phone": "+79001003040",
    "rentTime": 5,
    "deliveryDate": "2025-04-21",
    "comment": "Прокатимся",
    "color": [
        "BLACK"
    ]
}
    data_order_with_black_and_grey_scooter = {
    "firstName": "Сергей",
    "lastName": "Сергеев",
    "address": "Сергеевский пр., д. 7",
    "metroStation": 4,
    "phone": "+79001005060",
    "rentTime": 5,
    "deliveryDate": "2025-04-22",
    "comment": "Полетели",
    "color": [
        "BLACK", "GREY"
    ]
}
    data_order_without_scooter = {
    "firstName": "Николай",
    "lastName": "Николаев",
    "address": "Николаевский пр., д. 100",
    "metroStation": 4,
    "phone": "+79001001010",
    "rentTime": 5,
    "deliveryDate": "2025-04-24",
    "comment": "Полетели",
    "color": []
}
