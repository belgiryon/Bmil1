import unittest

import alphabet_gen  # Импортирует модуль генерации алфавита
import password_gen  # Импортирует модуль генерации пароля


class Test(unittest.TestCase):

    def test_password_length(self):
        # Генерирует пароль длиной 33 символа с помощью функции generate
        password = password_gen.generate(33, password_gen.Alphabet.value)
        # Проверяет, что длина сгенерированного пароля равна 33
        self.assertEquals(len(password), 33)

    def test_alphabet_length(self):
        # Генерирует алфавит длиной 22 символа с помощью функции generate
        alphabet = alphabet_gen.generate(22)
        # Проверяет, что длина сгенерированного алфавита равна 22
        self.assertEquals(len(alphabet), 22)

    def test_all_symbols_available(self):
        # Генерирует пароль длиной 22 символа с помощью функции generate
        password = password_gen.generate(22, password_gen.Alphabet.value)
        # Проверяет, что пароль содержит как минимум один символ верхнего регистра,
        # один символ нижнего регистра, одну цифру и состоит только из буквенно-цифровых символов
        self.assertTrue(password.isupper() and password.islower() and password.isdigit() and password.isalnum())
