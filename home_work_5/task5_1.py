# 1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.


with open('task5_1.txt', 'w') as f_obj:
    us_str = input('Enter anything: ')
    f_obj.writelines(us_str)
while us_str:
    us_str = input('Enter anything: ')
    if not us_str:
        break
