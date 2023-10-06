# 8.4 - Challenge: Find the Factors of a Number
# Solution to challenge

# Display all the factors of a number chosen by the usern
number = int(input('Введите положительное число:'))


for num in range(1, number + 1):
    res_fac = number % num
    if res_fac == 0:
        print(f'{num} is a factor of {number}')