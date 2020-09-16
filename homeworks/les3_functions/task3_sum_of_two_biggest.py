"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
"""
from typing import Union


def my_func(x: Union[int, float], y: Union[int, float], z: Union[int, float]) -> Union[int, float]:
    """
    Return sum of two biggest arguments.
    :param x: Union[int, float]
    :param y: Union[int, float]
    :param z: Union[int, float]
    :return: Union[int, float]
    """
    nums_to_compare = [x, y, z]
    for i in range(len(nums_to_compare)):
        biggest_idx = i
        for j in range(i + 1, len(nums_to_compare)):
            if nums_to_compare[j] > nums_to_compare[biggest_idx]:
                biggest_idx = j
        nums_to_compare[i], nums_to_compare[biggest_idx] = nums_to_compare[biggest_idx], nums_to_compare[i]

    return nums_to_compare[0] + nums_to_compare[1]


if __name__ == "__main__":
    print(my_func(0.5, 0, 1))
