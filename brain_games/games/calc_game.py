import random


COLCULATE_SIMWOLS = ['+', '-', '*']
CALC_RULES = "What is the result of the expression?"


def Question_Generator_Calc():
    first_argument = random.randint(1, 50)
    second_argument = random.randint(1, 50)
    simvol = generation_calculate_simbol(COLCULATE_SIMWOLS)
    print(f"Question: {first_argument} {simvol} {second_argument}")
    correct_answer = count_correct_answer(
        first_argument,  # Уменьшил отступ
        second_argument,
        simvol
    )
    return correct_answer


def count_correct_answer(
    first_argument: int,
    second_argument: int,
    simvol: str
):
    match simvol:
        case '+':
            return first_argument + second_argument
        case '-':
            return first_argument - second_argument
        case '*':
            return first_argument * second_argument


def generation_calculate_simbol(some_list: list):
    rundom_simvom = random.randint(0, len(COLCULATE_SIMWOLS) - 1)
    return some_list[rundom_simvom]
