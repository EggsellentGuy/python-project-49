import random


OPERATORS = ['+', '-', '*']
GAME_RULES = "What is the result of the expression?"


def generate_question():
    first_argument = random.randint(1, 50)
    second_argument = random.randint(1, 50)
    simvol = random.choice(OPERATORS)
    expression = f"{first_argument} {simvol} {second_argument}"
    correct_answer = count_correct_answer(first_argument,
                                          second_argument,
                                          simvol
                                          )
    return expression, correct_answer


def count_correct_answer(first_argument,
                         second_argument,
                         simvol):
    try:
        match simvol:
            case '+':
                return first_argument + second_argument
            case '-':
                return first_argument - second_argument
            case '*':
                return first_argument * second_argument
    except (ValueError, SyntaxError):
        print("Use only symbols for mathematical operations")
