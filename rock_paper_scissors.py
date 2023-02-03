import random

def get_computer_choice():
  choices = ['rock', 'paper', 'scissors']
  return random.choice(choices)

def play_round(player_selection, computer_selection):
  if player_selection == computer_selection:
    print(f"Both selected {player_selection}. It's a draw.")
  elif player_selection == "rock" and computer_selection == "scissors" or player_selection == "paper" and computer_selection == "rock" or player_selection == "scissors" and computer_selection == "paper":
    print(f"You choose {player_selection}. Computer Choose {computer_selection} Congrats You win!" )
  else:
    print(f"You choose {player_selection}. Computer choose {computer_selection} You lose!")

def game():
  player_score = 0
  computer_score = 0

  for i in range(5):
    player_selection = input("Choose one option: ")
    computer_selection = get_computer_choice()

    result = play_round(player_selection, computer_selection)

    if result == 1:
      player_score += 1
    elif result == -1:
      computer_score += 1

  if player_score > computer_score:
    print(f"Final score: {player_score} - {computer_score}. You Win!")
  elif player_score < computer_score:
    print(f"Final score: {player_score} - {computer_score}. You loss!")
  else:
    print(f"Final score: {player_score} - {computer_score}. Its a draw")

game()