"""Напишите программу, которая принимает на вход число N и выдает
набор произведений чисел от 1 до N"""


def function():
    while True:
        try:
            x = int(input("Введите число :"))
        except ValueError:
            print("Error! Это не число, попробуйте снова.")
        else:
            return x

namber = function()
i = 1
temp = 1
while i != namber:
    i = i + 1
    temp *= i
print(temp)
