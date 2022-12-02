"""Для списка реализовать обмен значений соседних элементов, т.е. значениями
обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д. При нечетном количестве
 элементов последний сохранить на своем месте. Для заполнения списка элементов
 необходимо использовать функцию input()."""


def function():
    while True:
        try:
            x = int(input("Введите количество элемнтов массива :"))
        except ValueError:
            print("Error! Это не число, попробуйте снова.")
        else:
            return x


qty = function()
my_list = list()
for i in range(qty):
    print(f'Введите {i} элемент : ')
    my_list.append(input())
print(my_list)
for i in range(0, qty - 1, 2):
    temp = my_list[i]
    my_list[i] = my_list[i + 1]
    my_list[i + 1] = temp
print(my_list)
