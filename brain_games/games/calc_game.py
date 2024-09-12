from brain_games.cli import welcome_user
from brain_games.constants import MAX_RAUNDS, COLCULATE_SIMWOLS
from brain_games.outsourced_functions import (
    generating_randint,
    generation_calculate_simbol,
    say_loosing_phrase
)
import prompt


def calc_game():
    name = welcome_user()
    count = 0
    for i in range(MAX_RAUNDS):
        first_argument = generating_randint(50)
        second_argument = generating_randint(50)
        simvol = generation_calculate_simbol(COLCULATE_SIMWOLS)
        print(f"Question: {first_argument} {simvol} {second_argument}")
        answer = prompt.string('Your answer ')
        correct_answer = count_correct_answer(first_argument, second_argument, simvol)
        if int(correct_answer) == int(answer):
            print('Correct!')
            count += 1
            continue
        else:
            say_loosing_phrase(answer, correct_answer)
            break
    if count == 3:
        print(f'Congratulations, {name}')


def count_correct_answer(first_argument, second_argument, simvol):
    match simvol:
        case '+':
            return first_argument + second_argument
        case '-':
            return first_argument - second_argument
        case '*':
            return first_argument * second_argument
