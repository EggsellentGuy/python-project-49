from brain_games.constant import RANDOM_INT
import prompt
from brain_games.cli import name


def even_game():
    print('Answer "yes" if the number is even, otherwise answer "no".')
    for i in range(3):
        print(f'Question: {RANDOM_INT}')
        answer = prompt.string('Your answer ')
        if even_check(RANDOM_INT) == 'yes':
            if answer == 'yes':
                print('Correct!')
                continue
            else:
                print("'no' is wrong answer ;(. Correct answer was 'yes'.")
                break
        elif even_check(RANDOM_INT) == 'no':
            if answer == 'no':
                print('Correct!')
                continue
            else:
                print("'yes' is wrong answer ;(. Correct answer was 'no'.")
                break

    print(f'Congratulations, {name}')


def even_check(num:int):
    if num % 2 == 0:
        return 'yes'
    else:
        return 'no' 
