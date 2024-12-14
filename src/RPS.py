import random
from enum import IntEnum

result = 0
last_user_action = 0
class GameAction(IntEnum):

    Rock = 0
    Paper = 1
    Scissors = 2

class GameComputerResult(IntEnum):
    Lose = 0
    Win = 1
    Draw = 2


def assess_game(user_action, computer_action):
    global result
    if user_action == computer_action:
        print(f"User and computer picked {user_action.name}. Draw game!")
        result = GameComputerResult.Draw

    # You picked Rock
    elif user_action == GameAction.Rock:
        if computer_action == GameAction.Scissors:
            print("Rock smashes scissors. You won!")
            result = GameComputerResult.Lose
        else:
            print("Paper covers rock. You lost!")
            result = GameComputerResult.Win

    # You picked Paper
    elif user_action == GameAction.Paper:
        if computer_action == GameAction.Rock:
            print("Paper covers rock. You won!")
            result = GameComputerResult.Lose
        else:
            print("Scissors cuts paper. You lost!")
            result = GameComputerResult.Win

    # You picked Scissors
    elif user_action == GameAction.Scissors:
        if computer_action == GameAction.Rock:
            print("Rock smashes scissors. You lost!")
            result = GameComputerResult.Win
        else:
            print("Scissors cuts paper. You won!")
            result = GameComputerResult.Lose
    return result


def get_computer_action():
    global result
    global last_user_action
    if result == GameComputerResult.Win:
        computer_selection = last_user_action
    elif result == GameComputerResult.Lose:

        #User pick Rock last round
        if last_user_action == GameAction.Rock:
            computer_selection = GameAction.Paper
            
        # User pick Paper last round
        elif last_user_action == GameAction.Paper:
           computer_selection =  GameAction.Scissors

        # User pick Scissor last round
        elif last_user_action == GameAction.Scissors:
           computer_selection =  GameAction.Rock  
    else:
        computer_selection =  random.randint(0, len(GameAction) - 1)
    computer_action = GameAction(computer_selection)
    print(f"Computer picked {computer_action.name}.")

    return computer_action


def get_user_action():
    # Scalable to more options (beyond rock, paper and scissors...)
    game_choices = [f"{game_action.name}[{game_action.value}]" for game_action in GameAction]
    game_choices_str = ", ".join(game_choices)
    user_selection = int(input(f"\nPick a choice ({game_choices_str}): "))
    user_action = GameAction(user_selection)

    return user_action


def play_another_round():
    another_round = input("\nAnother round? (y/n): ")
    return another_round.lower() == 'y'


def main():

    while True:
        try:
            user_action = get_user_action()
        except ValueError:
            range_str = f"[0, {len(GameAction) - 1}]"
            print(f"Invalid selection. Pick a choice in range {range_str}!")
            continue

        computer_action = get_computer_action()
        global last_user_action
        last_user_action = user_action
        assess_game(user_action, computer_action)

        if not play_another_round():
            break


if __name__ == "__main__":
    main()