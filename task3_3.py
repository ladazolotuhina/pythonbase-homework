#3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.
user_numbers = []
for i in range (3):
    number = int(input('Введите число: '))
    user_numbers.append(number)
print(sum(user_numbers)-min(user_numbers))
