"""
6. * Реализовать структуру данных «Товары».
Она должна представлять собой список кортежей.
Каждый кортеж хранит информацию об отдельном товаре.
В кортеже должно быть два элемента — номер товара и словарь
с параметрами (характеристиками товара: название, цена, количество, единица измерения).
Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
Пример готовой структуры:
[
(1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
(2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
(3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
]
Необходимо собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ — характеристика товара,
например название, а значение — список значений-характеристик, например список названий товаров.
Пример:
{
“название”: [“компьютер”, “принтер”, “сканер”],
“цена”: [20000, 6000, 2000],
“количество”: [5, 2, 7],
“ед”: [“шт.”]
}
"""
from pprint import pprint

article_characteristics = ["name", "price", "quantity", "units"]
goods = []

counter = 0
while True:
    tmp = {}
    for i in article_characteristics:
        user_input = input(f"Enter '{i}' of an article: ")
        # Check if user inputs an integer value for 'price', 'quantity'.
        # If not skip the step
        if i in ["price", "quantity"]:
            if user_input.isdigit():
                tmp[f"{i}"] = int(user_input)
                continue
            else:
                print(f"{i.capitalize()} should be integer. Try again")
                break
        tmp[f"{i}"] = user_input
    goods.append((counter + 1, tmp))
    # If 'price' or 'quantity' is not provided delete the product
    if not (goods[counter][1].get("price") and goods[counter][1].get("quantity")):
        goods.pop(counter)
        counter -= 1
    choice = input("\nWant to add an article? Y(yes), N(no)? ")
    print("")
    if choice.lower() == ("y" or "yes"):
        counter += 1
        continue
    else:
        break
print("Your goods: ", goods, end="\n")

goods_analytics = dict((i, []) for i in article_characteristics)
for article in goods:
    for i in article_characteristics:
        goods_analytics[i].append(article[1][i])
print("Goods analytics: ", end="")
pprint(goods_analytics)
