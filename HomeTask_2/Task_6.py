"""Реализовать структуру данных «Товары». Она должна представлять собой
список кортежей. Каждый кортеж хранит информацию об отдельном товаре.
В кортеже должно быть два элемента — номер товара и словарь с параметрами
(характеристиками товара: название, цена, количество, единица измерения).
Структуру нужно сформировать программно, т.е. запрашивать все данные у
пользователя."""


def functionPrice():
    while True:
        try:
            x = int(input("Введите цену товара :"))
        except ValueError:
            print("Error! Это не число, попробуйте снова.")
        else:
            return x


def function():
    while True:
        try:
            x = int(input("Введите количество товаров :"))
        except ValueError:
            print("Error! Это не число, попробуйте снова.")
        else:
            return x


qty = function()
lst = []
for i in range(qty):
    print(f"Ведите {i + 1} товар : ")
    l1 = {}
    l1['Название'] = input('Введите название : ')
    l1['Цена'] = functionPrice()  # input('Введите цену: ')
    l1['Количество'] = function()  # input('Введите количество :')
    l1['ед'] = input('Введите единицу измерения : ')
    item = (i, l1)
    lst.append(item)
    del item
print(lst)
sort_dict = {}
list_of_property = ['Название', 'Цена', 'Количество', 'ед']
for name in list_of_property:
    list_of_item = []
    for i in range(qty):
        list_of_item.append(lst[i][1].get(name))
    sort_dict[name] = list_of_item
print(sort_dict)
