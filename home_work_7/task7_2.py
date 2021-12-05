# 2. Реализовать проект расчета суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
# К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры:
# размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы:
# для пальто (V/6.5 + 0.5), для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани.
# Проверить на практике полученные на этом уроке знания:
# реализовать абстрактные классы для основных классов проекта,
# проверить на практике работу декоратора @property.

from abc import ABC, abstractmethod
class Clothes(ABC):
    @abstractmethod
    def consumption(self):
        pass

class Coat(Clothes):
    def __init__(self,V):
        self.V=V

    @property
    def consumption(self):
        return f'Для пошива пальто нужно: {self.V / 6.5 + 0.5 :.2f} м ткани'


class Costume(Clothes):
    def __init__(self,H):
        self.H=H
    @property
    def consumption(self):
        return f'Для пошива костюма нужно: {2 * self.H + 0.3 :.2f} м ткани'

    #def consumption(self):
    #result= f'Для пошива костюма и пальто нужно: {self.V / 6.5 + 0.5 :.2f}+{2 * self.H + 0.3 :.2f} м ткани'
        #return result

coat = Coat(48)
costume = Costume(1.7)
print(coat.consumption)
print(costume.consumption)
#print(result.consumption)

