# Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (
# булево).  А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась,
# повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс
# метод show_speed, который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите
# метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении
# скорости. Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам,
# выведите результат. Выполните вызов методов и также покажите результат.

class Car:

    def __init__(self, name, speed, color, is_police=False):
        self.name = name
        self.speed = speed
        self.color = color
        self.is_police = is_police

    def go(self):
        print('Можете начать движение')

    def stop(self):
        print('Остановитесь!')

    def turn(self, direction):
        print(f'Поверните на {direction}')

    def show_speed(self):
        print(f'Ваша скорость {self.speed}')


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            result = self.speed - 60
            print(f'Вы превысили скорость на {result} км/ч')
        else:
            print(f'Вы движитесь с допустимой скоростью {self.speed}')


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 40:
            print('Вы превысили скорость')


class PoliceCar(Car):
    def __init__(self, name, speed, color):
        super().__init__(name, speed, color, True)


town = TownCar('Mazda', 90, 'grey')
sport = SportCar('Bugatti', 200, 'red')
work = WorkCar('Man', 39, 'white')
police = PoliceCar('Kia', 90, 'blue')

town.show_speed()
work.show_speed()

police.turn('направо')
