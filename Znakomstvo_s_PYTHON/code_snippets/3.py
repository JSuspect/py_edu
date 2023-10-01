# Это пример как использовать цикл while вместо for
word = 'Pythonyashka'
index = 0

while index < len(word):
    print(word[index])
    index += 1


# Функция range
print('#'*30, 'this is divider', '#'*30)

for i in range(5, 10):
    print(i)

for count in range(10):
    print(word)
    print("Это вывод переменной count:", count)


# Программа, которая считает сумму введенную пользователем (3 раза)
# и делит ее между 2, 3 , 4 и 5 людьми
print('#'*30, 'this is divider', '#'*30)

i = 2
while i >= 0:
    amount = float(input('Введите потрченную сумму: '))
    for num_people in range(2, 6):
        print(f'{num_people} people: ${amount /num_people:,.2f} eath')
    i -= 1