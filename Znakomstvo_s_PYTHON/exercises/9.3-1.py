data = (1, 3), (3, 4), (7, 2), (6, 3)

# Solution 1
row = 0
for i in data:
    sum = i[0] + i[1]
    row += 1
    print(f'Row {row} sum: {sum}')

# Solution 2
index = 1
for row in data:
    print(f"Row {index} sum: {sum(row)}")
    index += 1
