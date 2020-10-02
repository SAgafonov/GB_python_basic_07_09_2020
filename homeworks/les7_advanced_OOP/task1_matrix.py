"""
1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.

Примеры матриц вы найдете в методичке.

Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix (двух матриц).
Результатом сложения должна быть новая матрица.

Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем
с первым элементом первой строки второй матрицы и т.д.
"""
from typing import List


class Matrix:
    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix

    def __str__(self):
        return "".join("|" + str(item).strip('[]') + "|" + "\n" for item in self.matrix)

    def __add__(self, other):
        new_matrix = []
        for line1, line2 in zip(self.matrix, other.matrix):
            new_matrix.append([])
            for x, y in zip(line1, line2):
                new_matrix[self.matrix.index(line1)].append(x + y)
        # return Matrix([x + y for line1, line2 in zip(self.matrix, other.matrix) for x, y in zip(line1, line2)])
        return Matrix(new_matrix)


if __name__ == '__main__':
    m1 = Matrix([[1, 2, 0], [4, 5, 6]])
    m2 = Matrix([[1, 2, 0], [4, 5, 6]])
    print(m1)
    print(m2)
    print(m1 + m2)
