# 2. Представлен список чисел.
# Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.

first_list = [20, 45, 8, 9, 5, 65, 2, 9, 2, 30]
new_list = [first_list[i] for i in range(1, len(first_list)) if first_list[i] > first_list[i - 1]]
print(new_list)
