"""
3. Реализовать базовый класс Worker (работник), в котором определить атрибуты:
name, surname, position (должность), income (доход).
Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия,
например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker.
В классе Position реализовать методы получения полного имени сотрудника (get_full_name)
и дохода с учетом премии (get_total_income).

Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные,
проверить значения атрибутов, вызвать методы экземпляров).
"""


class Worker:
    def __init__(self, name: str, surname: str, position: str, wage: float, bonus: float):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def get_full_name(self) -> str:
        """
        Return full name of employee.
        :return: str
        """
        return self.name + " " + self.surname

    def get_total_income(self) -> float:
        """
        Return full income of employee, including bonus.
        :return: float
        """
        return sum(self._income.values())


if __name__ == '__main__':
    u_name = "Test"
    u_surname = "Powed"
    u_position = "gdhnbn"
    u_wage = 23.4
    u_bonus = 45.45
    worker = Position(u_name, u_surname, u_position, u_wage, u_bonus)
    assert u_name == worker.name
    assert u_surname == worker.surname
    assert u_position == worker.position
    assert worker.get_total_income() == u_wage + u_bonus
    assert worker.get_full_name() == u_name + " " + u_surname
