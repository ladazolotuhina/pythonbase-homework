# 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.

with open('task5_3.txt', encoding='utf-8') as f_obj:
    summa = 0
    salary = []
    persons = []
    pers_list = f_obj.read().split('\n')
    for i in pers_list:
        i = i.split()
        if int(i[1]) <= 20000:
            persons.append(i[0])
        salary.append(i[1])

print(f'Фамилии сотрудников, имеющих оклад меньше 20000 : {persons}')
print(f'Средний оклад сотрудников отдела : {sum(map(int, salary)) / len(salary)}')
