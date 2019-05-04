# 1. nacita tah uzivatele DONE
# 2. validovat tah uzivatele DONE
# 3. zahrat nahodny tah DONE
# 4. informovat hrace o tahu DONE
# 5. Vyhodnoceni tahů DONE
# 6. informovat hrace o vysledku hry DONE

from random import choice
import rsp_lib


def main():
    list_choices = ["rock", "paper", "scissors"]
    valid = False
    while not valid:
        player_choice = input("Rock, Paper or Scissors:\n")
        player_choice = player_choice.lower()
        valid = rsp_lib.is_valid_choice(player_choice)

    print("Player choiced:", player_choice)

    AI_choice = choice(list_choices)

    print("Computer choiced:", AI_choice)

    result = rsp_lib.get_game_results(player_choice, AI_choice)

    return result


if __name__ == "__main__":
    main()
