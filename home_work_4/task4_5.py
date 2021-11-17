# Реализовать формирование списка, используя функцию range() и возможности генератора.
# В список должны войти чётные числа от 100 до 1000 (включая границы).
# Нужно получить результат вычисления произведения всех элементов списка.
# Подсказка: использовать функцию reduce().

from functools import reduce

numbers = range(100, 1001)
new_list = [i for i in numbers if i % 2 == 0]
result = reduce(lambda x, y: x * y, new_list)
print(result)
