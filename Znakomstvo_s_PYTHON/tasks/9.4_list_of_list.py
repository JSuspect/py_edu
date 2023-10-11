universities = [
['California Institute of Technology', 2175, 37704],
['Harvard', 19627, 39849],
['Massachusetts Institute of Technology', 10566, 40732],
['Princeton', 7802, 37000],
['Rice', 5879, 35551],
['Stanford', 19535, 40569],
['Yale', 11701, 40500]
]

# Определите функцию enrollment_stats(), получающую один параметр. Этим
# параметром должен быть список списков, в котором каждый вложенный список
# содержит три элемента:
# 1) название университета;
# 2) общее количество зачисленных студентов;
# 3) ежегодная плата за обучение.
# Функция enrollment_stats() должна возвращать два списка. Первый содер-
# жит все данные о зачисленных зарегистрированных студентах, а второй — все
# данные о плате за обучение.


def enrollment_stats(lol):
    # Список данных о зачисленных студентов сделан через for
    # Список данных об оплате сделан через генератор
    num_enrolled_students = []
    for i in lol:
        num_enrolled_students.append(i[1])

    tuition_fees = [num[2] for num in lol]

    return num_enrolled_students, tuition_fees

student, tuiotion = enrollment_stats(universities)

def mean(avg):
    result = int(sum(avg) / len(avg))
    return result

def median(input_list):
    # Сначала сортируем список
    sorted_list = sorted(input_list)

    # Находим длину списка
    list_length = len(sorted_list)

    # Проверяем, является ли длина списка четной или нечетной
    if list_length % 2 == 0:
        # Если длина четная, берем среднее двух центральных элементов
        middle1 = sorted_list[list_length // 2 - 1]
        middle2 = sorted_list[list_length // 2]
        median = (middle1 + middle2) / 2
    else:
        # Если длина нечетная, берем центральный элемент
        median = sorted_list[list_length // 2]

    return median

print('*' * 20)
print("Total students: ", sum(student))
print("Total tuiotion: $", sum(tuiotion))


print("Student mean: ", mean(student))
print("Student median: ", median(student))

print("Tuiotion mean: $", mean(tuiotion))
print("Tuiotion median: $", median(tuiotion))
print('*' * 20)
