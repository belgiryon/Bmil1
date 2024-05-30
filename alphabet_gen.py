import enum # Модуль для создания перечислений (enum).
import random #Модуль для генерации случайных чисел.
import string #Модуль для работы с строками.


class Alphabet(enum.Enum): # это перечисление (enum), в котором определены четыре типа символов:

    lower_case = string.ascii_lowercase #Все строчные буквы латинского алфавита (abcdefghijklmnopqrstuvwxyz).
    upper_case = string.ascii_uppercase #Все заглавные буквы латинского алфавита (ABCDEFGHIJKLMNOPQRSTUVWXYZ).
    punctuation = string.punctuation #Все символы пунктуации (!"#$%&'()*+,-./:;<=>?@[\]^_{|}~`).
    digits = string.digits # Все цифры (0123456789).


def error_processing(length): #проверяет корректность введенного значения длины алфавита
    if not length.isdigit(): # не является числом, возвращается сообщение об ошибке.
        return "Ошибка ввода длины алфавита. Длина алфавита - натуральное число"
    if int(length) < 0 or int(length) > 94: #меньше 0 или больше 94 (максимальное количество уникальных символов в алфавите), возвращается сообщение об ошибке.
        return "Неверная длина алфавита"
    return 0


def generate(length): # создает случайный алфавит заданной длины:
    length = int(length)
    alphabet = '' #для хранения уже добавленных символов.
    repeat = [] # для хранения уже добавленных символов.
    i = 0

    while i < length:
        type_of_elem = random.SystemRandom().choice(list(Alphabet)) # Выбирается случайный тип символа из перечисления Alphabet (например, строчные буквы, заглавные буквы и т.д.).
        elem = random.choice(type_of_elem.value) # Выбирается случайный символ из выбранного типа.
        if elem not in repeat: # Проверяем, что символ еще не добавлен в алфавит
            alphabet += elem # Добавляем символ к алфавиту
            repeat.append(elem)  # Добавляем символ в список уже добавленных
            i += 1 # Увеличиваем счетчик добавленных символов
    return alphabet # Возвращаем сгенерированный алфавит