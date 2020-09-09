"""
3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.
"""

while True:
    user_number = input("Enter a number: ")
    if not user_number.isdigit():
        print("You should enter a number! try again!")
        continue
    break
print("")
print(f"{user_number}+{user_number * 2}+{user_number * 3} =",
      int(user_number) +
      int(user_number * 2) +
      int(user_number * 3)
      )
