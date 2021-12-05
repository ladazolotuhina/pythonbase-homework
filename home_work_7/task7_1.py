# 1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
# который должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Примеры матриц вы найдете в методичке.
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix (двух матриц).
# Результатом сложения должна быть новая матрица.

from random import randint

class Matrix:
    def __init__(self, A):
        self.A = A

    def __str__(self):
        sp = ""
        for i in range(len(self.A)):
            for j in range(len(self.A[i])):
                sp += f'{self.A[i][j]}'
            sp += "\n"
        return sp

    def __add__(self, other):
        A = [
            [self.A[i][j]+other.A[i][j]for j in range(len(self.A[i]))]
            for i in range(len(self.A))]
        return Matrix(A)

x = Matrix([[randint(0, 9) for _ in range(4)] for _ in range(4)])
y = Matrix([[randint(0, 9) for _ in range(4)] for _ in range(4)])

print(x)
print(y)
print(x + y)
