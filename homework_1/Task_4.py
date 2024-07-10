# Задание 4.
# Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток.
# Программа должна подсказывать “больше” или “меньше” после каждой попытки. 
# Для генерации случайного числа используйте код:
# from random import randintnum = rand
# int(LOWER_LIMIT, UPPER_LIMIT)

from random import randint

LOWER_LIMIT = 0
UPPER_LIMIT = 1000
COUNTER = 10

num = randint(LOWER_LIMIT, UPPER_LIMIT)

for i in range(COUNTER):
    new_num = int(input(f'Угадайте число. Ваша {i+1} попытка: '))
    if num > new_num:
        print('Введите большее число')
    elif num < new_num:
        print('Введите меньшее число')
    else:
        print('Получилось! Вы угадали')
        break
else:
    print(f'Попытки исчерпаны. Число было {num}')