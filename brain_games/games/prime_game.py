import random

PRIME_RULES = 'Answer "yes" if given number is prime. \
Otherwise answer "no".'


def Question_Generator_Prime():
    prime_chek_num = random.randint(1, 100)
    expression = f"{prime_chek_num}"
    return expression, is_prime_number(prime_chek_num)


def is_prime_number(num: int):
    match num:
        case _ if num <= 1:
            return 'no'
        case _ if num <= 3:
            return 'yes'
        case _ if num % 2 == 0 or num % 3 == 0:
            return 'no'
        case _:
            i = 5
            while i * i <= num:
                if num % i == 0 or num % (i + 2) == 0:
                    return 'no'
                i += 6
            return 'yes'
