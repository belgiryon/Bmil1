import time

import matplotlib.pyplot as plt
import alphabet_gen
import password_gen
from speed import speed_array, update_time

# Функция главного меню
def main_menu():
    print("1. Создать Пароль")
    print("2. Аутентификация")
    print("0. Выход")
    return input("Ваш выбор: ")

# Функция для генерации пароля
def generate_password():
    alp_get = input("Введите длину алфавита: ")
    passw_get = input("Введите длину пароля: ")

    al = alphabet_gen.error_processing(alp_get) # Проверка длины алфавита на ошибки
    pssw = password_gen.error_processing(passw_get)  # Проверка длины пароля на ошибки

    if al != 0:
        print(f"Ошибка: {al}")
    if pssw != 0:
        print(f"Ошибка: {pssw}")

    if al == 0 and pssw == 0:
        res_alphabet = alphabet_gen.generate(alp_get) # Генерация алфавита
        pas = password_gen.generate(passw_get, res_alphabet) # Генерация пароля с использованием сгенерированного алфавита
        print(f"Сгенерированный Пароль: {pas}")

# Функция для построения графика
def plot_graph(start_times):
    intervals = speed_array(start_times)

    plt.figure(figsize=(5, 5), dpi=100)
    plt.plot(intervals)
    plt.title("Скорость Нажатий")
    plt.xlabel("Количество Нажатий")
    plt.ylabel("Время (секунды)")
    plt.show()

# Функция для аутентификации
def auth():
    start_times = []
    print("Введите пароль (ваши нажатия будут записаны):")

    password = input("Пароль: ")

    for char in password:
        start_times.append(update_time())# Запись времени каждого нажатия клавиши
        # Симуляция задержки при наборе текста, удалить при реальном использовании
        time.sleep(0.5)

    print("Время ввода пароля записано.")

    while True:
        print("1. Просмотр Графика")
        print("0. Вернуться в Главное Меню")
        choice = input("Ваш выбор: ")

        if choice == "1":
            plot_graph(start_times)
        elif choice == "0":
            break
        else:
            print("Неверный выбор, попробуйте снова.")

def main():
    while True:
        choice = main_menu()

        if choice == "1":
            generate_password() # Вызов функции генерации пароля
        elif choice == "2":
            auth() # Вызов функции аутентификации
        elif choice == "0":
            print("Выход...")
            break # Завершение программы
        else:
            print("Неверный выбор, попробуйте снова.")


if __name__ == "__main__":
    main() # Запуск программы
