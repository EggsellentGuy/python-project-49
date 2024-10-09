import random
from math import sqrt

GAME_RULES = 'Answer "yes" if given number is prime. \
Otherwise answer "no".'


def generate_question():
    prime_chek_num = random.randint(1, 100)
    expression = f"{prime_chek_num}"
    value = is_prime_number(prime_chek_num)
    answer = 'yes' if value else 'no'
    return expression, answer


def is_prime_number(num):
    if num < 2:
        return False
    for i in range(2, int(sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True
