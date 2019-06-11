from random import random

from prompt_toolkit import prompt

class Player():
    def __init__(self, name):
        self.player_name = name




class Roll():
    def __init__(self, name):
        self.name = name
        self.rolls_i_can_beat = []
        self.rolls_that_beat_me = []

    def __repr__(self):
        return self.name


def build_the_three_rolls():
    rock = Roll("Rock")
    paper = Roll("Paper")
    scissors = Roll("Scissors")

    rock.rolls_i_can_beat = [scissors]
    rock.rolls_that_beat_me = [paper]
    paper.rolls_i_can_beat = [rock]
    paper.rolls_that_beat_me = [scissors]
    scissors.rolls_i_can_beat = [paper]
    scissors.rolls_that_beat_me = [rock]

    return rock, paper, scissors


def game_loop(player1, player2, rolls):
    count = 1
    while count < 3:

        three_rolls = build_the_three_rolls()

        p2_roll = three_rolls[round(random() * 2)]

        p1_roll = three_rolls[round(random() * 2)]

        # outcome = p1_roll.can_defeat(p2_roll)

        print(f"Player 1 rolled: {p1_roll}")
        print(f"Player 2 rolled: {p2_roll}")
        # display winner for this round

        count += 1

    # Compute who won


def print_header():
    print("Welcome to Rock, Paper, Scissors! Python edition :)")


def get_players_name():
    return(prompt("Please enter your name: "))


def main():
    print_header()

    rolls = build_the_three_rolls()
    print(rolls)

    name = get_players_name()

    player1 = Player(name)
    player2 = Player("computer")

    # Doesn't work yet :)
    game_loop(player1, player2, rolls)


if __name__ == "__main__":
    main()
