print('='*30, 'Задание 1', '='*30)
num1 = int(input('число 1: '))
num2 = int(input('число 2: '))
res = f'если умножить {num1} на {num2} то получится {num1 * num2}'
print(res)




print('\n'*3, '='*30, 'Задание 2', '='*30)
txt = 'пол, стул, стол - это просто СЛОВА для примера'
txt2 = txt.find('ол')
print('это резутьтат работы метода find("ол")', txt2)

txt3 = txt.replace('ол', 'ОЛ')
print('это результат txt3: ', txt3)


