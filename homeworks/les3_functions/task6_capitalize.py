"""
6. Реализовать функцию int_func(), принимающую слово из маленьких латинских букв
и возвращающую его же, но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.

Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом.
Каждое слово состоит из латинских букв в нижнем регистре.
Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
Необходимо использовать написанную ранее функцию int_func().
"""
from typing import Tuple


def my_title(string_to_title: str) -> Tuple[str, str]:
    """
    Converts the first character of each word to upper case.
    :param string_to_title: String separated by white spaces, all words start with small letter
    :return: tuple(str, str)
    """
    # First variant
    # Get Upper case letter in accordance to index in alphabet string
    upper_case_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lower_case_alphabet = "abcdefghijklmnopqrstuvwxyz"
    list_of_string_to_title = string_to_title.split()
    for idx in range(len(list_of_string_to_title)):
        first_letter_idx = lower_case_alphabet.index(list_of_string_to_title[idx][0])
        list_of_string_to_title[idx] = upper_case_alphabet[first_letter_idx] + list_of_string_to_title[idx][1:]
    first_var = " ".join(list_of_string_to_title)

    # Second variant
    # Convert letter to Unicode and then subtract 32 to get Upper cased letter
    list_of_string_to_title_2 = string_to_title.split()
    result = []
    for word in list_of_string_to_title_2:
        first_letter_in_unicode = ord(word[0])
        result.append(chr(first_letter_in_unicode - 32) + word[1:])
    second_var = " ".join(result)
    return first_var, second_var


if __name__ == "__main__":
    print(my_title("zsdreg  asdds  sdff  ertpo"))
