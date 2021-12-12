# 5. Продолжить работу над первым заданием.
# Разработать методы, отвечающие за приём оргтехники на склад и передачу в определенное подразделение компании.
# Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных,
# можно использовать любую подходящую структуру, например словарь.
# 6. #Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
# Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
# Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей,
# изученных на уроках по ООП.
class Warehouse:
    def __init__(self):
        self.equ_dict = {}

    def delivery_to_wh(self, equipment):  # завоз на склад
        self.equ_dict.setdefault(equipment.group_name(), []).append(equipment)

    def get_equipment(self, quantity):
        if self.equ_dict[quantity]:
            self.equ_dict.setdefault((quantity)).pop(0)


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


class CompanyDepartment:  #
    def __init__(self, equipment):
        self.equiment = equipment


class Storekeeper:  # кладовщик выдает оргтехнику
    def __init__(self, warehouse):
        self.warehouse = warehouse

    def removal_from_wh(self, equipment, companydepartment):  # выдача на фирму
        if companydepartment:
            companydepartment.equipment = self.warehouse.get_equipment(equipment)
        else:
            print('В этом месяце ваш отдел уже получил оргтехнику')


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

storekeeper = Storekeeper('A')
companydepartment = CompanyDepartment('D')
print(companydepartment)
print(wh.equ_dict)
print('---------')
storekeeper.removal_from_wh(p1, companydepartment)

print(companydepartment.equiment)
print(wh.equ_dict)
print('---------')
# что-то так и не додумала(((( с валидоцией не сложилось...
