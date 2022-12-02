""" Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор
 натуральных чисел. У пользователя необходимо запрашивать новый элемент
  рейтинга. Если в рейтинге существуют элементы с одинаковыми значениями,
  то новый элемент с тем же значением должен разместиться после них."""
def function():
    while True:
        try:
            x = int(input("Введите число :"))
        except ValueError:
            print("Error! Это не число, попробуйте снова.")
        else:
            return x
my_list = [7, 5, 4, 4, 3]
rtg = function()
print(my_list)
#print(my_list.count(rtg))
if my_list.count(rtg)!=0:
    my_list.reverse()
    my_list.insert(my_list.index(rtg), rtg)
    my_list.reverse()
elif rtg>my_list[0]:
    my_list.insert(0, rtg)
else:
    my_list.append(rtg)
print(my_list)


