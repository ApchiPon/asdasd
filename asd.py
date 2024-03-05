import csv

fio = input('Введите ФИО человека: ')

with open('FIOandTelephone.csv', "r", encoding="utf-8") as file:
    reader = csv.DictReader(file, ["FIO", 'Telephone'])
    for row in reader:
        if fio == row['FIO']:
            print('Номер телефона: ', row['Telephone'])
            break
    else:
        print('Нет в телефонной книге')
