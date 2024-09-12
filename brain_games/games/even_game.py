from brain_games.outsourced_functions import (
    generating_randint,
    even_check,
    say_loosing_phrase
)
from brain_games.cli import welcome_user
from brain_games.constants import MAX_RAUNDS
import prompt


def even_game():
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    for i in range(MAX_RAUNDS):
        rand_int = generating_randint()
        even_check_randint = even_check(rand_int)
        if even_game_main_function(even_check_randint, rand_int):
            continue
        else:
            break

    else:
        print(f'Congratulations, {name}')


def even_game_main_function(even_int: str, random_int: int):
    print(f'Question: {random_int}')
    answer = prompt.string('Your answer ')
    if even_int == answer.lower():
        print('Correct!')
        return True
    else:
        say_loosing_phrase(answer, even_int)
        return False
