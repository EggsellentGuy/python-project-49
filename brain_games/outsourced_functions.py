import random
import prompt


#function to generate random number
def generating_randint():
    num = random.randint(1, 100)
    return num


#function to check if a number is even
def even_check(num: int):
    if num % 2 == 0:
        return 'yes'
    else:
        return 'no'


#the main function of the game "brin even"
def even_game_main_function(even_int: str, random_int: int):
    print(f'Question: {random_int}')
    answer = prompt.string('Your answer ')
    if even_int == answer:
        print('Correct!')
        return True
    else:
        print(f"'{answer}' is wrong answer ;(. Correct answer was '{even_int}'.")
        return False

