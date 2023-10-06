print('для выхода их программы нажмите: "q" "Q"', )
while True:
    word = input('Введите слово:')
    if word.lower() == 'q':
        print('EXIT')
        break
    print('вы ввели:', word)


