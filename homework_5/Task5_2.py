# Задание 2. Напишите функцию, которая принимает на вход строку - 
# абсолютный путь до файла. Функция возвращает кортеж из трёх элементов: 
# путь, имя файла, расширение файла.

import os

string = "F:\Python\homework_5\Task5_2.py"

def fun(f_path: str) -> tuple:
    path, filename = os.path.split(f_path)
    name, extension = filename.split('.')
    return path, name, extension

print(f'Исходная строка: {string} \nКортеж из адреса: {fun(string)}')