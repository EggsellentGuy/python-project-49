import random


EVEN_QUESTION_CONST = 'Answer "yes" if the number is even, \
otherwise answer "no".'


def Question_Generator_Even():
    rand_int = random.randint(1, 100)
    print(f"Question: {rand_int}")
    even_check_randint = even_check(rand_int)
    if even_check_randint:
        return 'yes'
    else:
        return 'no'


def even_check(num: int):
    return num % 2 == 0
