"""
5. Программа запрашивает у пользователя строку чисел, разделенных пробелом.
При нажатии Enter должна выводиться сумма чисел.
Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
Но если вместо числа вводится специальный символ, выполнение программы завершается.
Если специальный символ введен после нескольких чисел,
то вначале нужно добавить сумму этих чисел к полученной ранее сумме
и после этого завершить программу.
"""
from typing import List


def sum_user_numbers():
    """
    Print sum of user's list of numbers.
    """
    repeat = True
    sum_of_numbers = 0
    while repeat:
        user_nums = input("Enter numbers divided by white spaces or 'q' to exit: ")
        temp_list = user_nums.split()
        if 'q' in temp_list:
            repeat = False
            temp_list = temp_list[:temp_list.index('q')]
        list_of_nums = []
        for item in temp_list:
            try:
                list_of_nums.append(float(item))
            except ValueError as e:
                print(f"Got an error: {e}\nYou should provide numbers! {item} won't be considered")
                continue
        sum_of_numbers += my_sum(list_of_nums)
        print("\n~*~ Some of all numbers you have provided:", sum_of_numbers, end=" ~*~\n\n")


def my_sum(nums: List[float]) -> float:
    """
    Return sum of elements of the provided list
    :param nums: List[int, float]
    :return: float
    """
    result = 0
    for num in nums:
        result += num
    return result


if __name__ == "__main__":
    sum_user_numbers()
