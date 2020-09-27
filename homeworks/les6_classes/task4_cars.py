"""
4. Реализуйте базовый класс Car.
У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed,
который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.

Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.
"""
import random


class Car:
    def __init__(self, speed: int, color: str, name: str, is_police: bool):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self) -> str:
        if self.speed == 0:
            self.speed = random.randint(1, 100)
        return "Car is moving with speed {}".format(self.speed)

    def stop(self) -> str:
        if self.speed != 0:
            self.speed = 0
        return "Car is stopped"

    def turn(self, direction: str) -> str:
        if self.speed == 0:
            self.go()
        return f"Turning {direction}"

    def show_speed(self) -> int:
        return self.speed


class TownCar(Car):
    def __init__(self, speed: int, color: str):
        self.name = "Town car"
        self.is_police = False
        super().__init__(speed, color, self.name, self.is_police)
        self.speed_limit = 60

    def show_speed(self) -> int:
        if self.speed > self.speed_limit:
            print(f"Slow down. Your speed is {self.speed} km/h. You exceed the speed limit {self.speed_limit} km/h")
        else:
            return super().show_speed()


class SportCar(Car):
    def __init__(self, speed: int, color: str):
        self.name = "Sport car"
        self.is_police = False
        super().__init__(speed, color, self.name, self.is_police)


class WorkCar(Car):
    def __init__(self, speed: int, color: str):
        self.name = "Work car"
        self.is_police = False
        super().__init__(speed, color, self.name, self.is_police)
        self.speed_limit = 40

    def show_speed(self) -> int:
        if self.speed > self.speed_limit:
            print(f"Slow down. Your speed is {self.speed} km/h. You exceed the speed limit {self.speed_limit} km/h")
        else:
            return super().show_speed()


class PoliceCar(Car):
    def __init__(self, speed: int, color: str):
        self.name = "Police car"
        self.is_police = True
        super().__init__(speed, color, self.name, self.is_police)


if __name__ == '__main__':
    pc = PoliceCar(60, "black")
    wc = WorkCar(49, "silver")
    tc = TownCar(61, "yellow")
    sc = SportCar(0, "yellow")

    print(f"Police car speed {pc.speed}, color {pc.color}, name {pc.name}")
    print(f"Is this a police car? - {pc.is_police}")
    print(pc.turn("left"))
    print(pc.stop())
    print(f"New speed of police car is {pc.show_speed()}\n")

    print(f"Work car speed {wc.speed}, color {wc.color}, name {wc.name}")
    print(f"Is this a police car? - {wc.is_police}")
    wc.show_speed()
    print(wc.turn("left"))
    wc.speed = 20
    print(f"New speed of work car is {wc.show_speed()}")
    print(wc.stop())
    print(f"New speed of work car is {wc.show_speed()}\n")

    print(f"Town car speed {tc.speed}, color {tc.color}, name {tc.name}")
    print(tc.go())
    tc.show_speed()
    tc.speed = 10
    print(tc.turn("right"))
    print(f"New speed of town car is {tc.show_speed()}")
    print(tc.stop())
    print(f"New speed of town car is {tc.show_speed()}\n")

    print(f"Sport car speed {sc.speed}, color {sc.color}, name {sc.name}")
    print(sc.go())
    print(sc.turn("right"))
    sc.speed = 10
    print(f"New speed of sport car is {sc.show_speed()}")
    print(sc.stop())
    print(f"New speed of sport car is {sc.show_speed()}")
