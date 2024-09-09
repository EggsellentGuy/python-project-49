import random
import prompt
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


def generation_calculate_question():
    question = []
    question.append(str(generating_randint())) 
    question.append(generation_calculate_simbol(COLCULATE_SIMWOLS))
    question.append(str(generating_randint()))
    answer = " ".join(question)
    return answer
    

def generation_calculate_simbol(some_list: list):
    rundom_simvom = random.randint(0, 2)
    return some_list[rundom_simvom]