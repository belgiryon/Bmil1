import enum  # Импортируем модуль enum
import random  # Импортируем модуль random
import string  # Импортируем модуль string

class Alphabet(enum.Enum):
    lower_case = string.ascii_lowercase  # Алфавит с маленькими буквами
    upper_case = string.ascii_uppercase  # Алфавит с заглавными буквами
    punctuation = string.punctuation    # Алфавит с знаками пунктуации
    digits = string.digits              # Алфавит с цифрами

def error_processing(length):
    # Проверяем, является ли введенная длина числом
    if not length.isdigit():
        return "Ошибка ввода длины пароля. Длина пароля - натуральное число"
    # Проверяем, является ли введенная длина менее 8
    if int(length) < 8:
        return "Слишком короткий пароль"
    # Проверяем, является ли введенная длина более 127
    if int(length) > 127:
        return "Слишком длинный пароль"
    return 0

def sets(repeat, alphabet, type):
    print(type)
    # Если нет повторяющихся символов и есть тип алфавита
    if not set(repeat) & set(Alphabet.lower_case.value) and set(alphabet) & set(type):
        # Выбираем случайный символ из указанного алфавита
        pas = random.SystemRandom().choice(list(set(alphabet) & set(type)))
        return pas
    else:
        return -1

def generate(length, alphabet):
    length = int(length)
    repeat = []
    password = ""
    i = 0
    # Проходим по длине пароля
    for _ in range(length):
        pas = -1
        if i == 4:
            i = 0
        while pas == -1 and i <= 3:
            # Выбираем символ из указанного типа
            pas = sets(repeat, alphabet, list(Alphabet)[i].value)
            i += 1
        if pas == -1:
            # Если подходящего символа нет, выбираем случайный символ
            pas = random.SystemRandom().choice(alphabet)
        password += pas
        repeat.append(pas)
    return password
