import random


def roll():
    score = random.randint(1, 6)
    return score

num_rolls = 10_000
total = 0

for trial in range(num_rolls):
    total = total + roll()

avg_roll = total / num_rolls

print(f"The average result of {num_rolls} rolls is {avg_roll}")

