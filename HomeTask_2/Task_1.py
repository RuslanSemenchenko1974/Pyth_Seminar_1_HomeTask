""" Создать список и заполнить его элементами различных типов данных.
Реализовать скрипт проверки типа данных каждого элемента. Использовать
функцию type() для проверки типа. Элементы списка можно не запрашивать у
пользователя, а указать явно, в программе."""

my_list = [2, 'text', 456, 45.3, None, "Проверка", True, 's']
for j, i in enumerate(my_list):
    print(j, type(i))