"""
6. Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет
и наличие лекционных, практических и лабораторных занятий по этому предмету и их количество.
Важно, чтобы для каждого предмета не обязательно были все типы занятий.
Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
Вывести словарь на экран.

Примеры строк файла:
Информатика: 100(л) 50(пр) 20(лаб).
Физика: 30(л) — 10(лаб)
Физкультура: — 30(пр) —

Пример словаря:
{“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
"""
import re
from helper import path_maker

file_name = "task6.txt"
path_to_file = path_maker(file_name)


def get_total_lessons() -> dict:
    """
    Process every line of a file and return a dict with all subjects from a file and total amount of lessons.
    :return: dict
    """
    temp_d = {}
    try:
        with open(path_to_file, "r", encoding="UTF-8") as file:
            for line in file:
                temp_d.update(count_lessons(line))
    except FileNotFoundError as e:
        print(f"File {path_to_file} is not found.")
        print(e)
        exit(0)
    except IOError as e:
        print(f"Smth went wrong. Check if file {path_to_file} exists and try again")
        print(e)
        exit(0)
    return temp_d


def count_lessons(subject_info: str) -> dict:
    """
    Return dictionary where key is a lesson's name and value is number of lessons.
    :param subject_info: str
    :return: dict
    """
    temp_list = subject_info.split()
    d = {temp_list[0]: 0}
    for i in temp_list[1:]:
        # skip this string if string doesn't have numbers
        if not re.match(r"^\d+", i):
            continue
        try:
            d[temp_list[0]] += int(i[:i.find("(")])
        except ValueError as e:
            print(f"Check if {path_to_file} has correct format of numbers. They must be integers.")
            print(e)
            exit(0)
    return d


if __name__ == '__main__':
    print(get_total_lessons())
