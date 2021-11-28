#6. Необходимо создать (не программно) текстовый файл,где каждая строка описывает
# учебный предмет и наличие лекционных, практических и лабораторных занятий по этому предмету и их количество.
# Важно, чтобы для каждого предмета не обязательно были все типы занятий.
# Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран.
#Примеры строк файла:
#Информатика: 100(л) 50(пр) 20(лаб).
#Физика: 30(л) — 10(лаб)
#Физкультура: — 30(пр) —

#Пример словаря:
#{“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}

#import json

sub_dict = {}
with open('task5_6.txt') as f_obj:
    content= f_obj.read().split()
    for subj in content:
        #subj, lect, pract, lab = content.split()
        sub_dict[subj]=sum(int(i) for i in content if i.isdigit)
        #sub_dict[subj] = int(lect) + int(pract) + int(lab)
    print( {subj})
    #print(sum(int(i) for i in content if i.isdigit))