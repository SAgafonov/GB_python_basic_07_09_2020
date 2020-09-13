"""
5. Реализовать структуру «Рейтинг»,
представляющую собой не возрастающий набор натуральных чисел.
У пользователя необходимо запрашивать новый элемент рейтинга.
Если в рейтинге существуют элементы с одинаковыми значениями,
то новый элемент с тем же значением должен разместиться после них.
"""

rating_list = [7, 5, 3, 2, 3]

while True:
    user_rating = input("Enter some integer number or 'quit' to exit: ")
    if user_rating.lower() == "quit":
        break
    if not user_rating.isdigit():
        print("You should enter an integer number")
        continue
    int_user_rating = int(user_rating)
    if int_user_rating in rating_list:
        # Get the index of the last existed element in liest and insert new value after it
        rating_list.insert(rating_list[::-1].index(int_user_rating) + 1, int_user_rating)
    else:
        rating_list.append(int_user_rating)
    print("\nYour rating list is: ", sorted(rating_list, reverse=True))
