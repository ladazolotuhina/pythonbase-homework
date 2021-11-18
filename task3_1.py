#1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def divis_num():
    try:
        num_1 = float(input('Введите делимое: '))
        num_2 = float(input('Введите делитель: '))
        d_iv = round(num_1 / num_2, 3)
        return d_iv
    except ZeroDivisionError:
        return
print(divis_num())








