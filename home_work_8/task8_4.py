# Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
# А также класс «Оргтехника», который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определить параметры, общие для приведенных типов.
# В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.

class Warehouse:
    def __init__(self):
        self.equ_dict = {}

    def removal_from_wh(self):  # вывоз на фирму
        pass

    def delivery_to_wh(self, equipment):  # завоз на склад
        self.equ_dict.setdefault(equipment.group_name(), []).append(equipment)


class OfficeEquipment:
    def __init__(self, name, made, quantity):
        self.name = name
        self.made = made
        self.quantity = quantity
        self.group = self.__class__.__name__

    def __repr__(self):
        return f' {self.name} - {self.made}, {self.kind},{self.quantity} ед'

    def group_name(self):
        return f'{self.group}'


class Printer(OfficeEquipment):
    def __init__(self, name, made, quantity, kind):
        super().__init__(name, made, quantity)
        self.kind = kind


class Scaner(OfficeEquipment):
    def __init__(self, name, made, quantity, kind):
        super().__init__(name, made, quantity)
        self.kind = kind


class Xerox(OfficeEquipment):
    def __init__(self, name, made, quantity, kind):
        super().__init__(name, made, quantity)
        self.kind = kind


wh = Warehouse()
p1 = Printer('printer', 'HP', 5, 'laser')
p2 = Printer('printer', 'EPSON', 6, 'matrix')
wh.delivery_to_wh(p1)
wh.delivery_to_wh(p2)

sc1 = Scaner('scaner', 'HP', 8, 'tablet')
sc2 = Scaner('scaner', 'EPSON', 2, 'drum')
wh.delivery_to_wh(sc1)
wh.delivery_to_wh(sc2)
xer1 = Xerox('xerox', 'HP', 3, 'analog')
xer2 = Xerox('xerox', 'CANON', 7, 'digital')
wh.delivery_to_wh(xer1)
wh.delivery_to_wh(xer2)
print(wh.equ_dict)
