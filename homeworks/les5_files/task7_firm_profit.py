"""
7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
название, форма собственности, выручка, издержки.

Пример строки файла: firm_1 ООО 10000 5000.

Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).

Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

Подсказка: использовать менеджеры контекста.
"""
import json
from helper import path_maker

in_file = "task7.txt"
out_file = "task7_firms_info.json"
path_to_input_file = path_maker(in_file)
path_to_output_file = path_maker(out_file)


def read_from_file() -> dict:
    """
    Read lines from file and return dict with counted profit for each company.
    :return: dict
    """
    result = {}
    try:
        with open(path_to_input_file, "r", encoding="UTF-8") as file:
            for line in file:
                result.update(count_profit(line))
    except FileNotFoundError as e:
        print(f"File {path_to_input_file} is not found.")
        print(e)
        exit(0)
    except IOError as e:
        print(f"Smth went wrong. Check path to {path_to_input_file}")
        print(e)
        exit(0)
    return result


def count_profit(firm_info: str) -> dict:
    """
    Count profit for each company.
    :param firm_info: str
    :return: dict
    """
    temp_list = firm_info.split()
    d = {temp_list[0]: 0}
    try:
        d[temp_list[0]] = float(temp_list[2]) - float(temp_list[3])
    except ValueError as e:
        print(f"Check if {path_to_input_file} has correct format of numbers. They must be floats.")
        print(e)
        exit(0)
    return d


def count_average() -> float:
    """
    Count average profit for all companies that profit > 0.
    :return: float
    """
    overall_profit = 0
    counter = 0
    for val in read_from_file().values():
        if val < 0:
            continue
        overall_profit += val
        counter += 1
    return overall_profit / counter


def save_to_json():
    """
    Save companies with their profit and average profit as JSON file.
    :return:
    """
    data = [read_from_file(), {"average_profit": count_average()}]
    try:
        with open(path_to_output_file, "w") as file:
            json.dump(data, file)
    except IOError as e:
        print(f"Smth went wrong. Check path to {path_to_output_file}")
        print(e)
        exit(0)


if __name__ == '__main__':
    save_to_json()
