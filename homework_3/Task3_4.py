# Задание 4. 
# Создайте словарь со списком вещей для похода в качестве
# ключа и их массой в качестве значения. Определите какие
# вещи влезут в рюкзак передав его максимальную
# грузоподъёмность. Достаточно вернуть один допустимый вариант.


MAX_BACKPACK = 20

things = {'рюкзак': 2, 'котелок': 1, 'палатка': 9, 'спальник': 5, 'еда': 5, 'одежда': 4, 'обувь': 1, 'вода': 2}

weight_things = 0
print(f'Список вещей для похода: {things}')
print(f'Список вещей по максимально возможной загрузке рюкзака весом в {MAX_BACKPACK} кг: ')

things_list = list(things.items())
things_list.sort(key = lambda x: x[1])

for thing in things_list:
    if thing[1] + weight_things <= MAX_BACKPACK:
        weight_things += thing[1]
    else:
        things.pop(thing[0])
print(things)

print(f'Общий вес рюкзака c вещами: {weight_things} кг')

