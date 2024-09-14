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
    for _ in range(MAX_RAUNDS):
        rand_int = generating_randint()
        print(f"Question: {rand_int}")
        even_check_randint = even_check(rand_int)
        answer = prompt.string('Your answer ')
        if even_check_randint == answer.lower():
            print('Correct!')
            continue
        else:
            say_loosing_phrase(answer, even_check_randint, name)
            break
    else:
        print(f'Congratulations, {name}!')



