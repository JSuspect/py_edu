import random


num_times_A_wins = 0
num_times_B_wins = 0


trial = 10_000

for i in range(trial):
    vote_candidat_a = 0
    vote_candidat_b = 0
    # Первый участок
    if random.random() < .87:
        vote_candidat_a += 1
    else:
        vote_candidat_b += 1

    # Второй участок
    if random.random() < .65:
        vote_candidat_a += 1
    else:
        vote_candidat_b += 1

    # Третий участок
    if random.random() < .17:
        vote_candidat_a += 1
    else:
        vote_candidat_b += 1

    if vote_candidat_a > vote_candidat_b:
        num_times_A_wins += 1
    else:
        num_times_B_wins += 1


print(f"Probability A wins: {num_times_A_wins / trial}")
print(f"Probability B wins: {num_times_B_wins / trial}")
