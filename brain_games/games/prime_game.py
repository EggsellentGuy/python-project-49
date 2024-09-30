import random

GAME_RULES = 'Answer "yes" if given number is prime. \
Otherwise answer "no".'


def Generate_question():
    prime_chek_num = random.randint(1, 100)
    expression = f"{prime_chek_num}"
    value = is_prime_number(prime_chek_num)
    answer = 'yes' if value else 'no'
    return expression, answer


def is_prime_number(num: int) -> bool:
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True
