"""
5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""
import random
from typing import List
from helper import path_maker

file_name = "task5.txt"
path_to_file = path_maker(file_name)


def create_file_witn_nums() -> List[float]:
    """
    Create file with randomly generated numbers
    :return: List[float]
    """
    random_nums = [round(random.random() * 100, 3) for i in range(random.randint(1, 10))]
    try:
        with open(path_to_file, "w", encoding="UTF-8") as file:
            for num in random_nums:
                file.write(str(num) + " ")
    except IOError as e:
        print(f"Smth went wrong. Check paths to files and try again")
        print(e)
        exit(0)
    return random_nums


def get_sum_of_nums() -> float:
    """
    Get sum of all numbers in file
    :return: float
    """
    try:
        with open(path_to_file, "r", encoding="UTF-8") as file:
            string_of_nums = file.readline()
            result = sum(map(float, string_of_nums.split()))
    except FileNotFoundError as e:
        print(f"File {path_to_file} is not found")
        print(e)
        exit(0)
    except IOError as e:
        print(f"Smth went wrong. Check paths to file and try again")
        print(e)
        exit(0)
    except ValueError as e:
        print(f"Check if there's no letters in {file_name}.")
        print(e)
        exit(0)
    return result


if __name__ == '__main__':
    print(f"Sum of all nums {create_file_witn_nums()} in {file_name} is: ", get_sum_of_nums())
