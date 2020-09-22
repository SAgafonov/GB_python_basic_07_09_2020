"""
1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.
"""
import sys


def salary_count(user_manufacture: float, user_rate: float, user_bonus: float) -> float:
    """
    Return the salary.
    :param user_manufacture: float
    :param user_rate: float
    :param user_bonus: float
    :return:
    """
    return (user_manufacture * user_rate) + user_bonus


try:
    _, manufacture, rate, bonus = sys.argv
    manufacture, rate, bonus = map(float, sys.argv[1:])
except ValueError as e:
    if len(sys.argv) != 3:
        print("Provide exactly 3 arguments in the following order: manufacture, rate, bonus")
    else:
        print("Arguments should be numbers!")
    exit(0)


if __name__ == "__main__":
    print(f"Your salary, assuming manufacture: {manufacture} hours, rate: {rate} hours, bonus: {bonus} rubles is:",
          salary_count(manufacture, rate, bonus))
