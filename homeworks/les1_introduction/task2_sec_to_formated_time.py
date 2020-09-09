"""
2. Пользователь вводит время в секундах.
Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
Используйте форматирование строк.
"""

time_in_seconds = int(input("Enter time in seconds: "))

if 86400 > time_in_seconds >= 0:
    print("Human time: {:>02d}:{:>02d}:{:>02d}".format(
        (time_in_seconds // 3600 % 24),
        (time_in_seconds // 60 % 60),
        (time_in_seconds % 60)
    ))
else:
    print("Specify number in between [0, 86400)")
