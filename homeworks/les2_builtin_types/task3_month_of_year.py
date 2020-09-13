"""
3. Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите решения через list и через dict.
"""

months = ["January",
          "February",
          "March",
          "April",
          "May",
          "June",
          "July",
          "August",
          "September",
          "October",
          "November",
          "December"
          ]

# make a dict from list. Keys are month's numbers
months_to_numbers = {i: months[i] for i in range(len(months))}

while True:
    user_month = input("Enter number of month: ")
    if user_month.isdigit() and 0 < int(user_month) <= 12:
        break
    print("You should enter integer number from 1 to 12")

print("\nSolution with list:", months[int(user_month) - 1])
print("Solution with dictionary:", months_to_numbers[int(user_month) - 1])
