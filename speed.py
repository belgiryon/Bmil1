import time  # Импортируем модуль времени

def update_time():
    return time.time()  # Возвращает текущее время в формате времени Unix

def speed_array(start_times):
    # Функция принимает список начальных времен и вычисляет разницу между соседними элементами
    return [j - i for i, j in zip(start_times[:-1], start_times[1:])]
