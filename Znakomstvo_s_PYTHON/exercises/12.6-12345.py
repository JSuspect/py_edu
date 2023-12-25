import pathlib
import csv

file_path = pathlib.Path.home() / 'slink/wsld' / 'practice_files' / 'numbers.csv'

file_path.parent.mkdir(parents=True, exist_ok=True)
file_path.touch()

# 1 Напишите программу, которая записывает следующий список списков в файл numbers.csv
numbers = [
[1, 2, 3, 4, 5],
[6, 7, 8, 9, 10],
[11, 12, 13, 14, 15],
]

with file_path.open(mode='r+', encoding='utf-8', newline='') as file:
    csv_writer = csv.writer(file)
    csv_writer.writerows(numbers)


# 2 Напишите программу, которая читает числа в файле numbers.csv из упражнения 1 в список списков целых чисел с именем numbers
numbers_list = []

with file_path.open(mode='r', encoding='utf-8', newline='') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        numbers = [int(i) for i in row]
        numbers_list.append(numbers)


# 3 Напишите программу, которая записывает следующий список словарей в файл favorite_colors.csv
file_path_2 = pathlib.Path.home() / 'slink/wsld' / 'practice_files' / 'favorite_colors.csv'

favorite_colors = [
{"name": "Joe", "favorite_color": "blue"},
{"name": "Anne", "favorite_color": "green"},
{"name": "Bailey", "favorite_color": "red"},
]

with file_path_2.open(mode='w', encoding='utf-8', newline='') as file:
#    writer = csv.DictWriter(file, fieldnames=favorite_colors[0].keys())
    writer = csv.DictWriter(file, fieldnames=favorite_colors[0].keys())
    writer.writeheader()
    writer.writerows(favorite_colors)


# 5 Напишите программу, которая читает данные из файла favorite_colors.csv (см. упражнение 3) в список словарей favorite_colors.
list_read_csv = []

with file_path_2.open(mode='r', encoding='utf-8', newline='') as file:
    reader = csv.DictReader(file)
    for row in reader:
        list_read_csv.append(row)

print(list_read_csv)