"""
2. Реализовать проект расчета суммарного расхода ткани на производство одежды.
Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры:
размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы:
для пальто (V/6.5 + 0.5), для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.

Реализовать общий подсчет расхода ткани.
Проверить на практике полученные на этом уроке знания: реализовать абстрактные классы для основных классов проекта,
проверить на практике работу декоратора @property.
"""
import abc


class MyClothes(abc.ABC):
    @property
    @abc.abstractmethod
    def fabric_consumption(self):
        pass

    @abc.abstractmethod
    def general_fabric_consumption(self):
        pass


class Clothes(MyClothes):
    def __init__(self, clothes_type: str, size: float):
        self.__clothes_type = clothes_type
        self.__size = size

    @property
    def fabric_consumption(self):
        """
        Count expense of fabric for a clothes depends on its type.
        :return: float
        """
        if self.__clothes_type.lower() == "suit":
            return round((self.__size * 2 + 0.3), 3)
        elif self.__clothes_type.lower() == "coat":
            return round((self.__size / 6.5 + 0.5), 3)
        else:
            print("Unknown type of clothes")
            exit(0)

    @staticmethod
    def general_fabric_consumption(*args: float) -> float:
        """
        Represent general expense of fabric.
        :param args: float
        :return: float
        """
        return sum(args)


class Coat(Clothes):
    def __init__(self, size: float):
        self._name = "Coat"
        self.size = size
        super().__init__(self._name, self.size)


class Suit(Clothes):
    def __init__(self, size: float):
        self._name = "Suit"
        self.size = size
        super().__init__(self._name, self.size)


if __name__ == '__main__':
    coat_size = 5.4
    suit_size = 3.8
    coat = Coat(coat_size)
    suit = Suit(suit_size)
    print(f"For a coat with size {coat_size} you need:", coat.fabric_consumption)
    print(f"For a suit with size {suit_size} you need:", suit.fabric_consumption)
    print("General expense of fabric for a coat and a suit:",
          Clothes.general_fabric_consumption(coat.fabric_consumption, suit.fabric_consumption))
