# 1. Бросить монету.
# 2. Если монета упала орлом вверх, обновить счетчик орлов. Если монета упала решкой вверх, обновить счетчик решек.

import random

def coin_flip():
    """Возвращает случайно выбранную строку 'heads' или 'tails'."""
    if random.randint(0, 1) == 0:
        return "heads"
    else:
        return "tails"
    

heads_tally = 0
tails_tally = 0

for trial in range(1000000):
    if coin_flip() == "heads":
        heads_tally += 1
    else:
        tails_tally += 1

ratio = heads_tally / tails_tally
print(f"The ratio of heads ({heads_tally}) to tails ({tails_tally}) is {ratio}")