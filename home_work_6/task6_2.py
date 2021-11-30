# Реализовать класс Road, в котором определить атрибуты: length, width. Значения данных
# атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными. Определить метод расчета
# массы асфальта, необходимого для покрытия всего дорожного полотна. Использовать формулу: длина*ширина*масса асфальта
# для покрытия одного кв метра дороги асфальтом, толщиной в 1 см*число см толщины полотна. Проверить работу метода.
# Например: 20м*5000м*25кг*5см = 12500 т

class Road:

    def __init__(self, length, width):
        self._length = length
        self._width = width
        self.weight = 25
        self.height = 5

    def need_asphalt(self):
        need_massa = self._length * self._width * self.weight * self.height / 1000
        print(f'Необходимо {need_massa} тонн асфальта')


r = Road(5000, 20)
r.need_asphalt()
