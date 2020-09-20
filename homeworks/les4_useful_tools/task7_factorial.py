"""
7. Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение.
При вызове функции должен создаваться объект-генератор.
Функция должна вызываться следующим образом: for el in fact(n).
Функция отвечает за получение факториала числа,
а в цикле необходимо выводить только первые n чисел, начиная с 1! и до n!.

Подсказка: факториал числа n — произведение чисел от 1 до n.
Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.
"""
import math
from typing import Generator


def my_factorial(num: int) -> Generator[int, None, None]:
    """
    Return next value of a factorial of a provided number.
    :param num: int
    :return: Generator[int, None, None]
    """
    for i in range(num + 1):
        yield math.factorial(i)


if __name__ == "__main__":
    for val, fact in enumerate(my_factorial(10)):
        if val != 0:
            print(f"{val}! = {fact}")
