from random import choice

player_choice = input("Rock, Paper or Scissors:\n")

list_choices = ["rock", "paper", "scissors"]

AI_choice = choice(list_choices)
print("Computer choiced:", AI_choice)

if player_choice.lower() in list_choices:
    if player_choice.lower() == AI_choice:
        print("Tie!")

    elif player_choice.lower() == "rock" and AI_choice == "scissors" \
        or player_choice.lower() == "paper" and AI_choice == "rock" \
            or player_choice.lower() == "scissors" and AI_choice == "paper":
        print("Player won !")

    else:
        print("Player lost !")
else:
    print("Wrong input of player")
