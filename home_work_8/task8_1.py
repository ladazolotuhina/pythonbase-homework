# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода.
# Первый, с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
# Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.

class Date:

    def __init__(self, day=0, month=0, year=0):
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def from_string(cls, date_str):
        day, month, year = map(int, date_str.split('-'))
        us_date = cls(day, month, year)
        print(cls, date_str)
        return us_date

    @staticmethod
    def is_date_valid(date_str):
        day, month, year = map(int, date_str.split('-'))
        if day <= 31 and day != 0 and month <= 12 and month != 0 and year <= 2100:
            print(date_str)
            return day, month, year
        else:
            print('Введена неправильная дата!')


d = '14-10-2021'
is_date = Date.is_date_valid(d)
