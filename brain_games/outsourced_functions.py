import random
import prompt


def generating_randint():
    num = random.randint(1, 100)
    return num


def even_check(num: int):
    if num % 2 == 0:
        return 'yes'
    else:
        return 'no'


def even_game_main_function(even_int: str, random_int: int):
    print(f'Question: {random_int}')
    answer = prompt.string('Your answer ')
    if even_int == answer:
        print('Correct!')
        return True
    else:
        print(f"'{answer}' is wrong answer ;(. Correct answer was '{even_int}'.")
        return False

