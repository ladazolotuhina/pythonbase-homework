# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

with open('task5_5.txt', 'w') as f1:
    dig_str = '12 13 58 4 25 1.95'
    f1.write(dig_str)

with open('task5_5.txt', 'r') as f2:
    new_dig = f2.read()
    new_dig = new_dig.split()
    for i in range(len(new_dig)):
        new_dig[i] = float(new_dig[i])
    print(sum(new_dig))
