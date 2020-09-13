"""
2. Для списка реализовать обмен значений соседних элементов,
т.е. Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
При нечетном количестве элементов последний сохранить на своем месте.
Для заполнения списка элементов необходимо использовать функцию input().
"""

user_input = input("Enter any sequence splitted by spaces. Ex. '12 qwe [12,3] end_of_str': ")

splitted_input = user_input.split()
for i in range(0, len(splitted_input), 2):
    tmp = splitted_input[i]
    if (i + 1) < len(splitted_input):
        splitted_input[i] = splitted_input[i+1]
        splitted_input[i+1] = tmp
    else:
        break
print(splitted_input)
