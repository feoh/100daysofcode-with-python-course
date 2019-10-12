from random import  randint

def die_roll():
    return randint(1,6)


def total_dice_rolls(num_dice):
    total = 0
    for _ in range(num_dice):
        total += die_roll()

    return total

