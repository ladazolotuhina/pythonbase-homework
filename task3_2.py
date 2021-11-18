#2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы. Реализовать вывод данных о пользователе одной строкой.

def cust_data(name, surname, born_year, leave_city, email, phone):
    result= (f'{name} {surname} {born_year} года рождения, проживающий в городе {leave_city} {email} {phone}')
    return result

us_name = input('Имя: ')
us_surname = input('Фамилия: ')
us_born_year = input('Год рождения: ')
us_leave_city = input('Город: ')
us_email = input('Почта: ')
us_phone = input('Телефон: ')

print(cust_data(name = us_name, surname = us_surname, born_year = us_born_year, leave_city = us_leave_city, email = us_email, phone = us_phone))
