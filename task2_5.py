
# Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями,
# то новый элемент с тем же значением должен разместиться после них.
# Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
# Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
# Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
# Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
# Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2].

rating_list = [8, 6, 5, 4, 4, 3, 2, 2, 1]
rating = int(input('Введите цифру рейтинга: '))
insert = False
for index, elem in enumerate(rating_list):
    if rating>elem:
        rating_list.insert(index, rating)
        inserted = True
        break
if not inserted:
    rating_list.append(rating)
print (rating_list)
