word = input('Введите слово:')
if len(word) == 5:
    print('Длина ввода составляет 5 символов')
elif len(word) >= 5:
    print('Длина ввода, больше 5 символов')
else:
    print('Длина ввода, меньше 5 символов')