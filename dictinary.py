import csv
import random
from datetime import datetime

from prob import load_data

def fill_dictionary(words):
    more = '1'
    while more == "1":
        print('вводим новые слова в словарь')
        date_now = datetime.now()
        eng_word = input('введите слово на ')
        if eng_word in words:
            print('слово 1есть в словаре ')
            continue
        rus_word = input('введите перевод ')
        words[eng_word] = rus_word
        more = input('ввести еще слово, 1 да, 0 нет.')
        dict_file = open('dict.csv', 'a')
        w = csv.writer(dict_file)
        w.writerow([eng_word, rus_word, date_now])
        dict_file.close()

words = load_data()

mode = input('вводим словарик - y, no - нафиг ')
if mode == 'y':
    fill_dictionary(words)




datetime.today()


print('сейчас проверим слова')
more = '1'
while more == '1':
    key, trans_value = random.choice(list(words.items()))
    print('введите перевод слова {word}'.format(word=key))
    input_value = input('введите перевод ')
    if input_value == trans_value:
        print('зер гуд')
    else:
        print('учи дальше')

    more = input('еще слово или спать пойдешь? 1-да, 0-нет')

# дата ввода слов.
# проверка на повторы
# режим проверки слов.
# радомная проверка слов
# проверить 5 слов перед вводом слов