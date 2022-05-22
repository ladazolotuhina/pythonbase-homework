# задание 5.
# Запросите у пользователя значения выручки и издержек фирмы.
# Определите, с каким финансовым результатом работает фирма
# (прибыль — выручка больше издержек, или убыток — издержки больше выручки).
# Выведите соответствующее сообщение. Если фирма отработала с прибылью, вычислите рентабельность выручки
# (соотношение прибыли к выручке).
# Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.

print('Tell about your company')
proceeds = int(input('Write proceeds your company '))
costs = int(input('Write costs your company '))

if proceeds > costs:
    profit = proceeds - costs
    print(f'Your company has a profit {profit} $')
    profitabality = proceeds / costs
    print(f'Your company has a profitabality {profitabality} $')
    number_works = int(input('Write number of works your company '))
    profit_1_w = profit/number_works
    print(f'Your company has a profit per worker {profit_1_w} $')
else:
    print('Your company has a lesion')

print('END !')
