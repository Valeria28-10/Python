# Напишите программу, которая принимает две строки вида "a/b" - дробь с числителем и знаменателем. 
# Программа должна возвращать сумму и произведение* дробей. 
# Для проверки своего кода используйте модуль fractions.  

from fractions import Fraction
import math

# Наименьший общий делитель x
def common_divisor_number(numerator, denominator):
    if denominator == 0:
        return numerator
    return common_divisor_number(denominator, numerator % denominator)

x = input('Введите 1 строку вида a/b: ')
# Сплитирование x
x_numerator, x_denominator = (int(num) for num in x.split('/'))
while x_denominator == 0:
    x = input('Вы ошиблись! Делить на 0 нельзя: \nВведите 1 строку вида a/b: ')
    x_numerator, x_denominator = (int(num) for num in x.split('/'))
    
y = input('Введите 2 строку вида a/b: ')
# Сплитирование y
y_numerator, y_denominator = (int(num) for num in y.split('/'))
while y_denominator == 0:
    y = input('Вы ошиблись! Делить на 0 нельзя: \nВведите 2 строку вида a/b: ')
    y_numerator, y_denominator = (int(num) for num in y.split('/'))

# Сумма дробей
numerator = x_numerator * y_denominator + x_denominator * y_numerator
denominator = x_denominator * y_denominator

nod = common_divisor_number(numerator, denominator)
result = f'{numerator // nod}/{denominator // nod}'
print(f'Сумма дробей равна: {result}')

# Произведение дробей
numerator = x_numerator * y_numerator
denominator = x_denominator * y_denominator

nod = common_divisor_number(numerator, denominator)
result = f'{numerator // nod}/{denominator // nod}'
print(f'Результат произведения дробей, равен: {result}')

# Проверка с использованием модуля fractions 
sum_Fraction = Fraction(x) + Fraction(y)
print(f'Результат суммы дробей используя модуль fractions, равен: {sum_Fraction}')
product_Fraction = Fraction(x) * Fraction(y)
print(f'Результат произведения дробей используя модуль fractions, равен: {product_Fraction}')