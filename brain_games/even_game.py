from brain_games.outsourced_functions import generating_randint, even_check
from brain_games.outsourced_functions import even_game_main_function
from brain_games.cli import welcome_user


def even_game():
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    correct_answers = 0
    for i in range(3):
        rand_int = generating_randint()
        even_check_randint = even_check(rand_int)
        if even_game_main_function(even_check_randint, rand_int):
            correct_answers += 1
            continue
        else:
            break

    if correct_answers == 3:
        print(f'Congratulations, {name}')
