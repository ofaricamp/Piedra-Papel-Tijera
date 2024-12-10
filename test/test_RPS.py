import pytest
from src.RPS import GameComputerResult, GameAction, assess_game

@pytest.mark.draw
def test_draw():
    '''
    Partidas con empate
    '''

    assert GameComputerResult.Draw == assess_game(
        user_action=GameAction.Rock,
        computer_action=GameAction.Rock)

    assert GameComputerResult.Draw == assess_game(
        user_action=GameAction.Scissors, 
        computer_action=GameAction.Scissors)

    assert GameComputerResult.Draw == assess_game(
        user_action=GameAction.Paper,
        computer_action=GameAction.Paper)

@pytest.mark.rock
def test_rock_loses():
    '''
    Rock pierde con Paper 
    '''
    assert GameComputerResult.Lose == assess_game(
        user_action=GameAction.Paper,
        computer_action=GameAction.Rock)

@pytest.mark.rock
def test_rock_wins():
    '''
    Rock gana a Scissors
    '''
    assert GameComputerResult.Win == assess_game(
        user_action=GameAction.Scissors,
        computer_action=GameAction.Rock)

@pytest.mark.paper
def test_paper_loses():
    '''
    Paper pierde con Scissors
    '''
    assert GameComputerResult.Lose == assess_game(
        user_action=GameAction.Scissors,
        computer_action=GameAction.Paper)

@pytest.mark.paper
def test_paper_wins():
    '''
    Paper gana a Rock
    '''
    assert GameComputerResult.Win == assess_game(
        user_action=GameAction.Rock,
        computer_action=GameAction.Paper)

@pytest.mark.scissors
def test_scissors_loses():
    '''
    Scissors pierde con Rock 
    '''
    assert GameComputerResult.Lose == assess_game(
        user_action=GameAction.Rock,
        computer_action=GameAction.Scissors)

@pytest.mark.scissors
def test_scissors_wins():
    '''
    Scissors gana a Paper 
    '''
    assert GameComputerResult.Win == assess_game(
        user_action=GameAction.Paper,
        computer_action=GameAction.Scissors)
