import random

def generate_email():
    return f"{random.randint(100000, 999999)}@yandex.ru"


def generate_password():
    return f"{random.randint(100000, 999999)}"