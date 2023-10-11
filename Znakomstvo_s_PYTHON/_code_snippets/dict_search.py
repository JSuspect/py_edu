# Задача перебрать словарь 'capitals' и вывести пару ключ-значение.
capitals = {
    'New York': 'Albany',
    'California': 'Sacramento',
    'Texas': 'Austin',
    'Florida': 'Tallahassee',
}

# Для распаковки значений из словаря в Python, 
# вы можете использовать цикл for, чтобы перебрать 
# ключи и значения словаря. Вот пример:
my_dict = {'a': 1, 'b': 2, 'c': 3}

for key, value in my_dict.items():
    print(f"Key: {key}, Value: {value}")

# Также, если вам нужны только значения словаря (а не ключи), 
# вы можете использовать метод values():
my_dict = {'a': 1, 'b': 2, 'c': 3}

for value in my_dict.values():
    print(f"Value: {value}")

# Если вам нужны только ключи, вы можете использовать метод keys():
my_dict = {'a': 1, 'b': 2, 'c': 3}

for key in my_dict.keys():
    print(f"Key: {key}")


# При переборе capitals.items() каждая итерация цикла создает кортеж, содержащий название штата и его столицы. 
# Присваивание этого кортежа state, capital обеспечивает распаковку компонентов в переменные state и capital.
# Чтобы каждая пара ключ-значение выводилась заданное количество раз:
iterations = 3  # Задайте желаемое количество итераций
count = 0  # Инициализируем счетчик

for state, capital in capitals.items():
    if count >= iterations:
        break  # Выходим из цикла, если достигнуто заданное количество итераций
    for _ in range(iterations):
        print(f"The capital of {state} is {capital}")
    count += 1

# или
for state, capital in capitals.items():
    q = 0  # Инициализируем счетчик для while
    while q < 3:
        print(f"The capital of {state} is {capital}")
        q += 1


# Если вы хотите, чтобы каждая пара ключ-значение выводилась только один раз, 
# и при этом управлять общим количеством пар, которые нужно вывести, 
# вы можете воспользоваться следующим кодом:
pairs_to_print = 3  # Задайте желаемое количество пар для вывода
count = 0  # Инициализируем счетчик

for state, capital in capitals.items():
    if count >= pairs_to_print:
        break  # Выходим из цикла, если достигнуто заданное количество пар
    print(f"The capital of {state} is {capital}")
    count += 1
