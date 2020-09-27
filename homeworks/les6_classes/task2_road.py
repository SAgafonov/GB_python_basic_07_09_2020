"""
2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
Значения данных атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными.
Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв метра дороги асфальтом,
толщиной в 1 см * число см толщины полотна. Проверить работу метода.

Например: 20м * 5000м * 25кг * 5см = 12500 т
"""


class Road:
    def __init__(self, length: float, width: float):
        self._length = length
        self._width = width

    def mass_count(self, asphalt_thickness: float) -> float:
        """
        Count mass of asphalt needed to cover the whole road.
        :param: float
        :return: float
        """
        asphalt_mass_for_one_square_metre = 25
        return self._length * self._width * asphalt_mass_for_one_square_metre * asphalt_thickness


if __name__ == '__main__':
    road = Road(5000, 20)
    print(f"{road.mass_count(5)/1000}, tons")
