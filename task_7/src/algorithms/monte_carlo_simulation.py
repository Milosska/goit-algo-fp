import random


def monte_carlo_simulation(num_trials: int) -> dict[int, float]:
    sums = {i: 0.0 for i in range(2, 13)}

    for _ in range(num_trials):
        dice_1 = random.randint(1, 6)
        dice_2 = random.randint(1, 6)
        roll_sum = dice_1 + dice_2
        sums[roll_sum] += 1

    for total_key in sums:
        sums[total_key] /= num_trials

    return sums
