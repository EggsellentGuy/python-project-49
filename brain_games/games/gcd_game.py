import random


GCD_RULES = 'Find the greatest common divisor of given numbers.'


def Question_Generator_Gcd():
    first_num = random.randint(1, 50)
    second_num = random.randint(1, 50)
    print(f"Question: {first_num} {second_num}")
    return count_gcd(first_num, second_num)


def count_gcd(first_num: int, second_num: int) -> int:
    while second_num != 0:
        remainder = first_num % second_num
        first_num = second_num
        second_num = remainder
    return first_num
