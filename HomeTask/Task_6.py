""" Спортсмен занимается ежедневными пробежками. В первый день его результат
 составил a километров. Каждый день спортсмен увеличивал результат на 10 %
 относительно предыдущего. Требуется определить номер дня, на который
 результат спортсмена составит не менее b километров. Программа должна
 принимать значения параметров a и b и выводить одно натуральное число —
 номер дня."""

distance1 = float(input('Введите расстояние в 1 день : '))
distance2 = float(input('Введите расстояние в последний день : '))
i = 0
while distance1 < (distance2+distance2*0.1):
    i += 1
    print(f' {i}-й день  : {round(distance1, 2)}')
    distance1 += distance1 * 0.1
print(f'Ответ: на {i}-й день спортсмен достиг результата — не менее \
{distance2} км')
