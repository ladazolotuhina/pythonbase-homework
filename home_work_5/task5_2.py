# 2. Создать текстовый файл (не программно),
# сохранить в нем несколько строк, выполнить подсчет количества строк, количества слов в каждой строке.

with open('task5_2.txt') as f_obj:
    content = f_obj.read()
    print(content)
    f_obj = open('task5_2.txt')
    lines = f_obj.read().split('\n')
    count_line = len(lines)
    count_word = 0
    for line in lines:
        words = line.split()
        count_word += (len(words))
    print(f'File has {count_line} lines, {count_word} words')
