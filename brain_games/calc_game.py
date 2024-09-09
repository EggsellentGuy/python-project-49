from brain_games.cli import welcome_user
from brain_games.constants import MAX_RAUNDS
from brain_games.outsourced_functions import generating_randint, generation_calculate_simbol
import prompt
from brain_games.constants import COLCULATE_SIMWOLS


def calc_game():
    name = welcome_user()
    count = 0
    for i in range(MAX_RAUNDS):
        first_argument = generating_randint()
        second_argument = generating_randint()
        simvol = generation_calculate_simbol(COLCULATE_SIMWOLS)
        print(f"Question: {first_argument} {simvol} {second_argument}")
        answer = prompt.string('Your answer ')
        correct_answer = count_correct_answer(first_argument, second_argument, simvol)
        if int(correct_answer) == int(answer):
            print('Correct!')
            count += 1
            continue
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
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
