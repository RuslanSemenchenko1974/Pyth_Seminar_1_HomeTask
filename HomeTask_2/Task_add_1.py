"""Напишите программу, которая принимает на вход вещественное
число и показывает сумму его цифр"""


def function():
    while True:
        try:
            x = float(input("Введите число :"))
        except ValueError:
            print("Error! Это не число, попробуйте снова.")
        else:
            return x


namber = function()
if int(namber) < namber:
    while int(namber) != namber:
        namber *= 10
namber = int(namber)

temp=0
while namber > 0:
    temp = temp + namber % 10
    namber = namber // 10
print(f'Сумма цыфр : {temp}')
