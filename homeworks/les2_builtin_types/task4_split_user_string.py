"""
4. Пользователь вводит строку из нескольких слов, разделённых пробелами.
Вывести каждое слово с новой строки.
Строки необходимо пронумеровать.
Если в слово длинное, выводить только первые 10 букв в слове.
"""

user_input = input("Enter any sequence splitted by spaces. Ex. 'test mylongstring': ")

splitted_input = user_input.split()
for number, word in enumerate(splitted_input, 1):
    print(f"{number}.", word if len(word) < 10 else word[:10])
