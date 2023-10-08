import random

def unfair_coin_flip(probability_of_tails):
    if random.random() < probability_of_tails:
        return "tails"
    else:
        return "heads"
    
heads_tally = 0
tails_tally = 0

while True:
    try:
        float_num = float(input('Введите коэффицент от "0.0" до "1.0": '))
        break
    except ValueError:
        print('Необходимо ввести значение "0.0" до "1.0"!', '\n')

for trial in range(10000):
    if unfair_coin_flip(float_num) == 'tails':
        tails_tally += 1
    else:
        heads_tally += 1

ratio = heads_tally / tails_tally

print(f"The ratio of heads ({heads_tally}) to tails ({tails_tally}) is {ratio}")