import random


def roll():
    if random.randint(0, 1) == 0:
        return "heads"
    else:
        return "tails"

trial = 10_000
flips = 0

for i in range(trial):
    if roll() == 'heads':
        flips += 1
        
        while roll() == 'heads':
            flips += 1

        flips += 1
    else:
        flips += 1

        while roll() == 'heads':
            flips += 1

        flips += 1

avg_flips_per_trial = flips / trial
print(f"The average number of flips per trial is {avg_flips_per_trial}.")