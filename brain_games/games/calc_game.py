from brain_games.cli import welcome_user
from brain_games.constants import MAX_RAUNDS
from brain_games.outsourced_functions import (
    generating_randint,
    say_loosing_phrase
)
import prompt
import random


COLCULATE_SIMWOLS = ['+', '-', '*']


def calc_game():
    name = welcome_user()
    print("What is the result of the expression?")
    for _ in range(MAX_RAUNDS):
        first_argument = generating_randint(50)
        second_argument = generating_randint(50)
        simvol = generation_calculate_simbol(COLCULATE_SIMWOLS)
        print(f"Question: {first_argument} {simvol} {second_argument}")
        answer = prompt.string('Your answer ')
        correct_answer = count_correct_answer(
            first_argument,
            second_argument,
            simvol
        )
        if int(correct_answer) == int(answer):
            print('Correct!')
            continue
        else:
            say_loosing_phrase(answer, correct_answer, name)
            break
    else:
        print(f'Congratulations, {name}!')


def count_correct_answer(
    first_argument: int,
    second_argument: int,
    simvol: str
) -> int:
    match simvol:
        case '+':
            return first_argument + second_argument
        case '-':
            return first_argument - second_argument
        case '*':
            return first_argument * second_argument


def generation_calculate_simbol(some_list: list):
    rundom_simvom = random.randint(0, len(COLCULATE_SIMWOLS) - 1)
    return some_list[rundom_simvom]
