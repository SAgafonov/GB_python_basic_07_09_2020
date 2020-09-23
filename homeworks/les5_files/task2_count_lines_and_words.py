"""
2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""
from helper import path_maker

file_name = "task2.txt"
path_to_file = path_maker(file_name)


def count_lines_and_words() -> dict:
    """
    Count lines in a file and number of words in each line
    :return: dict
    """
    d = {}
    try:
        with open(path_to_file, "r", encoding="UTF-8") as file:
            for num, line in enumerate(file.readlines(), 1):
                d[num] = len(line.split())
    except FileNotFoundError as e:
        print(f"File {path_to_file} is not found")
        print(e)
        exit(0)
    return d


if __name__ == '__main__':
    temp = count_lines_and_words()
    print(f"There're {max(temp)} lines in a file {file_name}")
    for i, val in temp.items():
        print(f"{val} words in line {i}")
