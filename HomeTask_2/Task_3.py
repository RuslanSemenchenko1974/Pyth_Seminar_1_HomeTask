"""Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому
 времени года относится месяц (зима, весна, лето, осень). Напишите решения
 через list и через dict. """


def function():
    while True:
        try:
            x = int(input("Введите месяц :"))
        except ValueError:
            print("Error! Это не число, попробуйте снова.")
        else:
            return x


us_month_number = 0
while 0 >= us_month_number or us_month_number >= 13:
    us_month_number = function()
    if 0 >= us_month_number or us_month_number >= 13:
        print('Неправильно')

month_list = ['Январь', 'Февраль', 'Март', "Апрель", 'Май', 'Июнь', 'Июль',
              'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь']
seson = {1: 'Зима', 2: 'Зима', 3: 'Весна', 4: 'Весна', 5: 'Весна', 6: 'Лето',
         7: 'Лето', 8: 'Лето', 9: 'Осень', 10: 'Осень', 11: 'Осень',
         12: 'Зима'}
print(month_list[us_month_number - 1], end=' : ')
print(seson.get(us_month_number))
