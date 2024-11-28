# ДЗ: Логические выражения и условия


def get_age():
    while True:
        try:
            age = int(input("Введите возраст кандидата: "))
        except ValueError:
            print("Ошибка, некорректное число")
        else:
            return age


def get_citizenship():
    while True:
        try:
            citizenship = str(input("Имеется ли у кандидата гражданство? (Да \ Нет): ")).lower()
            if citizenship == "да":
                is_citizen = True
            elif citizenship == "нет":
                is_citizen = False
            else:
                raise ValueError
        except ValueError:
            print("Ошибка, введите Да или Нет")
        else:
            return is_citizen


def get_banned_state():
    while True:
        try:
            banned_state = str(input("Кандидат дисквалифицирован? (Да \ Нет): ")).lower()
            if banned_state == "да":
                is_banned = True
            elif banned_state == "нет":
                is_banned = False
            else:
                raise ValueError
        except ValueError:
            print("Ошибка, введите Да или Нет")
        else:
            return is_banned


def main():
    while True:
        print("Проверка на допуск кандидата к голосованию на выборах:\n")
        age = get_age()
        is_citizen = get_citizenship()
        is_banned = get_banned_state()
        print(
            "Может голосовать\n" if age >= 18 and is_citizen and not is_banned else "Не может голосовать\n")


main()
