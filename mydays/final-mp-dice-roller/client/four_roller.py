from roller_client import RollerService
from sys import exit

def main():
    rsvc = RollerService("http://localhost:5000")

    print("Four Dice Roller! by Chris Patti")
    print("--------------------------------")
    print("\n\n")

    player_name=input("Please enter your name. We'll create an account for you if you don't have ona already:")
    current_player = rsvc.find_player(name=player_name)

    if not current_player:
        print(f"Hi {player_name}! Welcome to Four Roller!")
        current_player = rsvc.create_player(player_name)

    player_score = rsvc.roll_turn(num_dice=4)
    computer_score = rsvc.roll_turn(num_dice=4)

    if player_score > computer_score:
        print(f"You won!!!!!")
    else:
        print("Sorry. You lost this game.")
        exit(0)

    print(f"Your Score: {player_score}")
    print(f"Computer Score: {computer_score}")

    current_player_id = current_player['id']
    rsvc.record_score(player_id=current_player_id, current_score=player_score)
    print("Checking to see if you hit a new personal high score...")
    broken_high_score = rsvc.check_high_score(player_id=current_player_id, current_score=player_score)
    if broken_high_score:
        print("Congratulations you hit an all time high! Recording your new high score.")
        rsvc.record_high_score(player_id=current_player_id, current_score=player_score)

if __name__ == '__main__':
    main()
