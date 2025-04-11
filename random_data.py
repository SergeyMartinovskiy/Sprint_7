from faker import Faker

faker = Faker()


def gen_fake_login_courier(length=7):
    login = faker.user_name()
    return login[:length]

def gen_fake_first_name(length=6):
    first_name = faker.name()
    return first_name[:length]

def gen_fake_password(length=4):
    password = faker.password(length=4)
    return password[:length]
