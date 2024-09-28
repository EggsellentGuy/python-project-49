import random


EVEN_RULES = 'Answer "yes" if the number is even, \
otherwise answer "no".'


def Question_Generator_Even():
    rand_int = random.randint(1, 100)
    expression = f"{rand_int}"
    even_check_randint = even_check(rand_int)
    if even_check_randint:
        return expression, 'yes'
    else:
        return expression, 'no'


def even_check(num: int):
    return num % 2 == 0
