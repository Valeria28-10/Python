# Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление. 
# Функцию hex используйте для проверки своего результата.  
 
DIV_HEX = 16

original_num: int = int(input("Введите целое число: "))

hex_str = '0123456789ABCDEF'
result: str = ''
while original_num >= DIV_HEX:        
    result += hex_str[original_num % DIV_HEX]
    original_num = original_num // DIV_HEX
result += hex_str[original_num % DIV_HEX]
print(f"Результат в шестнадцатеричной системе счисления, равен: ", result[::-1])

result_hex = hex(original_num)
print(f'Результат в шестнадцатеричной системе счисления используя Функцию hex, равен: {result_hex}')