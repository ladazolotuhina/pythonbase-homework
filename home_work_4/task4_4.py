# Представлен список чисел. Определите элементы списка, не имеющие повторений.
# Сформируйте итоговый массив чисел, соответствующих требованию.
# Элементы выведите в порядке их следования в исходном списке.
# Для выполнения задания обязательно используйте генератор.
# Пример исходного списка: [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11].
# Результат: [23, 1, 3, 10, 4, 11]

my_list = [23, 5, 6, 6, 7, 4, 8, 11, 8, 55, 6, 7, 9, 7, 5, 5, 11]
result = [elem for elem in my_list if my_list.count(elem) < 2]
print(result)
