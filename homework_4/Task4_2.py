#Задание 2. Напишите функцию принимающую на вход 
# только ключевые параметры и возвращающую словарь, 
# где ключ — значение переданного аргумента, а 
# значение — имя аргумента. Если ключ не хешируем, 
# используйте его строковое представление.

def dict_func(**kwargs) -> dict:
   
    return_dict = {}
    for key, value in kwargs.items():
        if value.__hash__ is None:
            return_dict[str(value)] = key
        else:
            return_dict[value] = key

    return return_dict


result = dict_func(num=19, my_text=[1, 5, 7], str_word='Hello world!', n=(1, 2, 3), sh=6)
print(result)