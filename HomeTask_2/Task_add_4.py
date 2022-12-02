"""Задайте список из N элементов, заполненных числами из промежутка [-N, N].
Найдите произведение элементов на указанных позициях. Позиции хранятся в
файле file.txt в одной строке одно число."""

def function():
    while True:
        try:
            x = int(input("Введите число  N :"))
        except ValueError:
            print("Error! Это не число, попробуйте снова.")
        else:
            return x


n = function()
my_list = []
i = -n
while i <= n:
    my_list.append(i)
    i += 1
print(my_list)
path = 'file.txt'
s = 1
list_pos = []
data = open(path, 'r')
for line in data:
    if int(line) <= 2 * n - 1:
        s = s * my_list[int(line) - 1]
        list_pos.append(my_list[int(line) - 1])
    else:
        print(f"В списке нет позиции {int(line)}")
data.close
print(f"Произведение чисел {list_pos} = {s}")
