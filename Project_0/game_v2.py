"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np
import math

def random_predict(number:int=1) -> int:
    """Рандомно угадываем число в диапазоне от 1 до 100

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0

    while True:
        count += 1
        predict_number = np.random.randint(1, 101) # предполагаемое число
        if number == predict_number:
            break # выход из цикла, если угадали
    return(count)

def binary_predict(number: int = 1) -> int:
    """Бинарный поиск числа в интервале от 1 до 100.

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    
    """При бинарном поиске искомый ключ сравнивается с ключом среднего элемента в массиве. 
       Если они равны, то поиск успешен. 
       В противном случае поиск осуществляется аналогично в левой или правой частях массива."""
    
    arr = list(range(1,101))
    low = 0 #индекс левой границы интервала поиска
    high = len(arr)- 1 #индекс правой границы интервала поиска

    count = 0
    while (low <= high):
        count += 1
        mid = math.floor((low + high)/2) #середина интервала поиска
        midVal = arr[mid] #значение элемента в середине интервала поиска

        if midVal < number:
            low = mid + 1
        elif midVal > number:
            high = mid - 1
        else:
            break # выход из цикла, если угадали

    return count;  


def score_game(predict_func) -> int:
    """За какое количество попыток в среднем из 1000 подходов угадывает алгоритм

    Args:
        predict_func ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """

    count_ls = [] # список для сохранения количества попыток
    np.random.seed(1) # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000)) # загадали список чисел

    for number in random_array:
        count_ls.append(predict_func(number))

    score = math.floor(np.mean(count_ls)) # находим среднее количество попыток

    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    return(score)

# RUN
#score_game(random_predict)
#print(random_predict(25))

if __name__ == '__main__':
    #score_game(random_predict)
    score_game(binary_predict)