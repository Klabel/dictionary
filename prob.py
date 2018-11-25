import csv

import os


def load_data():
    data = {}
    file_name = 'dict1.csv'
    if not os.path.isfile(file_name):
        f = open(file_name, 'w')
        f.close()
        return data
    with open(file_name) as f:
        read_file = csv.reader(f)
        for row in read_file:
            if not row:  # проверка на пропущенные строки
                continue
            key = row[0]
            walue = row[1]
            data[key] = walue  # присваивание переменных с ключем и значением
    return data
