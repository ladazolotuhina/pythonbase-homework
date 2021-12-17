# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
# Проверьте его работу на данных, вводимых пользователем.
# При вводе пользователем нуля в качестве делителя программа должна корректно
# обработать эту ситуацию и не завершиться с ошибкой.
#


class MyError(Exception):
    pass


num_1 = float(input('Введите делимое: '))
num_2 = float(input('Введите делитель: '))

try:
    d_iv = round(num_1 / num_2, 3)
    if num_2 == 0:
        raise MyError

except ZeroDivisionError as e:
    print('Деление на ноль не допустимо!')

except MyError as err:
    print(err)
else:
    print(f'результат деления: {d_iv}')
