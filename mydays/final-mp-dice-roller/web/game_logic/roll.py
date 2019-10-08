from random import  randint

def die_roll():
    return randint(1,6)


def total_dice_rolls(num_dice):
    total = 0
    for _ in range(num_dice):
        total += die_roll()

    return total


if __name__ == "__main__":
    num_rolls = 4
    player_score = total_dice_rolls(num_rolls)
    computer_score = total_dice_rolls(num_rolls)

    print(f"Player Score: {player_score}")
    print(f"Computer Score: {computer_score}")

    if player_score > computer_score:
        print("Yay you won!")
    else:
        print("Sorry. You lost!")

