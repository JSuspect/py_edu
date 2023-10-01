def invest(amount, rate, years):
    first_year = 1
    print('\n'*3,'#'* 50, 'Итого основные входные данные:')
    print(f'Основная сумма: {amount} \nГодовой процент: {rate} \nВклад внесен на количество лет: {years}')
    while first_year <= years:
        amount = amount + (amount / 100 * rate)
        print (f'years {first_year:>3}: ${amount:>20,.2f}')
        first_year += 1


a = float(input('Введите основную сумму: '))
r = int(input('Введите годовой процент: '))
y = int(input('Введите на сколько лет вы вносите вклад: '))

invest(a, r, y)