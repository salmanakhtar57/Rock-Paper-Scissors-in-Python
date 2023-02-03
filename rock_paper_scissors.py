import random

def get_computer_choice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def play_round(player_selection, computer_selection):
    if player_selection == computer_selection:
        print(f"Both selected {player_selection}. It's a draw.")
        return 0
    elif player_selection == "rock" and computer_selection == "scissors" or player_selection == "paper" and computer_selection == "rock" or player_selection == "scissors" and computer_selection == "paper":
        print(f"You choose {player_selection} and computer Choose {computer_selection} \nCongrats You win!" )
        return 1
    else:
        print(f"You choose {player_selection} and computer choose {computer_selection} \nYou lose!")
        return -1

def game():
    player_score = 0
    computer_score = 0

    for i in range(5):
        player_selection = input("\nPick your choice, 'Rock', 'Paper' or 'Scissors': ")
        computer_selection = get_computer_choice()

        result = play_round(player_selection, computer_selection)

        if result == 1:
            player_score += 1
        elif result == -1:
            computer_score += 1

    if player_score > computer_score:
        print(f"\nFinal score: {player_score} - {computer_score}. You won the game!")
    elif player_score < computer_score:
        print(f"\nFinal score: {player_score} - {computer_score}. You loss the game!")
    else:
        print(f"\nFinal score: {player_score} - {computer_score}. Its a draw")

game()