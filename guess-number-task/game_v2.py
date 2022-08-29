"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np


def random_predict(number: int = 1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0

    while True:
        count += 1
        predict_number = np.random.randint(1, 101)  # предполагаемое число
        if number == predict_number:
            break  # выход из цикла если угадали
    return count


def binary_search(arr, number: int = 1) -> int:
    """Binary serach in integer array

    Args:
        arr (_type_): list of int numbers
        number (int, optional): predict number. Defaults to 1.

    Returns:
        int: predicion count
    """
    low = 0
    high = len(arr)- 1

    count = 0
    while (low <= high):
        count += 1
        mid =   int((low + high)/2)
        midVal = arr[mid]

        if midVal < number:
            low = mid + 1
        elif midVal > number:
            high = mid - 1
        else:
            break # выход из цикла если угадали

    return count;  # number not found.


def score_game(random_predict) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    #np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел
    arr = list(range(1,101))
    for number in random_array:
        #count_ls.append(random_predict(number))
        count_ls.append(binary_search(arr,number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score


if __name__ == "__main__":
    # RUN
    score_game(random_predict)