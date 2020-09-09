"""
4. Пользователь вводит целое положительное число.
Найдите самую большую цифру в числе.
Для решения используйте цикл while и арифметические операции.
"""

while True:
    user_input = input("Enter positive integer: ")
    # Check if user's input is positive integer
    if not user_input.isdigit() or int(user_input) <= 0:
        print("You should provide a positive integer!")
        continue

    user_number = int(user_input)
    # Take the last number as the biggest cipher
    biggest_cipher = user_number % 10
    while user_number:
        # Get the number without the last cipher
        user_number //= 10
        # Change the biggest cipher if True
        if user_number % 10 > biggest_cipher:
            biggest_cipher = user_number % 10
    print(biggest_cipher)
    break


