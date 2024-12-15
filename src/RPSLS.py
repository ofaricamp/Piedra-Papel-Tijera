import random
from enum import IntEnum

result = 0
last_user_action = 0
last_computer_action = 0
class GameAction(IntEnum):

    Rock = 0
    Paper = 1
    Scissors = 2
    Lizard = 3
    Spock = 4

class GameComputerResult(IntEnum):
    Lose = 0
    Win = 1
    Draw = 2

WinConditions = {
    GameAction.Rock: [GameAction.Paper,GameAction.Spock],
    GameAction.Paper: [GameAction.Scissors, GameAction.Lizard],
    GameAction.Scissors: [GameAction.Rock,GameAction.Spock],
    GameAction.Lizard: [GameAction.Scissors, GameAction.Rock],
    GameAction.Spock:[GameAction.Paper, GameAction.Lizard]
}

def assess_game(user_action, computer_action):
    global result
    if user_action == computer_action:
        print(f"User and computer picked {user_action.name}. Draw game!")
        result = GameComputerResult.Draw
    elif computer_action in WinConditions[user_action]:
        print(f"Computer picked {computer_action}, you lose!")
        result = GameComputerResult.Win
    else:
        print(f"computer picked {computer_action}, you win!")
        result = GameComputerResult.Lose    
    return result


def get_computer_action():
    global result
    global last_user_action
    global last_computer_action

    if result == GameComputerResult.Win:
       choice = [option for option in WinConditions if option not in [last_computer_action,last_user_action]]
       computer_selection = random.choice(WinConditions[choice])
    elif result == GameComputerResult.Lose:
         computer_selection =  random.choice(WinConditions[last_user_action])
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
    global last_user_action
    global last_computer_action
    while True:
        try:
            user_action = get_user_action()
        except ValueError:
            range_str = f"[0, {len(GameAction) - 1}]"
            print(f"Invalid selection. Pick a choice in range {range_str}!")
            continue

        computer_action = get_computer_action()
        last_user_action = user_action
        last_computer_action = computer_action
        assess_game(user_action, computer_action)

        if not play_another_round():
            break

if __name__ == "__main__":
    main()