"""
6. Спортсмен занимается ежедневными пробежками.
В первый день его результат составил a километров.
Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего.
Требуется определить номер дня, на который общий результат спортсмена составить не менее b километров.
Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня.
Например: a = 2, b = 3.
Результат:
1-й день: 2
2-й день: 2,2
3-й день: 2,42
4-й день: 2,66
5-й день: 2,93
6-й день: 3,22

Ответ: на 6-й день спортсмен достиг результата — не менее 3 км.
"""

first_day_result = float(input("Enter how many km runner has done for the first day: "))
aim_result = float(input("Enter how many km runner should run: "))
runner_day_progress_in_percent = 10
runner_progress = first_day_result
counter = 1
while runner_progress <= aim_result:
    print(f"{counter}-й день: {runner_progress:.3}")
    runner_progress += runner_progress * (runner_day_progress_in_percent / 100)
    counter += 1
    if runner_progress > aim_result:
        print(f"{counter}-й день: {runner_progress:.3}")

print(f"\nОтвет: на {counter}-й день  спортсмен достиг результата — не менее {aim_result} км.")
