from random import choice


LIST_CHOICES = ["rock", "paper", "scissors"]


def is_valid_choice(player_choice):
    return player_choice.lower() in LIST_CHOICES


def random_choice():
    return choice(LIST_CHOICES)


def get_game_results(player_choice, AI_choice):
    if player_choice.lower() == AI_choice:
        print("Tie !")
        return 0

    elif player_choice.lower() == "rock" and AI_choice == "scissors" \
        or player_choice.lower() == "paper" and AI_choice == "rock" \
            or player_choice.lower() == "scissors" and AI_choice == "paper":
        print("Player won !")
        return 1

    else:
        print("Player lost !")
        return -1
