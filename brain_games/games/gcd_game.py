import random


GAME_RULES = 'Find the greatest common divisor of given numbers.'


def generate_question():
    first_num = random.randint(1, 50)
    second_num = random.randint(1, 50)
    expression = f"{first_num} {second_num}"
    return expression, count_gcd(first_num, second_num)


def count_gcd(first_num: int, second_num: int) -> int:
    while second_num != 0:
        remainder = first_num % second_num
        first_num = second_num
        second_num = remainder
    return first_num
