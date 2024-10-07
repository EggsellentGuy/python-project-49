import random


GAME_RULES = 'Answer "yes" if the number is even, \
otherwise answer "no".'


def generate_question():
    rand_int = random.randint(1, 100)
    expression = f"{rand_int}"
    value = even_check(rand_int)
    answer = 'yes' if value else 'no'
    return expression, answer


def even_check(num):
    return num % 2 == 0
