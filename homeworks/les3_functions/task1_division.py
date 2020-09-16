"""
1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
"""
from typing import Union


def divider(x: Union[int, float], y: Union[int, float]) -> float:
    """
    Divides two numbers.
    :param x: [int, float]
    :param y: [int, float]
    :return: float
    """
    return x / y


def user_input() -> tuple:
    """
    Get user input.
    :return: tuple(float, float)
    """
    while True:
        user_num_x = input("Enter dividend: ")
        user_num_y = input("Enter divisor: ")
        try:
            num_x, num_y = float(user_num_x), float(user_num_y)
            if num_y == 0:
                print("Divisor can't be zero! Try again\n")
                continue
            return num_x, num_y
        except ValueError as e:
            print(f"Got an error: {e}\nYou should provide numbers! Try again\n")


if __name__ == "__main__":
    dividend, divisor = user_input()
    print(divider(dividend, divisor))
