"""
1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""
from helper import path_maker

file_name = "test.txt"
path_to_file = path_maker(file_name)


def user_data_into_file():
    """
    Write user's input into file
    :return:
    """
    try:
        with open(path_to_file, "a") as file:
            while True:
                user_data = input("Enter some data: ")
                file.write(user_data + "\n")
                if user_data == "":
                    break
    except IOError as e:
        print(f"Smth went wrong. Check paths to file and try again")
        print(e)
        exit(0)


if __name__ == "__main__":
    user_data_into_file()
