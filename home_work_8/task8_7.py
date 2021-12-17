# Реализовать проект «Операции с комплексными числами».
# Создайте класс «Комплексное число», реализуйте перегрузку методов сложения и умножения комплексных чисел.
# Проверьте работу проекта, создав экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров.
# Проверьте корректность полученного результата.

class ComplexNumber:

    def __init__(self, re_a, im_b):
        self.a = re_a
        self.b = im_b
        num = re_a + im_b

    def __add__(self, other):
        return f' Сложение комплексных чисел: {self.a + other.a}+{self.b + other.b}i'

    def __mul__(self, other):
        return f' Умножение комплексных чисел: {self.a * other.a - self.b * other.b}+{self.a * other.b + self.b * other.a}i'


num = ComplexNumber(5, 3)
num_1 = ComplexNumber(-2, 1)
print(num + num_1)
print(num * num_1)
