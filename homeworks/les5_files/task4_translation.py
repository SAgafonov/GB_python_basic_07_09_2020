"""
4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4

Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
"""
from helper import path_maker

file_input = "task4.txt"
file_output = "task4_output.txt"
path_to_input_file = path_maker(file_input)
path_to_output_file = path_maker(file_output)


def translation():
    """
    Translate English words to Russian and write it to a new file
    :return:
    """
    for_translation = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}
    try:
        with open(path_to_input_file, "r", encoding="UTF-8") as in_file, \
                open(path_to_output_file, "w", encoding="UTF-8") as out_file:
            for line in in_file:
                for key in for_translation.keys():
                    if key.lower() in line.lower():
                        k = key
                    translated_line = line.replace(k, for_translation[k])
                out_file.write(translated_line)
    except FileNotFoundError as e:
        print(f"File {path_to_input_file} is not found")
        print(e)
        exit(0)
    except IOError as e:
        print(f"Smth went wrong. Check paths to file and try again")
        print(e)
        exit(0)


if __name__ == '__main__':
    translation()
