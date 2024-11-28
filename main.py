#Election validation
from setuptools.command.easy_install import is_sh

country = 'страна'

def get_age():
    while True:
        try:
            age = int(input("Введите возраст кандидата: "))
        except ValueError:
            "Ошибка, некорректное число"
        else:
            return age


def get_citizenship():
    while True:
        try:
            citizenship = str(input("Введите гражданство кандидата: ")).lower()
        except ValueError:
            "Ошибка, некорректный текст"
        else:
            return citizenship


def get_banned_state():
    while True:
        try:
            banned_state = str(input("Кандидат дисквалифицирован? (Да \ Нет): "))
            if banned_state.lower() == "да":
                is_banned = True
            elif banned_state.lower() == "нет":
                is_banned = False
            else:
                raise ValueError
        except ValueError:
            "Ошибка, введите Да или Нет"
        else:
            return is_banned


def main():
    while True:
        print("Проверка на допуск кандидата к голосованию на выборах:\n")
        age = get_age()
        citizenship = get_citizenship()
        is_banned = get_banned_state()
        print("Может голосовать\n" if age >= 18 and citizenship == country and not is_banned else "Не может голосовать\n")

main()