from brain_games.cli import welcome_user
from brain_games.constants import MAX_RAUNDS
from brain_games.outsourced_functions import (
    generating_randint,
    say_loosing_phrase
)
import prompt


def gcd_game():
    name = welcome_user()
    print('Find the greatest common divisor of given numbers.')
    for _ in range(MAX_RAUNDS):
        first_num = generating_randint(50)
        second_num = generating_randint(50)
        print(f"Question: {first_num} {second_num}")
        answer = prompt.string('Your answer ')
        if int(answer) == int(count_gcd(first_num, second_num)):
            print('Correct!')
            continue
        else:
            say_loosing_phrase(answer, count_gcd(first_num, second_num))
            break
    else:
        print(f'Congratulations, {name}')


def count_gcd(first_num: int, second_num: int) -> int:
    while second_num != 0:
        remainder = first_num % second_num
        first_num = second_num
        second_num = remainder
    return first_num
