from enum import Enum


class WbException(AssertionError):
    ...


class User:
    def __init__(self, login, password):
        self.login = login
        self.password = password


class UserData(Enum):
    trial_tariff = User('', '')
    paid_tariff = User('', '')


month = {
    1: 'Января',
    2: 'Февраля',
    3: 'Марта',
    4: 'Апреля',
    5: 'Мая',
    6: 'Июня',
    7: 'Июля',
    8: 'Августа',
    9: 'Сентября',
    10: 'Октября',
    11: 'Ноября',
    12: 'Декабря'
}
