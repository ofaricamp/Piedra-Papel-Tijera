import pytest
from src.RPSLS import GameComputerResult, GameAction, assess_game


# @pytest.fixture
# def game():
#     '''
#     Setup del objeto game
#     '''
#     setup_game = Game()
#     return setup_game


@pytest.mark.draw
def test_draw():

    assert GameComputerResult.Draw == assess_game(
        user_action=GameAction.Spock,
        computer_action=GameAction.Spock)

    assert GameComputerResult.Draw == assess_game(
        user_action=GameAction.Lizard,
        computer_action=GameAction.Lizard)

    assert GameComputerResult.Draw == assess_game(
        user_action=GameAction.Rock,
        computer_action=GameAction.Rock)

    assert GameComputerResult.Draw == assess_game(
        user_action=GameAction.Scissors,
        computer_action=GameAction.Scissors)

    assert GameComputerResult.Draw == assess_game(
        user_action=GameAction.Paper,
        computer_action=GameAction.Paper)


@pytest.mark.spock
def test_spock_loses():
    '''
    Spock pierde con Lizard y Paper 
    '''
    assert GameComputerResult.Lose == assess_game(
        user_action=GameAction.Paper,
        computer_action=GameAction.Spock)

    assert GameComputerResult.Lose == assess_game(
        user_action=GameAction.Lizard,
        computer_action=GameAction.Spock)


@pytest.mark.spock
def test_spock_wins():
    '''
    Spock gana a Rock y Scissors 
    '''
    assert GameComputerResult.Win == assess_game(
        user_action=GameAction.Rock,
        computer_action=GameAction.Spock)

    assert GameComputerResult.Win == assess_game(
        user_action=GameAction.Scissors,
        computer_action=GameAction.Spock)


@pytest.mark.lizard
def test_lizard_loses():
    '''
    Lizard pierde con Rock y Scissors 
    '''
    assert GameComputerResult.Lose == assess_game(
        user_action=GameAction.Rock,
        computer_action=GameAction.Lizard)

    assert GameComputerResult.Lose == assess_game(
        user_action=GameAction.Scissors,
        computer_action=GameAction.Lizard)


@pytest.mark.lizard
def test_lizard_wins():
    '''
    Lizard gana a Spock y Paper 
    '''
    assert GameComputerResult.Win == assess_game(
        user_action=GameAction.Spock,
        computer_action=GameAction.Lizard)

    assert GameComputerResult.Win == assess_game(
        user_action=GameAction.Paper,
        computer_action=GameAction.Lizard)


@pytest.mark.rock
def test_rock_loses():
    '''
    Rock pierde con Spock y Paper 
    '''
    assert GameComputerResult.Lose == assess_game(
        user_action=GameAction.Spock,
        computer_action=GameAction.Rock)

    assert GameComputerResult.Lose == assess_game(
        user_action=GameAction.Paper,
        computer_action=GameAction.Rock)


@pytest.mark.rock
def test_rock_wins():
    '''
    Rock gana a Scissors y Lizard 
    '''
    assert GameComputerResult.Win == assess_game(
        user_action=GameAction.Scissors,
        computer_action=GameAction.Rock)

    assert GameComputerResult.Win == assess_game(
        user_action=GameAction.Lizard,
        computer_action=GameAction.Rock)


@pytest.mark.paper
def test_paper_loses():
    '''
    Paper pierde con Scissors y Lizard 
    '''
    assert GameComputerResult.Lose == assess_game(
        user_action=GameAction.Scissors,
        computer_action=GameAction.Paper)

    assert GameComputerResult.Lose == assess_game(
        user_action=GameAction.Lizard,
        computer_action=GameAction.Paper)


@pytest.mark.paper
def test_paper_wins():
    '''
    Paper gana a Rock y Spock 
    '''
    assert GameComputerResult.Win == assess_game(
        user_action=GameAction.Rock,
        computer_action=GameAction.Paper)

    assert GameComputerResult.Win == assess_game(
        user_action=GameAction.Spock,
        computer_action=GameAction.Paper)


@pytest.mark.scissors
def test_scissors_loses():
    '''
    Scissors pierde con Spock y Rock 
    '''
    assert GameComputerResult.Lose == assess_game(
        user_action=GameAction.Spock,
        computer_action=GameAction.Scissors)

    assert GameComputerResult.Lose == assess_game(
        user_action=GameAction.Rock,
        computer_action=GameAction.Scissors)


@pytest.mark.scissors
def test_scissors_wins():
    '''
    Scissors gana a Lizard y Paper 
    '''
    assert GameComputerResult.Win == assess_game(
        user_action=GameAction.Lizard,
        computer_action=GameAction.Scissors)

    assert GameComputerResult.Win == assess_game(
        user_action=GameAction.Paper,
        computer_action=GameAction.Scissors)