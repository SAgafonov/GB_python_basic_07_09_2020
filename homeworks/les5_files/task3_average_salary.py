"""
3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.
"""
from helper import path_maker

file_name = "task3.txt"
path_to_file = path_maker(file_name)


def read_from_file() -> list:
    """
    Open file and read all lines
    :return: list
    """
    try:
        with open(path_to_file, "r", encoding="UTF-8") as file:
            content = file.readlines()
    except FileNotFoundError as e:
        print(f"File {path_to_file} is not found")
        print(e)
        exit(0)
    return content


def salary_less_twenty(list_of_users: list) -> str:
    """
    Return users with salary less than 20k
    :param list_of_users: list
    :return: str
    """
    try:
        return ', '.join([item.split()[0].strip(":") for item in list_of_users if float(item.split()[1]) < 20000])
    except ValueError as e:
        print(f"Check if {file_name} has correct format: <name>: <salary> <currency>")
        print(e)
        exit(0)


def average_salary(list_of_users: list) -> float:
    """
    Return average salary.
    :param list_of_users: list
    :return: float
    """
    try:
        temp = list(map(float, [item.split()[1] for item in list_of_users]))
    except ValueError as e:
        print(f"Check if {file_name} has correct format: <name>: <salary> <currency>")
        print(e)
        exit(0)
    return sum(temp) / len(temp)


if __name__ == '__main__':
    from_file = read_from_file()
    print(f"{salary_less_twenty(from_file)} have less than 20k")
    print("Average salary is: ", average_salary(from_file))
