from brain_games.outsourced_functions import generating_randint, even_check
from brain_games.cli import welcome_user
from brain_games.constants import MAX_RAUNDS
import prompt


def even_game():
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    correct_answers = 0
    for i in range(MAX_RAUNDS):
        rand_int = generating_randint()
        even_check_randint = even_check(rand_int)
        if even_game_main_function(even_check_randint, rand_int):
            correct_answers += 1
            continue
        else:
            break

    if correct_answers == 3:
        print(f'Congratulations, {name}')


def even_game_main_function(even_int: str, random_int: int):
    print(f'Question: {random_int}')
    answer = prompt.string('Your answer ')
    if even_int == answer.lower():
        print('Correct!')
        return True
    else:
        print(f"'{answer.lower()}' is wrong answer ;(.\
 Correct answer was '{even_int}'.")
        return False
