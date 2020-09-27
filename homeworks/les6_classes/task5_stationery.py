"""
5. Реализовать класс Stationery (канцелярская принадлежность).
Определить в нем атрибут title (название) и метод draw (отрисовка).
Метод выводит сообщение “Запуск отрисовки.”
Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
В каждом из классов реализовать переопределение метода draw.
Для каждого из классов метод должен выводить уникальное сообщение.
Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
"""


class Stationery:
    def __init__(self, title: str):
        self.__title = title

    def draw(self):
        return "Start painting"


class Pen(Stationery):
    def __init__(self):
        self.__name = "Pen"
        super().__init__(self.__name)

    def draw(self) -> str:
        return f"{super().draw()} with a {self.__name.lower()}"


class Pencil(Stationery):
    def __init__(self):
        self.__name = "Pencil"
        super().__init__(self.__name)

    def draw(self) -> str:
        return f"{super().draw()} with a {self.__name.lower()}"


class Handle(Stationery):
    def __init__(self):
        self.__name = "Handle"
        super().__init__(self.__name)

    def draw(self) -> str:
        return f"{super().draw()} with a {self.__name.lower()}"


if __name__ == '__main__':
    pen = Pen()
    pencil = Pencil()
    handle = Handle()
    assert pen.draw() == "Start painting with a pen"
    assert pencil.draw() == "Start painting with a pencil"
    assert handle.draw() == "Start painting with a handle"
