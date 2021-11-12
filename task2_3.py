#Пользователь вводит месяц в виде целого числа от 1 до 12.
#Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.
mounth = input('Введите номер месяца: ')
w, sp, su, a = 'зима','весна', 'лето','осень'
season_dict = {'1': w, '2': w, '3': sp,'4': sp,'5': sp,'6': su, '7': su,'8': su,'9': a, '10': a,'11': a,'10': w}
print(season_dict[mounth])
season_list = [w, w, sp,sp, sp, su, su, su, a, a, a, w]
print(season_list[int(mounth)-1])

print('END')
