# Реализовать базовый класс Worker, в котором определить атрибуты: name, surname, position,
# income. Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия,
# например, {"wage": wage, "bonus": bonus}. Создать класс Position на базе класса Worker. В классе Position
# реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).
# Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные, проверить значения
# атрибутов, вызвать методы экземпляров).

class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': int(wage), 'bonus': int(bonus)}


class Position(Worker):

    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_total_income(self):
        return self._income["wage"] + self._income["bonus"]


person = Position('Anna', 'Ivanova', 'PR', '150000', '50000')
print(person.name)
print(person.surname)
print(person.get_full_name())
print(person.get_total_income())
print(person.get_full_name(), person.get_total_income())
