import random
from brain_games.constants import COLCULATE_SIMWOLS


# function to generate random number
def generating_randint():
    num = random.randint(1, 100)
    return num


# function to check if a number is even
def even_check(num: int):
    if num % 2 == 0:
        return 'yes'
    else:
        return 'no'


# function to chose random simbol
def generation_calculate_simbol(some_list: list):
    rundom_simvom = random.randint(0, len(COLCULATE_SIMWOLS) - 1)
    return some_list[rundom_simvom]
