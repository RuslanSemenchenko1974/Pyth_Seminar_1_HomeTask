"""Ввод числа с клавиатуры с проверкой ввода"""
def function():
    while True:
        try:
            x = int(input("Введите число"))
        except ValueError:
            print("Error! Это не число, попробуйте снова.")
        else:
            return x

a=function()
