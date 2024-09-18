from brain_games.cli import welcome_user
from brain_games.constants import MAX_RAUNDS
from brain_games.outsourced_functions import (
    generating_randint, is_user_win
)
import prompt


def prime_game():
    name = welcome_user()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    for _ in range(MAX_RAUNDS):
        prime_chek_num = generating_randint()
        print(f"Question: {prime_chek_num}")
        user_answer = prompt.string('Your answer ')
        correct_answer = is_prime_number(prime_chek_num)
        if is_user_win(user_answer, correct_answer, name):
            continue
        else:
            break
    else:
        print(f'Congratulations, {name}!')


def is_prime_number(num: int):
    match num:
        case _ if num <= 1:
            return 'no'
        case _ if num <= 3:
            return 'yes'
        case _ if num % 2 == 0 or num % 3 == 0:
            return 'no'
        case _:
            i = 5
            while i * i <= num:
                if num % i == 0 or num % (i + 2) == 0:
                    return 'no'
                i += 6
            return 'yes'
