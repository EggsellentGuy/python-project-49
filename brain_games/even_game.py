from brain_games.constant import generating_randint, even_check
import prompt
from brain_games.cli import welcome_user


def even_game():
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    for i in range(3):
        random_int = generating_randint()
        print(f'Question: {random_int}')
        answer = prompt.string('Your answer ')
        if even_check(random_int) == 'yes':
            if answer.lower() == 'yes':
                print('Correct!')
                continue
            else:
                print("'no' is wrong answer ;(. Correct answer was 'yes'.")
                break
        elif even_check(random_int) == 'no':
            if answer.lower() == 'no':
                print('Correct!')
                continue
            else:
                print("'yes' is wrong answer ;(. Correct answer was 'no'.")
                break

    print(f'Congratulations, {name}')
