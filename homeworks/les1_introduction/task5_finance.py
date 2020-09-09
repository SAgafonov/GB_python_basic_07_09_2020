"""
5. Запросите у пользователя значения выручки и издержек фирмы.
Определите, с каким финансовым результатом работает фирма
(прибыль — выручка больше издержек, или убыток — издержки больше выручки).
Выведите соответствующее сообщение.
Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке).
Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.
"""

gain = float(input("Enter the firm's gain: "))
expenses = float(input("Enter the firm's expenses: "))
if gain == expenses:
    print("Company works at zero")
elif gain > expenses:
    profit = gain - expenses
    profitability = (gain - expenses) / gain
    print("Your company is profitable. \nProfitability is {:>.03f}".format(profitability))
    quantity_of_employees = int(input("Enter the number of company employees: "))
    print("Profit for an employee is {:>.03f}".format(profit / quantity_of_employees))
else:
    print("Your company is unprofitable.")
