# задание 1.
# Поработайте с переменными, создайте несколько, выведите на экран,
# запросите у пользователя несколько чисел и строк и сохраните в переменные, выведите на экран.

your_name = input('Как Ваше имя? ')
answer = f'Привет, {your_name}! Рады знакомству!'
print(answer)

your_number = int(input('Введите число '))
print(your_number + 5)
print(your_number / 5)
print(your_number ** 5)
print(f'Разряд Вашего числа {your_number :05}')

like_number = int(input('Введите свое любимое число '))
my_like_number = f'Мое любимое число {7}'
print(my_like_number)

print('END!')
