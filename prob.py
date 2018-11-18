import csv


more = '1'
def load_data():
    data = {}
    with open('dict.csv') as f:
        read_file = csv.reader(f)
        for row in read_file:
            if not row:#проверка на пропущенные строки
                continue
            key = row[0]
            walue = row[1]
            data[key] = walue#присваивание переменных с ключем и значением
    return data

if __name__ =="__main__":
    words = load_data()

    dict_file = open('dict.csv', 'a')
    w = csv.writer(dict_file)
    print("проверка слов")
    for i in range(4):

        key = input('введите английское слово ')
        value = input('введите перевод ')
        if key in words and value == words[key]:#сверяем значение с ключем
            print("правильно")
        else:
            print('ошибка')