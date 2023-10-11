import random

print(
    '\n'*2,
    '*'*20,
    'Угадай число', 
    '*'*20
      )

print('\nКомпьютер генерирует случайное число в диапозоне от 1 до 10. Необходимо отгадать число. Для выхода ввделите "0"\n')


score = 0
count_iter = 0
answer = 1

while answer:
    rand = random.randint(1, 10)
    try:
        answer = int(input('Отгадайте число: '))
    except ValueError:
        print('Нужно вводить число!\n')
        continue
    if answer == 0:
        break
    elif answer == rand:
        count_iter += 1
        score += 1
        print(f'Правильно! Ваш счет {score} из {count_iter}')
    else:
        count_iter += 1
        print('Попробуйте еще раз!\n')

print(f'\nВаш счет {score} из {count_iter}')
print(
    '\n'*2,
    '*'*20,
    'До встречи!', 
    '*'*20
      )
