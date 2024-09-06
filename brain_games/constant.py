import random


def generating_randint():
    num = random.randint(1, 100)
    return num


def even_check(num: int):
    if num % 2 == 0:
        return 'yes'
    else:
        return 'no'
