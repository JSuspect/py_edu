# Необходимо, с помощью генератора списка, создать список "indexes", 
# содержащий индексы списка "food".


# Этот код использует генератор списка и функцию enumerate, чтобы создать список индексов элементов из списка food.
food = ['rice', 'beans', 'rice', 'beans', 'rice', 'beans']
indexes = [index for index, item in enumerate(food)]
print(indexes)


# Конечно, можно создать список индексов элементов списка food без использования функции enumerate следующим образом:
food = ['rice', 'beans', 'rice', 'beans', 'rice', 'beans']
indexes = [i for i in range(len(food))]
print(indexes)

