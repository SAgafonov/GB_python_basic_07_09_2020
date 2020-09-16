"""
2. Реализовать функцию, принимающую несколько параметров,
описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.
"""


def user_input() -> dict:
    """
    Get user input.
    :return: dict.
    """
    user_data_template = {
        "name": str,
        "surname": str,
        "year_of_birth": int,
        "city": str,
        "email": str,
        "phone": str
    }

    user_data = {}
    for question, data_type in user_data_template.items():
        while True:
            try:
                input_data = data_type(input(f"Enter your {question}: "))
                if question == "year_of_birth" and input_data // 1000 not in range(1, 10):
                    print("Date of birth should be positive four-digit number!")
                    continue
            except ValueError as e:
                print(f"{e}\nProvide correct data")
                continue
            user_data[question] = input_data
            break
    return user_data


def print_user_data(**kwargs):
    """
    Print keyword arguments with its values.
    :param kwargs:
    :return:
    """
    print("")
    for key, value in kwargs.items():
        print(f"{key.capitalize()}: {value}", end="; ")


if __name__ == "__main__":
    print_user_data(**user_input())
