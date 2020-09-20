"""
6. Реализовать два небольших скрипта:
а) итератор, генерирующий целые числа, начиная с указанного,

Подсказка: использовать функцию count() и cycle() модуля itertools.
Обратите внимание, что создаваемый цикл не должен быть бесконечным.
Необходимо предусмотреть условие его завершения.

Например, выводим целые числа, начиная с 3, а при достижении числа 10 завершаем цикл.
"""
import itertools
import sys
from typing import Generator


def my_gen_of_int_nums(start_value: int, stop_value: int) -> Generator[int, None, None]:
    """
    Generate integers from specified start value till a specified stop value
    :param start_value: int
    :param stop_value: int
    :return: Generator[int, None, None]
    """
    for num in itertools.count(start_value):
        if num >= stop_value + 1:
            break
        else:
            yield num


try:
    _, num_to_start, num_to_stop = sys.argv
    num_to_start, num_to_stop = int(num_to_start), int(num_to_stop)
    if num_to_start > num_to_stop:
        print("Start value should be less than stop value.")
        exit(0)
except ValueError as e:
    if str(e)[:-20] == "not enough values to unpack" or str(e)[:-13] == "too many values to unpack":
        print("Provide exactly 2 arguments in the following order: Number to start with, Number to stop at")
    else:
        print("Arguments should be integers!")
    exit(0)


if __name__ == "__main__":
    print(list(my_gen_of_int_nums(num_to_start, num_to_stop)))
