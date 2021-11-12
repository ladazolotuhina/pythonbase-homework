# задание 3.
# Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например, пользователь ввёл число 3.
# Считаем 3 + 33 + 333 = 369.

user_number = input("Write a number: ")
number_str = f"{user_number} + {user_number*2} + {user_number*3} = "
summary = int(user_number) + int(user_number*2) + int(user_number*3)
result = number_str + str(summary)
print(result)

print('END!')