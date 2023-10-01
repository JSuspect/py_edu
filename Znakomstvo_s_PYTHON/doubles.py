# Увеличиваем введенное число пользователем в 2 раза и выводим результат
# Используем цикл, цикл будет работать 5 раз
def doubles(i):
    result = i * 2
    print(result)
    return result

num = int(input('Введите число, которое будет учеличено в 2 раза: '))
count = 0
while count < 5:
    num = doubles(num)
    count += 1
