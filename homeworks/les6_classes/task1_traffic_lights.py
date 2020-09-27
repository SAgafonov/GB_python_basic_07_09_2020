"""
1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
Атрибут реализовать как приватный.
В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) —
на ваше усмотрение.
Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
Проверить работу примера, создав экземпляр и вызвав описанный метод.

Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить соответствующее сообщение и завершать скрипт.
"""
import time
from typing import Tuple


class TrafficLight:
    def __init__(self, lights: Tuple[str, str, str] = ("red", "yellow", "green")):
        self.__lights = lights

    def check_the_sequence(self) -> bool:
        """
        Check if the sequence of lights is correct: red, yellow, green
        :return: bool
        """
        correct_seq = ("red", "yellow", "green")
        if self.__lights == correct_seq:
            return True
        else:
            return False

    def running(self):
        """
        Print lights in correct order with predefined duration
        :return:
        """
        ligths_duration = {"red": 7, "yellow": 2, "green": 3}
        if self.check_the_sequence():
            for light in self.__lights:
                print(light.capitalize())
                time.sleep(ligths_duration.get(light))
        else:
            print("Check the sequence of lights! It should be ('red', 'yellow', 'green')")
            exit(0)


if __name__ == '__main__':
    tl = TrafficLight()
    tl.running()
