"""
4. Программа принимает действительное положительное число x и целое отрицательное число y.
Необходимо выполнить возведение числа x в степень y.
Задание необходимо реализовать в виде функции my_func(x, y).
При решении задания необходимо обойтись без встроенной функции возведения числа в степень.

Подсказка: попробуйте решить задачу двумя способами.
Первый — возведение в степень с помощью оператора **.
Второй — более сложная реализация без оператора **, предусматривающая использование цикла.
"""
from typing import Union


def my_abs(num: Union[float, int]) -> Union[float, int]:
    """
    Return the absolute value of a number.
    :param num: Union[float, int]
    :return: Union[float, int]
    """
    return num if num >= 0 else -num


def my_power(x: Union[int, float], y: int):
    """
    Raising x to the power of y.
    :param x: Union[int, float]
    :param y: int. May be negative
    """
    # First variant via '**'
    print("Result using '**': x ** y =", x ** y)

    # Second variant via loop
    result = 1
    for i in range(my_abs(y)):
        if y > 0:
            result *= x
        else:
            result /= x
    print("Result using loop: x ** y =", result)


if __name__ == "__main__":
    my_power(0.2, -9)
