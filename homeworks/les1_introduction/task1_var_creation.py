"""
1. Поработайте с переменными, создайте несколько, выведите на экран,
запросите у пользователя несколько чисел и строк и сохраните в переменные, выведите на экран.
"""

str_var = "My string!"
int_var = 323
float_var = 43.32
bool_var = True

while True:
    usr_int_number = input("Enter some integer number: ")
    if not usr_int_number.isdigit():
        print("You should enter the integer number. Try again\n")
        continue
    usr_number_str = input("Enter some letters: ")
    if not usr_number_str.isalpha():
        print("You should enter the alphabet letters. Try again from the beginning\n")
        continue
    print("\nstr_var = {0}\n"
          "int_var = {1}\n"
          "float_var = {2}\n"
          "bool_var = {3}"
          "user's number = {4}\n"
          "user's string = {5}".format(str_var, int_var, float_var, bool_var, usr_int_number, usr_number_str))
    break

