import csv



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



