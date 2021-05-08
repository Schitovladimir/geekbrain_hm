"""Lesson - 2
Task -6
*Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
Каждый кортеж хранит информацию об отдельном товаре.
В кортеже должно быть два элемента — номер товара и словарь с параметрами
(характеристиками товара: название, цена, количество, единица измерения).
Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
Пример готовой структуры:
[
    (1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
    (2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
    (3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
]
Необходимо собрать аналитику о товарах.
Реализовать словарь, в котором каждый ключ — характеристика товара, например название,
а значение — список значений-характеристик, например список названий товаров.
Пример:
{
    “название”: [“компьютер”, “принтер”, “сканер”],
    “цена”: [20000, 6000, 2000],
    “количество”: [5, 2, 7],
    “ед”: [“шт.”]
"""

goods = []
i = 0

#Ввод значений в список
while True:
    i += 1
    name = input("Enter name of product: ")
    price = input("Enter price for product: ")
    if price.isdigit() == False:
        while price.isdigit() == False:
            price = input("Enter price for product in the NUMBER format: ")
    quantity = input("Enter quantity of goods: ")
    if quantity.isdigit() == False:
        while quantity.isdigit() == False:
            quantity = input("Enter quantity of goods in the NUMBER format: ")
    pieces = input("Enter pieces of goods: ")
    if pieces.isdigit() == False:
        while pieces.isdigit() == False:
            pieces = input("Enter pieces of goods in the NUMBER format: ")
    exit = input("If there is no any goods, please enter 'q': ")
    product = (i, {"name": name, "price": price, "quantity": quantity, "pieces": pieces})
    goods.append(product)
    if exit.lower() == "q":
        break
print(goods)

dict_prod = {}
i = 0
#Передача значений в словарь
for product in goods:
    for key, value in product[1].items():
        if i > 0: #После того, как создали список, добавляем в него значения из других словарей
            dict_prod[key].append(value)
        else: #Если записываем первый раз данные в словарь, то в значении создаем список для каждого ключа
            value = value.split()
            dict_prod.setdefault(key, value)
    i += 1
print(dict_prod)

