#Создать список и заполнить его элементами различных типов данных.
# Реализовать скрипт проверки типа данных каждого элемента.
#Использовать функцию type() для проверки типа.
# Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.
my_str = 'have a good day'
my_list = list(my_str)
print(len(my_list))
print(type(my_list))
my_list[0] = '!'
print(my_list)
my_list_1 = ['hello', 'привет', 15, 2, True]
print(len(my_list_1))
print(type(my_list_1))
print(my_list_1)
my_list_1.append(7)
print(my_list_1)
my_list_1.insert(1,'Hi')
print(my_list_1)

print('END')
