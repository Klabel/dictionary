import csv
import random
from datetime import datetime

from prob import load_data


def fill_dictionary(words):
    more = '1'
    while more == "1":
        print('вводим новые слова в словарь')
        date_now = datetime.now()
        eng_word = input('введите слово на изучаемом языке ').strip()
        if eng_word in words:
            print('слово есть в словаре ')
            continue
        rus_word = input('введите перевод ').strip()
        words[eng_word] = rus_word
        more = input('ввести еще слово, 1 да, 0 нет.')
        dict_file = open('dict.csv', 'a')
        w = csv.writer(dict_file)
        w.writerow([eng_word, rus_word, date_now])
        dict_file.close()


words = load_data()

mode = input('пополнить словарик? да - y, нет - no ')
if mode == 'y':
    fill_dictionary(words)
if not words:
    print("нет слов в словаре, надо заполнить слова!")
    fill_dictionary(words)
datetime.today()

print('сейчас проверим слова')
more = '1'
while more == '1':
    word_with_translation = list(random.choice(list(words.items())))  # получаем список из ключа и значения
    random.shuffle(word_with_translation)  # перемешиваем список
    word, translation = word_with_translation  # присваиваем список строчкой выше (распаковка списка)
    print('введите перевод слова {word}'.format(word=word))
    input_value = input('введите перевод ')
    if input_value == translation:
        print('зер гуд')
    else:
        print('правильно - ', translation, 'учи дальше')

    more = input('еще? 1-да, 0-нет')

    # дата ввода слов.
    # проверка на повторы
    # режим проверки слов.
    # радомная проверка слов
    # проверить 5 слов перед вводом слов
