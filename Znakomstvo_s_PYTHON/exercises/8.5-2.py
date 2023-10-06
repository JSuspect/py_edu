for i in range(1, 51):
    if i % 3 == 0:
        continue
    else:
        print(f'число {i} не кратно трем!')


# Exercise 2
# Display every number from 1 through 50 except multiples of 3
for i in range(1, 51):
    if i % 3 == 0:
        continue
    print(i)