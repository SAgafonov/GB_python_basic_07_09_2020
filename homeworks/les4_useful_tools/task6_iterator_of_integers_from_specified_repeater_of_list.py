"""
6. Реализовать два небольших скрипта:
а) итератор, генерирующий целые числа, начиная с указанного,
б) итератор, повторяющий элементы некоторого списка, определенного заранее.

Подсказка: использовать функцию count() и cycle() модуля itertools.
Обратите внимание, что создаваемый цикл не должен быть бесконечным.
Необходимо предусмотреть условие его завершения.

Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10 завершаем цикл.
Во втором также необходимо предусмотреть условие, при котором повторение элементов списка будет прекращено.
"""
import itertools
from typing import Generator, Any


def my_gen_of_int_nums(start_value: int, stop_value: int) -> Generator[int, None, None]:
    """
    Generate integers from specified start value till a specified stop value
    :param start_value: int
    :param stop_value: int
    :return: Generator[int, None, None]
    """
    if start_value <= stop_value:
        for num in itertools.count(start_value):
            if num >= stop_value + 1:
                break
            else:
                yield num
    else:
        print("Start value should be less than stop value.\n")


def my_repeater_of_list_items(num_of_repeats: int, list_to_repeat: list) -> Generator[Any, None, None]:
    """
    Repeat elements of provided list for a specified number of times.
    :param num_of_repeats: int
    :param list_to_repeat: list
    :return: Generator[Any, None, None]
    """
    for el in itertools.cycle(list_to_repeat):
        if num_of_repeats == 0:
            break
        else:
            yield el
            num_of_repeats -= 1


if __name__ == "__main__":
    print(list(my_gen_of_int_nums(-7, 9)))

    init_list = [1, "2we", 2.4, "wer", [2, 4]]
    print(list(my_repeater_of_list_items(7, init_list)))
