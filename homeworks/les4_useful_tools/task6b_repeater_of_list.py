"""
6. Реализовать два небольших скрипта:
б) итератор, повторяющий элементы некоторого списка, определенного заранее.

Подсказка: использовать функцию count() и cycle() модуля itertools.
Обратите внимание, что создаваемый цикл не должен быть бесконечным.
Необходимо предусмотреть условие его завершения.

Необходимо предусмотреть условие, при котором повторение элементов списка будет прекращено.
"""
import itertools
import sys
from typing import Generator, Any


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


try:
    _, num_to_repeat = sys.argv
    num_to_repeat = int(num_to_repeat)
except ValueError as e:
    if str(e)[:-20] == "not enough values to unpack" or str(e)[:-13] == "too many values to unpack":
        print("Provide exactly 1 argument. It should be an integer")
    else:
        print("Arguments should be integers!")
    exit(0)


if __name__ == "__main__":
    init_list = [1, "2we", 2.4, "wer", [2, 4]]
    print(list(my_repeater_of_list_items(num_to_repeat, init_list)))
