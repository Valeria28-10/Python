# Задание 3. 
# В большой текстовой строке подсчитать количество 
# встречаемых слов и вернуть 10 самых частых. 
# Не учитывать знаки препинания и регистр символов. 
# За основу возьмите любую статью из википедии или 
# из документации к языку.

text = "Python (МФА: в русском языке встречаются названия пито́н или па́йтон) " \
    "— высокоуровневый язык программирования общего назначения с динамической строгой типизацией и автоматическим управлением памятью, " \
    "ориентированный на повышение производительности разработчика, читаемости кода и его качества, а также на обеспечение переносимости написанных на нём программ. " \
    "Язык является полностью объектно-ориентированным в том плане, что всё является объектами. Необычной особенностью языка является выделение блоков кода отступами. " \
    "Синтаксис ядра языка минималистичен, за счёт чего на практике редко возникает необходимость обращаться к документации. " \
    "Сам же язык известен как интерпретируемый и используется в том числе для написания скриптов. " \
    "Недостатками языка являются зачастую более низкая скорость работы и более высокое потребление памяти написанных на нём программ по сравнению с аналогичным кодом, " \
    "написанным на компилируемых языках, таких как C или C++. "

WORD_LIST = 10

text = text.lower().replace('.', '').replace(',', '').replace('[', ' [')
list_word = text.split()
dict_word = {}

for item in list_word:
    if item not in dict_word:
        dict_word[item] = list_word.count(item)
count = 0
print(f'{WORD_LIST} часто встречающихся слов в тексте: ')
while len(dict_word) != 0 and WORD_LIST > count:
    for item in dict_word:
        if dict_word[item] == max(dict_word.values()):
            print(f'{dict_word[item]} - слово: "{item}"\n')
            if len(dict_word) != 1 and WORD_LIST > count+1:
                print('', end='')
            dict_word.pop(item)
            count += 1
            break
