import random

capitals_dict = {
    'Россия': 'Москва',
    'Украина': 'Киев',
    'Беларусь': 'Минск',
    'Казахстан': 'Нур-Султан',
    'Узбекистан': 'Ташкент',
    'Таджикистан': 'Душанбе',
    'Киргизия': 'Бишкек',
    'Армения': 'Ереван',
    'Азербайджан': 'Баку',
    'Грузия': 'Тбилиси',
    'Молдавия': 'Кишинев',
    'Литва': 'Вильнюс',
    'Латвия': 'Рига',
    'Эстония': 'Таллин',
    'Туркмения': 'Ашхабад',
    'Туркция': 'Анкара',
    'Иран': 'Тегеран',
    'Афганистан': 'Кабул',
    'Пакистан': 'Исламабад',
    'Китай': 'Пекин'
}

capitals_keys = []
positive_answer = ['yes', 'y', 'да'] 
negative_answer = ['no', 'n', 'нет'] 
exit_answer = ['exit', 'e', '']
game_on = True

for key in capitals_dict.keys():
    capitals_keys.append(key)

play_offer = input(f'\nЭта программа случайным образом выбирает страну из списка {len(capitals_keys)} и просит в ответ ввести название ее столицы.\n\nХотите попробовать сыграть? (Да/Нет): ')

while game_on:
    if play_offer.lower() in positive_answer:

        while True:
            random_key = random.choice(capitals_keys)
            random_key_value = capitals_dict[random_key]
            user_answer = input(f'\nВам выпала страна:{random_key}\nДля выхода из игры введите "Enter" или "Exit". \nДля продолжения игры ввведите столицу страны {random_key}: ')

            if user_answer.lower() in exit_answer:
                print('\n', '='*20, 'Exit', '='*20)
                game_on = False
                break
            elif user_answer.lower() == random_key_value.lower():
                print('\n', '*'*20,'Верно', '*'*20)
            else:
                print('\n', '*'*20,'Неверно', '*'*20)
                play_offer = input(f'\nВы блин, не знали, что столица {random_key} - это {random_key_value}\nПопробуем еще раз? (Да/Нет): ')
                break

    elif play_offer in negative_answer:
        print('\nНу может в следующий раз ;)\n')
        break
    elif play_offer == '':
        play_offer = input(f'\nВы ничего не ввели. Не тупите! Введите Да/Нет: ')
    else:
        play_offer = input(f'\nВы ввели: "{play_offer}". Не тупите! Введите Да/Нет: ')
